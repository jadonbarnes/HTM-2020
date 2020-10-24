from django import forms
from .models import Blog_post

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog_post
        fields = ('name','content','image','author')

