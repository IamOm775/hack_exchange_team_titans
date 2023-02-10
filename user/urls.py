from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('profile', views.UserProfile, name="UserProfile"),
    path('userdetails', views.Userdetails, name='Userdetail'),
    
    
]
