from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from users.forms import CustomRegisterForm

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