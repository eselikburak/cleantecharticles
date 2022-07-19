from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile


def user_register(request):
    #TODO When a new user created must take the profile user_type #solved
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == "GET":
        return redirect('home')

    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')

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
                                            # TODO password accepting without any validating!
            user.save()

            # Assign profile user_type
            Profile.objects.create(user=user)

            messages.add_message(request, messages.SUCCESS, 'Account created you can, Sing in!')
            return redirect("login")

def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        remember_me = request.POST.get('remember_me')
        if user is not None:
            if user.is_active:
                login(request, user)
                # For if user check the remember_me checkbox
                if not remember_me:
                    request.session.set_expiry(0)
                return redirect('home')
            else:
                #TODO Doesn't seem this message on screen, solve this
                messages.add_message(request, messages.INFO, 'Account is Desibled!')
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