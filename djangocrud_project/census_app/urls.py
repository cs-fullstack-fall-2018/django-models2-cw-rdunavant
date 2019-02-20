# Create a route table for your application (urls.py)
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
