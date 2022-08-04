from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/',views.user_logout , name='logout'),
    path('register/', views.user_register, name='register'),
    path('<str:username>/profile', views.user_profile, name="profile"),
    path('my-dashboard/', views.user_dashboard, name="my-dashboard"),
    path('my-dashboard/<str:username>/posts', views.user_dashboard_posts, name="my-posts"),
    path('my-dashboard/<str:username>/drafts', views.user_dashboard_drafts, name="my-drafts"),
    path('my-dashboard/<str:username>/<slug:post_slug>', views.post_detail_dashboard, name="post_detail_dashboard"),
]
