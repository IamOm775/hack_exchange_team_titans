from django.contrib import admin
from django.urls import path, include
from client import views

urlpatterns = [
    path('', views.ClientDashBoard, name="ClientDashBoard"),
    path('checkout', views.cartcheckout, name="cartcheckout"),
    path('savecart', views.savecart, name="savecart"),
]