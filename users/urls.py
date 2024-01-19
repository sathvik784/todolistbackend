from django.contrib import admin
from django.urls import path
from users.views import Register, Login, UserView, Logout
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
    path('user/', UserView.as_view()),
    path('logout/', Logout.as_view()) 
]