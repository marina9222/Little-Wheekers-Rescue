from django.shortcuts import render,get_object_or_404,redirect
from .models import GuineaPig, Adoption
from django.contrib.auth.decorators import login_required

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
        guinea_pig.adopted = True 
        guinea_pig.save()  
        adopter = request.user.adopter  
        Adoption.objects.create(guinea_pig=guinea_pig, adopter=adopter)  
        return redirect('adoptions:available_guinea_pigs') 

    return render(request, 'adoptions/adopt_guinea_pig.html', {'guinea_pig': guinea_pig}) 
