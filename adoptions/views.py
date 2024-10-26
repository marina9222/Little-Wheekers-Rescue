from django.shortcuts import render,get_object_or_404
from .models import GuineaPig

# Create your views here.

def available_guinea_pigs(request):
    guinea_pigs = GuineaPig.objects.filter(adopted=False)
    return render(request, 'adoptions/available_guinea_pigs.html', {'guinea_pigs': guinea_pigs})

def adopt_guinea_pig(request, guinea_pig_id):
    guinea_pig = get_object_or_404(GuineaPig, id=guinea_pig_id)
    if request.method == 'POST':
        guinea_pig.adopted = True
        guinea_pig.save()
        adopter = request.user.adopter  
        Adoption.objects.create(guinea_pig=guinea_pig, adopter=adopter)
        return redirect('adoptions:available_guinea_pigs')

    return render(request, 'adoptions/adopt_guinea_pig.html', {'guinea_pig': guinea_pig})