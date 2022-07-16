from django.shortcuts import redirect, render
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

def user_login(request):

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        messages.add_message(request, messages.INFO, 'Password or Username invalid!')
        return redirect('home')



def user_logout(request):
    logout(request)
    return redirect('home')