from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Home
from accounts.models import Profile
from django.views.generic import FormView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import ContactForm

def home(request):
    num_of_authors = Profile.objects.filter(user_type='blog_author').count()
    num_of_authors += Profile.objects.filter(user_type='tutorial_author').count()
    context = {
        'home_content': Home.objects.all()[0],
        'num_of_authors': num_of_authors,
    }
    return render(request, 'pages/home.html', context)


def about(request):
    context = {
        'home_content': Home.objects.all()[0]
    }
    return render(request, 'pages/about.html', context)


class ContactView(SuccessMessageMixin, FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = 'We Received Your Request'

    #TODO if user is auth get him/her infos

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# def contact(request):
#     return render(request, 'pages/contact.html')<