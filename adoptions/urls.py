from django.urls import path
from . import views

app_name = 'adoptions'

urlpatterns = [
    path('', views.available_guinea_pigs, name='available_guinea_pigs'),
    path('<int:guinea_pig_id>/adopt/', views.adopt_guinea_pig, name='adopt_guinea_pig'),  # New URL pattern
]