from django.shortcuts import render
from .models import Home

def home(request):
    context = {
        'home_content': Home.objects.all()[0] 
    }
    return render(request, 'pages/home.html', context)


def about(request):
    context = {
        'home_content': Home.objects.all()[0] 
    }
    return render(request, 'pages/about.html', context)