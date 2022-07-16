from django.shortcuts import render
from .models import Post, Category
from django.contrib.auth.decorators import login_required

def blog(request):
    posts = Post.objects.all().order_by('-created_date')
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'categories': categories,
        'latest_posts': posts[0:3]
    }
    return render(request, 'blog/blog.html', context)

def blog_as_category(request, category_slug):
    posts = Post.objects.filter(categories__slug=category_slug)
    categories = Category.objects.all()
    all_posts = Post.objects.all().order_by('-created_date')
    context = {
        'posts': posts,
        'categories': categories,
        'latest_posts': all_posts[0:3] #use filter 
    }
    return render(request, 'blog/blog.html', context)

def post_detail(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    context = {
        'post': post,
        'the_post_categories': post.categories.all()
    }
    return render(request, 'blog/post_detail.html', context)


@login_required
def post_update(request, pk):
    post = Post.objects.get(pk=pk)
    categories = Category.objects.all()
    context = {
        'post': post,
        'categories': categories
    }
    return render(request, 'blog/post_update.html', context)