from django.urls import path
from . import views

urlpatterns = [
    path('all-posts/', views.blog, name='allposts'),
    path('category/<slug:category_slug>/', views.blog_as_category, name='blog_as_category'),
    path('post/<slug:post_slug>', views.post_detail, name='post_detail'),
    path('post/update/<int:pk>/', views.post_update, name='post_update'),
]
