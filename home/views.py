from django.shortcuts import render


# Create your views here.



def home_view(request):
    return render(request, 'home/index.html') 
    
def about_us(request):
    return render(request, 'home/about_us.html')

def adoption_policy(request):
    return render(request, 'home/adoption_policy.html')