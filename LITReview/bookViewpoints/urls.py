from django.urls import path

from . import views

app_name = 'bookViewpoints'
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
path('ticket_answer/<int:ticket_id>/', views.ticket_to_review, name='ticket_answer'),
path('new_ticket/', views.create_ticket, name='new_ticket'),
path('update_ticket/<int:ticket_id>/', views.modify_ticket, name='update_ticket'),
path('update_review/<int:review_id>/<int:ticket_id>/', views.modify_review, name='update_review'),
path('delete_ticket_to_confirm/<int:ticket_id>/', views.confirm_delete_ticket, name='delete_ticket_to_confirm'),
path('delete_review_to_confirm/<int:review_id>/', views.confirm_delete_review, name='delete_review_to_confirm'),
path('delete_ticket/<int:ticket_id>/', views.del_ticket, name='delete_ticket'),
path('delete_review/<int:review_id>/', views.del_review, name='delete_review'),
path('delete_follow_to_confirm/<int:follow_id>/', views.confirm_delete_follow, name='delete_follow_to_confirm'),
path('delete_follow/<int:follow_id>/', views.del_follow, name='delete_follow'),
path('add_new_follow/', views.add_follow, name='add_new_follow'),
]
