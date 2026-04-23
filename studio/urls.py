from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('studios/', views.studios, name='studios'),
    path('equipment/', views.equipment, name='equipment'),
    path('services/', views.services, name='services'),
]