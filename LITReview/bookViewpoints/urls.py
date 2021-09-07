from django.urls import path

from . import views

urlpatterns = [
path('flux/', views.even_flow, name='flux'),
]
