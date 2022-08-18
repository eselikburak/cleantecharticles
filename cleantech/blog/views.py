from django.http import Http404

from django.core.paginator import Paginator

from django.shortcuts import get_object_or_404, redirect, render

from accounts.models import Profile
from django.contrib import messages
from .forms import PostForm
from .models import Post, Category
from django.contrib.auth.decorators import login_required
from django.views.generic import View


def blog(request):
    posts = Post.objects.filter(is_available=True).order_by('-published_date')
    paginator = Paginator(posts, 12)  # show 12 contact per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = Category.objects.all()

    context = {
        'page_obj': page_obj,
        'categories': categories,
    }
    return render(request, 'blog/blog.html', context)


def blog_as_category(request, category_slug):
    posts = Post.objects.filter(
        is_available=True, categories__slug=category_slug).order_by('-published_date')
    paginator = Paginator(posts, 12)  # show 12 contact per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = Category.objects.all()

    context = {
        'page_obj': page_obj,
        'categories': categories,
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
            post.save()

            # if author make deactivate the post
            if post.is_available == False:
                return redirect('my-posts', username=request.user.username)
            else:
                return redirect('post_detail_dashboard', username=request.user.username, post_slug=post.slug)
    #categories = Category.objects.all()
    else:
        form = PostForm(instance=post)
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'blog/post_update.html', context)


def post_new(request):
    if Profile.objects.get(user=request.user).user_type == 'blog_author':
        if request.method == 'POST':
            form = PostForm(request.POST, files=request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                post.categories.set(form.cleaned_data['categories'])
                # This is(categories) adding after saveing beacuse this needs post id!

                if post.is_available == False:
                    return redirect('my-drafts', username=request.user.username)
                else:
                    return redirect('post_detail_dashboard', username=request.user.username, post_slug=post.slug)
        else:
            print('else')
            form = PostForm()
        context = {
            'form': form,
        }
        return render(request, 'blog/post_new.html', context)
    else:
        # TODO add message to the user
        return redirect('allposts')


def post_delete(request, pk):
    current_user = request.user
    post = Post.objects.get(id=pk)
    post_title: str = post.title
    if current_user.id == post.author.id:  # if current user and post author is same person
        post.delete()
        messages.success(
            request, f'\"{post_title.capitalize()}\" has been deleted!')
        return redirect('my-posts', username=current_user.username)
    else:
        messages.warning(
            request, f'{post_title.capitalize()} has not been deleted!')
        return redirect('allposts')

from django.http import JsonResponse
from django.core import serializers


class SearchView(View):

    def get(self, request):
        # Add here more filter to security or search on net !
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            searchbox_text = request.GET.get('searchbox_text')
            if searchbox_text == "" or len(searchbox_text) > 200:
                search_results = False
            else:
                #TODO Do not send all object data just send title and slug field!
                search_results = Post.objects.filter(is_available=True, title__contains=str(searchbox_text))[:20]
            if search_results and search_results.count() >= 1:  
                search_results = serializers.serialize('json', search_results)
            else:
                search_results = False # list(search_results)
            return JsonResponse({'search_results': search_results}, status=200)

        else:
            raise Http404