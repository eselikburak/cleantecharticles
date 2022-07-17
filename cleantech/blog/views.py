from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Post, Category
from django.contrib.auth.decorators import login_required

def blog(request):
    posts = Post.objects.filter(is_available=True).order_by('-created_date')
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'categories': categories,
        'latest_posts': posts[0:3]
    }
    return render(request, 'blog/blog.html', context)

def blog_as_category(request, category_slug):
    posts = Post.objects.filter(is_available=True, categories__slug=category_slug)
    categories = Category.objects.all()
    all_posts = Post.objects.all().order_by('-created_date')
    context = {
        'posts': posts,
        'categories': categories,
        'latest_posts': all_posts[0:3] #use filter 
    }
    return render(request, 'blog/blog.html', context)

def post_detail(request, post_slug):
    post = get_object_or_404(Post, is_available=True, slug=post_slug)
    context = {
        'post': post,
        'the_post_categories': post.categories.all()
    }
    return render(request, 'blog/post_detail.html', context)


@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)

        # if form.has_changed():
        #     print('Some changes has occourd!')

        if form.is_valid():
            
            post = form.save(commit=False)
            post.author = request.user
            post.categories.set(form.cleaned_data['categories'])
            post.publish()

            # if author make deactivate the post 
            if post.is_available == False:
                return redirect('allposts')
            else:
                return redirect('post_detail', post_slug=post.slug)
    #categories = Category.objects.all()
    else: 
        form = PostForm(instance=post)
    context = {
        'form': form,
    }
    return render(request, 'blog/post_update.html', context)