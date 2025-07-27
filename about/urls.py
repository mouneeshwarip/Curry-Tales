from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_us, name='about'),
    path('edit/', views.edit_about_us, name='edit_about_us'),
    path('contact/', views.contact, name='contact'),
]