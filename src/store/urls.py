from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='home'),
    path('aboutus/', views.Aboutus, name ='aboutus'),
    path('login/', views.userLogin, name ='login'),
    path('register/', views.register, name = "register")

]