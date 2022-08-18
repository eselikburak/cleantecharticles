from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Home
from accounts.models import Profile
from django.views.generic import FormView, TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import ContactForm

class HomeView(TemplateView):
    template_name: str = 'pages/home.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        num_of_authors = Profile.objects.filter(user_type='blog_author').count()
        num_of_authors += Profile.objects.filter(user_type='tutorial_author').count()
        context['home_content'] = Home.objects.all()[0]
        context['num_of_authors'] = num_of_authors
        return context


class AboutView(TemplateView):
    template_name: str = 'pages/about.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['home_content'] = Home.objects.all()[0]
        return context


class ContactView(SuccessMessageMixin, FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = 'We received your message.'

    #TODO if user is auth get him/her infos

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
