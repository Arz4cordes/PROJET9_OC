from django.urls import path

from . import views

# urls pour la page d'accueil home_page qui permet de se connecter,
# la page subscribe avec le formulaire d'inscription,
# et le chemin vers l'application bookViewpoints avec les différentes autres vues
urlpatterns = [
path('subscribe/', views.subscribe_page, name='subscribe'),
path('home_page/', views.home_page, name='home_page'),
path('connection/', views.bookViewpoints_pages, name='to_bookViewpoints'),
]
