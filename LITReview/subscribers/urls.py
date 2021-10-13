from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# urls pour la page d'accueil home_page qui permet de se connecter,
# la page subscribe avec le formulaire d'inscription,
# et le chemin vers l'application bookViewpoints avec les différentes autres vues
app_name = 'subscribers'


# créer sa propre vue connection avec la condition is_authenticate
urlpatterns = [
    path('', views.connexion, name='accueil'),
    path('login/', views.connexion, name='login'),
    path('subscribe/', views.subscription, name='subscribe'),
    path('logout/', auth_views.LogoutView.as_view(template_name='subscribers/logout.html'), name='logout'),
    path('followers/', views.subscriptions, name='followers'),
    path('delete_follow_to_confirm/<int:follow_id>/', views.confirm_delete_follow, name='delete_follow_to_confirm'),
    path('delete_follow/<int:follow_id>/', views.del_follow, name='delete_follow'),
    path('add_new_follow/', views.add_follow, name='add_new_follow'),
]
