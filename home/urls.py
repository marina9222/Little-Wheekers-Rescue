from django.contrib import admin
from django.urls import path
from . import views
from home.views import home_view

app_name = 'home' 

urlpatterns = [ 
    path('about/', views.about_us, name='about_us'),
    path('adoption-policy/', views.adoption_policy, name='adoption_policy'),
    path('', home_view, name='home') 
]
