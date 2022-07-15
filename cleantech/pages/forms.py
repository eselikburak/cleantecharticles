from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Name',
        'data-sb-validations': 'required'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Email',
        'data-sb-validations':'required, email'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Your Message',
        'style': 'height: 10rem;',
        'data-sb-validations': 'required'
    }))

    class Meta:
        model = Contact
        fields =  ['name', 'email', 'message']