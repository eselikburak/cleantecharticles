
from django import forms
from .models import Post
from ckeditor.fields import RichTextFormField

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.widgets.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Post Title',
    }))
    content = RichTextFormField()
    
    image = forms.ImageField(widget=forms.widgets.ClearableFileInput(attrs={
        'class':'form-control',
    }))
    is_available = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input',
    }), required=False)

    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'is_available', 'categories']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['categories'].widget.attrs.update({'class': 'form-select'})