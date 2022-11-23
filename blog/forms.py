from django import forms
from .widgets import CustomClearableFileInput
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'image', 'content']

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)
