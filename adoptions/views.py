from django.shortcuts import render, get_object_or_404, redirect
from .models import GuineaPig, Adoption
from django.contrib.auth.decorators import login_required
from .forms import AdoptionForm

# Create your views here.

# View for displaying available guinea pigs for adoption
def available_guinea_pigs(request):
    guinea_pigs = GuineaPig.objects.filter(adopted=False)
    return render(request, 'adoptions/available_guinea_pigs.html', {'guinea_pigs': guinea_pigs})

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
                number_of_guinea_pigs=form.cleaned_data['number_of_guinea_pigs'],
                living_arrangement=form.cleaned_data['living_arrangement'],
            )
            adoption.save()

           
            return redirect('adoptions:adoption_success')
    else:
        form = AdoptionForm()

    return render(request, 'adoptions/adopt_guinea_pig.html', {'guinea_pig': guinea_pig, 'form': form})

def adoption_success(request):
    return render(request, 'adoptions/adoption_success.html')