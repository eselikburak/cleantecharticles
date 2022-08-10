from django.urls import path
from . import views

urlpatterns = [
    path('<str:tutorial_name>', views.tutorial, name='tutorial'),
]
