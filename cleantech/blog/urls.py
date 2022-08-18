from django.urls import path
from . import views

urlpatterns = [
    path('all-posts/', views.blog, name='allposts'),
    path('post/post-new', views.post_new, name="post_new"),
    path('category/<slug:category_slug>/', views.blog_as_category, name='blog_as_category'),
    path('post/<slug:post_slug>', views.post_detail, name='post_detail'),
    path('post/update/<int:pk>/', views.post_update, name='post_update'),
    path('post/delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('search/', views.SearchView.as_view(), name="search"),
]
