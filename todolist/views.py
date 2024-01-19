from django.shortcuts import render
from todolist.models import Task
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.

class GetTasks(APIView):
    def get(self, request):
        all_tasks = Task.objects.all()
        task_list = []
        for task in all_tasks:
            task_dict = {
                'id': task.id,
                'task': task.task,
                'done': task.done
            }
            task_list.append(task_dict)
        print(task_list)
        return Response({'all_tasks': task_list})

class AddTask(APIView):
    def post(self, request):
        print(request.data)
        task_data = request.data['task']
        task = task_data.get('task')
        done = request.data['done']
        if task != '':
            new_database_entry = Task(task=task, done=done)
            #new_database_entry.save(commit=False).manager = request.user
            new_database_entry.save()
            return Response({'message': 'success'})
        else:
            return Response({'message': 'failure'})
        
class DeleteTask(APIView):
    def delete(self, request, task_id):
        try:
            task = Task.objects.get(pk=task_id)
            task.delete()
            return Response({'message': 'Deleted Successfully'})
        except Exception as e:
            return Response({'message': str(e)})