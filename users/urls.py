from django.contrib import admin
from django.urls import path
from users.views import Register
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', auth_views.LogoutView.as_view()) 
]