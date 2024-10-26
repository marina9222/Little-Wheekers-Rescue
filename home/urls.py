from django.contrib import admin
from django.urls import path
from . import views

app_name = 'home' 

urlpatterns = [
    path('', views.index, name='index'),  
    path('about/', views.about_us, name='about_us'),
    path('adoption-policy/', views.adoption_policy, name='adoption_policy'),  
]
