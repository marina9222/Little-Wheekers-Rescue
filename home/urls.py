from django.contrib import admin
from django.urls import path
from . import views
from home.views import home_view


app_name = 'home' 

urlpatterns = [ 
    path('about/', views.about_us, name='about_us'),
    path('adoption-policy/', views.adoption_policy, name='adoption_policy'),
    path('', home_view, name='home'),
    path('donate/', views.donate, name='donate'),
    path('donate/success/', views.donation_success, name='donation_success'),
    path('donate/cancel/', views.donation_cancel, name='donation_cancel'),
    path('management/', views.management_view, name='management_view'),
]
