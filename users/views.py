from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from users.forms import CustomRegisterForm
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime

class Register(APIView):

    def post(self, request):
        print(request.body)
        print(request.data)

        register = CustomRegisterForm(request.data)
        
        if register.is_valid():
            register.save()
            return Response({'message': 'Account Registered'})
        else:
            return Response({'message': register.errors})

class Login(APIView):    
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        
        user = User.objects.filter(username=username).first()
        if user is None:
            raise AuthenticationFailed('User not Found')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')
        
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {'jwt': token}
        
        return response
    
class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        
        if not token:
            raise AuthenticationFailed('Not Authenticated')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Not Authenticated')
        
        user = User.objects.filter(id=payload['id']).first()
        user_data = {
            'id': user.id,
            'username': user.username,
            'password': user.password
        }
        
        return Response(user_data)
        
class Logout(APIView):
    def post(self, request):
        response = Response()
        
        response.delete_cookie('jwt')
        response.data = {'message': 'success'}
        return response