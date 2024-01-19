from django.contrib import admin
from django.urls import path
from todolist import views
from todolist.views import GetTasks, AddTask, DeleteTask

urlpatterns = [
    path('tasks', GetTasks.as_view()),
    path('add_tasks', AddTask.as_view()),
    path('delete_task/<task_id>', DeleteTask.as_view())
]
