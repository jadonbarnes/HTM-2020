from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create, name = 'create'),
    path('delete/<post_id>', views.delete, name='delete')
]