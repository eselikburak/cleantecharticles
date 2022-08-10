from django.shortcuts import render

# Create your views here.
def tutorial(request, tutorial_name):
    if tutorial_name == 'python':
        return render(request, 'tutorial/tutorial.html')