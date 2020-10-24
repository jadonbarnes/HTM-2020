from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import Blog_post


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

def delete(request,post_id = None):
    object = Blog_post.objects.get(id=post_id)
    object.delete()
    return redirect('profile')