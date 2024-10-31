from django.shortcuts import render, redirect
import stripe
from django.conf import settings
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.



def home_view(request):
    return render(request, 'home/index.html') 

def about_us(request):
    return render(request, 'home/about_us.html')

def adoption_policy(request):
    return render(request, 'home/adoption_policy.html')


stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def donate(request):
    if request.method == 'POST':
        amount = int(request.POST.get('amount')) * 100  

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'gbp',
                    'product_data': {
                        'name': 'Donation to Little Wheekers Rescue',
                    },
                    'unit_amount': amount,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('home:donation_success')),
            cancel_url=request.build_absolute_uri(reverse('home:donation_cancel')),
        )
        return redirect(session.url, code=303)

    return render(request, 'home/donate.html')

def donation_success(request):
    return render(request, 'home/donation_success.html')

def donation_cancel(request):
    return render(request, 'home/donation_cancel.html')