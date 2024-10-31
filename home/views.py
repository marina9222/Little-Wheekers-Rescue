from django.shortcuts import render
import stripe
from django.conf import settings


# Create your views here.



def home_view(request):
    return render(request, 'home/index.html') 

def about_us(request):
    return render(request, 'home/about_us.html')

def adoption_policy(request):
    return render(request, 'home/adoption_policy.html')


stripe.api_key = settings.STRIPE_SECRET_KEY