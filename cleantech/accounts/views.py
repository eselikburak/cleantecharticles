from django.shortcuts import redirect, render
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def user_login(request):

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        messages.add_message(request, messages.INFO, 'Password or Username invalid!')
        return redirect('home')


@login_required
def user_logout(request):
    logout(request)
    return redirect('home')