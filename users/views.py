from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from users.forms import CustomRegisterForm

# Create your views here.
#task_data = request.data['task']
#task = task_data.get('task')
#done = request.data['done']

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