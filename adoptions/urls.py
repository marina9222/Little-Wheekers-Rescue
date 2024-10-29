from django.urls import path
from . import views
from .views import available_guinea_pigs, adopt_guinea_pig, adoption_success, my_profile

app_name = 'adoptions'


urlpatterns = [
    path('available/', available_guinea_pigs, name='available_guinea_pigs'),  
    path('<int:guinea_pig_id>/adopt/', adopt_guinea_pig, name='adopt_guinea_pig'),
    path('success/', adoption_success, name='adoption_success'),
    path('profile/', my_profile, name='my_profile'),
    ]