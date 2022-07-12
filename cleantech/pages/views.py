from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'pages/home.html', context)


def about(request):
    context = {}
    return render(request, 'pages/about.html', context)