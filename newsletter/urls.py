# Import required libraries to configure urls

from django.urls import path
from . import views

urlpatterns = [
    path('', views.newsletter, name='newsletter')
]