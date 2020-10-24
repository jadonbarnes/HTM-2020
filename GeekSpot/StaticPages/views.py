from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import sys
sys.path.insert(1, 'GeekSpot/Blog')
from Blog.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    template = loader.get_template('StaticPages/index.html')
    post_list = Blog_post.objects.order_by('-pub_date')
    context = {
        'post_list': post_list,
    }
    return HttpResponse(template.render(context,request))

@login_required
def profile(request):
    template = loader.get_template('StaticPages/profile.html')
    post_list = Blog_post.objects.filter(author = request.user)
    user = request.user
    context = {
        'post_list': post_list,
        'user':user,
    }
    return HttpResponse(template.render(context,request))

def about(request):
    template = loader.get_template('StaticPages/about.html')
    context = {}
    return HttpResponse(template.render(context,request))