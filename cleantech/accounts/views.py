from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def user_register(request):
    #TODO When a new user created must take the profile user_type
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == "GET":
        return redirect('home')

    elif request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password != repassword:
            messages.add_message(request, messages.ERROR, 'Passwords are not same!')
            return redirect('home')
        elif User.objects.filter(username=username).exists():
            messages.add_message(request, messages.ERROR, 'Username invalid!')
            return redirect('home')
        elif User.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR, 'Email invalid!')
            return redirect('home')
        else:
            user = User.objects.create_user(username=username, 
                                            email=email,
                                            first_name=firstname,
                                            last_name=lastname,
                                            password=password)
            user.save()

            messages.add_message(request, messages.SUCCESS, 'Account created you can, Sing in!')
            return redirect("login")

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.add_message(request, messages.INFO, 'Password or Username invalid!')
            return redirect('home')
    else:
        return redirect('home')


@login_required
def user_logout(request):
    logout(request)
    return redirect('home')


def dashboard(request, username):
    current_user = request.user
    if get_object_or_404(User, username=str(username)) == current_user:
        pass
    else:
        pass