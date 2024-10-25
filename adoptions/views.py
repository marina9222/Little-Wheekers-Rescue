from django.shortcuts import render
from .models import GuineaPig

# Create your views here.

def guinea_pigs(request):
    """ A view to show all guinea pigs including sorting"""

    guinea_pigs = GuineaPig.objects.all()
    
    context = {
        'guinea_pigs':guinea_pigs,
    }


    return render(request, '/templates/guinea_pigs.html', context)