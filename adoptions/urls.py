from django.urls import path
from . import views

urlpatterns = [
    path('', views.guinea_pigs, name='guinea_pigs')
]
