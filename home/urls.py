from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('search/', views.search, name="search"),
    path('signup', views.HandleSignUp, name="HandleSignUp"),
    path('signup_advertizer', views.HandleSignUp_advertizer, name="HandleSignUp_advertizer"),
    path('createaccount', views.HandleUserSignUp, name="HandleUserSignUp"),
    path('handle_signup_advertizer', views.handle_signup_advertizer, name="handle_signup_advertizer"),
    path('login', views.handleLogin, name="handleLogin"),
    path('logout', views.handleLogout, name="handleLogout"),
    
]
