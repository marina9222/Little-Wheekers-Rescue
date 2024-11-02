from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse
from django.utils import timezone 
from django.db.models import Sum 
from django.views.decorators.csrf import csrf_exempt
import stripe
from .models import Donation




# Create your views here.



def home_view(request):
    donations = Donation.objects.aggregate(total=Sum('amount'))['total']
    template = 'home/index.html'
    context = {
        'donations': donations,
    }
    return render(request, template, context)


def about_us(request):
    return render(request, 'home/about_us.html')

def adoption_policy(request):
    return render(request, 'home/adoption_policy.html')


stripe.api_key = settings.STRIPE_SECRET_KEY

from django.contrib import messages

@csrf_exempt
def donate(request):
    if request.method == 'POST':
        amount = int(request.POST.get('amount')) * 100  # Convert to cents

        # Save the amount to session
        request.session['donation_amount'] = amount

        # Create a Stripe Checkout session
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
    amount = request.session.get('donation_amount')  # Retrieve the amount from session

    if request.user.is_authenticated and amount:
       
        Donation.objects.create(user=request.user, amount=amount / 100)  # Store amount in pounds
        # Clear the session amount after processing
        del request.session['donation_amount']
    
    return render(request, 'home/donation_success.html', {'amount': amount / 100}) 


def donation_cancel(request):
    return render(request, 'home/donation_cancel.html')