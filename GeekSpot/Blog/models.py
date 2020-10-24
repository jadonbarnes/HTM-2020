from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog_post(models.Model):
    name = models.CharField(max_length = 200)
    pub_date = models.DateTimeField(auto_now=True)
    content = models.TextField(default='')
    image = models.ImageField(upload_to='images',default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
