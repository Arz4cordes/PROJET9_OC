from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# urls pour la page d'accueil home_page qui permet de se connecter,
# la page subscribe avec le formulaire d'inscription,
# et le chemin vers l'application bookViewpoints avec les différentes autres vues
app_name = 'subscribers'


# créer sa propre vue connection avec la condition is_authenticate
urlpatterns = [
    path('login/', views.connexion, name='login'),
    path('subscribe/', views.subscription, name='subscribe'),
    path('logout/', auth_views.LogoutView.as_view(template_name='subscribers/logout.html'), name='logout'),
]
