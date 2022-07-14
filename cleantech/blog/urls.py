from django.urls import path
from . import views

urlpatterns = [
    path('all-blogs/', views.blog, name='allblogs'),
    path('category/<slug:category_slug>/', views.blog_as_category, name='blog_as_category'),
    path('post/<slug:post_slug>', views.blog_detail, name='blog_detail'),
]
