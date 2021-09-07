from django.urls import path

from . import views

urlpatterns = [
path('Accueil/', views.home_page, name='Accueil'),
path('Inscription/', views.subscribe_page, name='Inscription'),
]
