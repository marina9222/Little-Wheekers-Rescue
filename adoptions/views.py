from django.shortcuts import render, get_object_or_404, redirect
from .models import GuineaPig, Adoption
from home.models import Donation
from django.contrib.auth.decorators import login_required
from django.db.models import F
from .forms import AdoptionForm
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

# View for displaying available guinea pigs for adoption
def available_guinea_pigs(request):
    guinea_pigs = GuineaPig.objects.all().order_by("adopted", "name")

    sort_by = request.GET.get('sort', None)

    if sort_by == 'age_asc':
        guinea_pigs = guinea_pigs.order_by('-birth_year')
    elif sort_by == 'age_desc':
        guinea_pigs = guinea_pigs.order_by('birth_year')
    elif sort_by == 'gender_male':
        guinea_pigs = guinea_pigs.filter(gender='M')
    elif sort_by == 'gender_female':
        guinea_pigs = guinea_pigs.filter(gender='F')

    return render(request, 'adoptions/available_guinea_pigs.html', {
        'guinea_pigs': guinea_pigs,
        'selected_sort': sort_by,
    })


@login_required
def my_profile(request):
    # Fetch adoptions and donations for the authenticated user
    adoptions = Adoption.objects.filter(adopter=request.user)
    donations = Donation.objects.filter(
        user=request.user
    ).order_by('-date')  # Assuming 'date' is a field in the Donation model

    return render(request, 'adoptions/my_profile.html', {
        'adoptions': adoptions,
        'donations': donations,
    })


# View for adopting a specific guinea pig
@login_required
def adopt_guinea_pig(request, guinea_pig_id):
    guinea_pig = get_object_or_404(GuineaPig, id=guinea_pig_id)

    if request.method == 'POST':
        form = AdoptionForm(request.POST)
        if form.is_valid():

            adoption = Adoption(
                guinea_pig=guinea_pig,
                adopter=request.user,
                address=form.cleaned_data['address'],
                phone_number=form.cleaned_data['phone_number'],
                number_of_guinea_pigs=form.cleaned_data[
                    'number_of_guinea_pigs'],
                living_arrangement=form.cleaned_data['living_arrangement'],
            )
            adoption.save()
            guinea_pig.adopted = True
            guinea_pig.save()

            user_email = request.user.email
            subject = "Thank you for submitting your adoption form!"
            message = (
                f"Hi {request.user.first_name},\n\n"
                f"Thank you for submitting your adoption form for "
                f"{guinea_pig.name}.\n\n"
                "We are excited to process your application and "
                "will get back to you soon.\n\n"
                "Best regards,\n"
                "The Little Wheekers Rescue Team"
            )
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [user_email]

            try:
                send_mail(subject, message, from_email, recipient_list)
            except Exception as e:
                # Log or handle email sending failure if needed
                print(f"Error sending email: {e}")

            return redirect('adoptions:adoption_success')
    else:
        form = AdoptionForm()

    return render(request, 'adoptions/adopt_guinea_pig.html', {
        'guinea_pig': guinea_pig,
        'form': form,
    })


def adoption_success(request):
    return render(request, 'adoptions/adoption_success.html')
