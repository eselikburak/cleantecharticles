from django.shortcuts import render
from .models import Home
from accounts.models import Profile

def home(request):
    num_of_authors = Profile.objects.filter(user_type='blog_author').count()
    num_of_authors += Profile.objects.filter(user_type='tutorial_author').count()
    context = {
        'home_content': Home.objects.all()[0],
        'num_of_authors': num_of_authors,
    }
    return render(request, 'pages/home.html', context)


def about(request):
    context = {
        'home_content': Home.objects.all()[0]
    }
    return render(request, 'pages/about.html', context)

def contact(request):
    return render(request, 'pages/contact.html')