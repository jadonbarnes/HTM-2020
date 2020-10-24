from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import BlogForm

# Create your views here.
def create(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'Blog/create.html', {'form': form, 'img_obj': img_obj})
    else:
        form = BlogForm()
    return render(request, 'Blog/create.html', {'form': form})