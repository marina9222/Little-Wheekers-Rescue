from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import stripe

from .models import Donation
from .forms import GuineaPigForm
from adoptions.models import GuineaPig


# Set Stripe API key
stripe.api_key = settings.STRIPE_SECRET_KEY


# Home page view
def home_view(request):
    donations = Donation.objects.aggregate(total=Sum('amount'))['total']
    context = {'donations': donations}
    return render(request, 'home/index.html', context)


# About Us page view
def about_us(request):
    return render(request, 'home/about_us.html')


# Adoption Policy page view
def adoption_policy(request):
    return render(request, 'home/adoption_policy.html')


# Donation page and Stripe integration
@csrf_exempt
@login_required
def donate(request):
    if request.method == 'POST':
        amount = int(request.POST.get('amount')) * 100  # Convert to cents
        request.session['donation_amount'] = amount  # Save the amount

        # Create a Stripe Checkout session
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'gbp',
                    'product_data': {
                        'name': 'Donation to Little Wheekers Rescue'
                    },
                    'unit_amount': amount,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri(
                reverse('home:donation_success')
            ),
            cancel_url=request.build_absolute_uri(
                reverse('home:donation_cancel')
            ),
        )
        return redirect(session.url, code=303)

    return render(request, 'home/donate.html')


def donation_success(request):
    amount = request.session.get('donation_amount')  # Retrieve the amount

    if amount:
        # Save donation to database if user is authenticated
        if request.user.is_authenticated:
            Donation.objects.create(user=request.user, amount=amount / 100)

        # Determine user email
        user_email = request.user.email if request.user.is_authenticated else None

        # Send a thank-you email
        subject = "Thank You for Your Generous Donation!"
        message = (
            f"Dear {request.user.first_name },\n\n"
            f"Thank you for your donation of £{amount / 100:.2f} "
            "to Little Wheekers Rescue. Your support helps us care for and "
            "rehome guinea pigs.\n\n"
            "Best regards,\nThe Little Wheekers Rescue Team"
        )

        if user_email:
            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [user_email]
                )
            except Exception as e:
                print(f"Error sending email: {e}")  # Handle email failure

        # Clear the session amount after processing
        del request.session['donation_amount']

    return render(request, 'home/donation_success.html', {
        'amount': amount / 100
    })


# Donation cancel page
def donation_cancel(request):
    return render(request, 'home/donation_cancel.html')


# Check if user is a manager
def is_manager(user):
    return user.is_superuser


# Management dashboard for adding guinea pigs
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
    return render(request, 'home/management.html', {
        'form': form,
        'guinea_pigs': guinea_pigs
    })


# Edit guinea pig details
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

    return render(request, 'home/edit_guinea_pig.html', {
        'form': form,
        'guinea_pig': guinea_pig
    })


# Delete guinea pig
@user_passes_test(is_manager)
def delete_guinea_pig(request, guinea_pig_id):
    guinea_pig = get_object_or_404(GuineaPig, id=guinea_pig_id)
    if request.method == 'POST':
        guinea_pig.delete()
        messages.success(request, 'Guinea pig deleted successfully!')
        return redirect('/management/')

    return render(request, 'home/delete_guinea_pig.html', {
        'guinea_pig': guinea_pig
    })

