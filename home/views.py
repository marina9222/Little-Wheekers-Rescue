from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.db.models import Sum 
from django.views.decorators.csrf import csrf_exempt
import stripe
from .models import Donation
from .forms import GuineaPigForm
from django.contrib.auth.decorators import user_passes_test
from  adoptions.models import GuineaPig



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


def is_manager(user):
    return user.is_superuser

@user_passes_test(is_manager)
def management_view(request):
    if request.method == 'POST':
        form = GuineaPigForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            messages.success(request, 'Guinea pig added successfully!')
            return redirect('/management/')
    else:
        form = GuineaPigForm()

    guinea_pigs = GuineaPig.objects.all()

    return render(request, 'home/management.html', {'form': form, 'guinea_pigs': guinea_pigs})

@user_passes_test(is_manager)
def edit_guinea_pig(request, guinea_pig_id):
    guinea_pig = get_object_or_404(GuineaPig, id=guinea_pig_id)
    
    if request.method == 'POST':
        form = GuineaPigForm(request.POST, request.FILES, instance=guinea_pig)
        if form.is_valid():
            form.save()
            messages.success(request, 'Guinea pig updated successfully!')
            return redirect('/management/')
    else:
        form = GuineaPigForm(instance=guinea_pig)
    
    return render(request, 'home/edit_guinea_pig.html', {'form': form, 'guinea_pig': guinea_pig})

@user_passes_test(is_manager)
def delete_guinea_pig(request, guinea_pig_id):
    guinea_pig = get_object_or_404(GuineaPig, id=guinea_pig_id)
    if request.method == 'POST':
        guinea_pig.delete()
        messages.success(request, 'Guinea pig deleted successfully!')
        return redirect('/management/')
    
    return render(request, 'home/delete_guinea_pig.html', {'guinea_pig': guinea_pig})