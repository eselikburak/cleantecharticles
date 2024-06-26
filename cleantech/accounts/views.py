from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import LoginForm, RegisterForm
from blog.models import Post
from .models import Profile



def user_register(request):

    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            # When a new user created assign the user_type to the new user.
            user = User.objects.get(username=username)
            Profile.objects.create(user=user)
            messages.success(request, 'Account has been created, You can LOGIN')
            return redirect('login')
    
    else:
        form = RegisterForm()

    context = {
        'form': form
    }

    return render(request, 'accounts/register.html', context)


def user_login(request):

    if request.user.is_authenticated:
        messages.info(request, 'You already login!')
        #TODO show this message on the screen!
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request.POST)

        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data['remember_me']
            user = authenticate(request, username=username, password=password)
            if not remember_me:
                request.session.set_expiry(0)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.info(request, 'Disabled Account')
                    #TODO this message not showing if a user is not active.

            else:
                messages.info(request, 'Username or password is invalid!')

    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form':form})

    


@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def user_dashboard(request):
    current_user = request.user
    return redirect("my-posts", username=current_user.username)


@login_required(login_url='login')
def user_dashboard_posts(request, username):
    if Profile.objects.get(user=request.user).user_type == 'blog_author':

        if request.user.username == username:
            username = str(username) #TODO Add more security if necessary
            posts = Post.objects.filter(author__username=username, is_available=True).order_by('-published_date')
            if posts:
                context = {
                    'posts': posts
                }
                return render(request, 'accounts/dashboard_posts.html', context)
            else:
                context = {
                    'posts': posts
                }
                messages.info(request, "You don't have any post!")
                return render(request, 'accounts/dashboard_posts.html', context)
        else:
            return redirect('home')
    else:
        messages.info(request, "You are not an author!")
        return redirect('allposts')


@login_required(login_url='login')
def user_dashboard_drafts(request, username):
    if Profile.objects.get(user=request.user).user_type == 'blog_author':
        if request.user.username == username:
            username = str(username) #TODO Add more security if necessary
            posts = Post.objects.filter(author__username=username, is_available=False).order_by('-published_date')
            if posts:
                context = {
                    'posts': posts
                }
                return render(request, 'accounts/dashboard_posts.html', context)
            else:
                # Add message
                return redirect('my-dashboard')
        else:
            return redirect('my-dashboard')
    else:
        messages.info(request, "You are not an author!")
        return redirect('allposts')

@login_required(login_url='login')
def post_detail_dashboard(request, username, post_slug):
    if request.user.username == username:
        post = get_object_or_404(Post, author__username=str(username), slug=post_slug)
        context = {
            'post': post
        }
        return render(request, 'accounts/post_detail.html', context)
    else:
        return redirect('my-dashboard')
    
@login_required
def user_profile(request, username):
    current_user = request.user
    if isinstance(username, str):
        user = get_object_or_404(User, username=username)
        if user.id == current_user.id: # if this statement is true user looking own profile page.
            return render(request, 'accounts/profile.html')
        else:
            messages.info(request, "Sorry, you can not see the other user profiles!")
            return redirect('allposts')
    else:
        messages.info(request, "Wrong Request!")
        return redirect('home')