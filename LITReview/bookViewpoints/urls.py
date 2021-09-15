from django.urls import path

from . import views

# urls permettant d'accéder au flux (flow),
# à la liste des abonnements (followers),
# à la liste des posts de l'utilisateur (user_posts),
# à la création d'une critique sur un nouveau livre (new_review),
# à la création d'une critique en réponse à un ticket (ticket_answer),
# et à la création d'un ticket (new_ticket)
urlpatterns = [
path('flow/', views.even_flow, name='flow'),
path('followers/', views.subscriptions, name='followers'),
path('user_posts/', views.posts_list, name='user_posts'),
path('new_review/', views.create_review, name='new_review'),
path('ticket_answer/', views.ticket_to_review, name='ticket_answer'),
path('new_ticket/', views.create_ticket, name='new_ticket'),
]
