from django.shortcuts import get_object_or_404, render, redirect

from bookViewpoints.models import Review, Ticket
from bookViewpoints.forms import ReviewForm, TicketForm

from django.utils import timezone
from operator import itemgetter
from datetime import *
from django.utils import timezone

def even_flow(request):
    """ récupération des 5 derniers tickets publiés
        et des 5 dernières critiques publiées, puis
        classement des 5 dernières dates dans une liste
        contenant un trinome (date, type de post, id du post),
        :return: chemin vers le template qui affiche
        les 5 derniers posts, ainsi que deux listes
        tickets_list et reviews_list classées par ordre chronologique
        """
    last_tickets = Ticket.objects.filter(time_created__lte=timezone.now()).order_by('-time_created')[:5]
    last_reviews = Review.objects.filter(time_created__lte=timezone.now()).order_by('-time_created')[:5]
    return render(request, 'bookViewpoints/flow.html',
                  {'tickets': last_tickets, 'reviews': last_reviews})

def subscriptions(request):
    # récupérer les followers de l'user et les users que suit l'user
    return render(request, 'bookViewpoints/followers.html')


def posts_list(request):
    if request.user.id is not None:
        last_tickets = get_object_or_404(Ticket, pk=request.user.id)
        last_reviews = get_object_or_404(Review, pk=request.user.id)
        return render(request, 'bookViewpoints/user_posts.html',
                      {'tickets': last_tickets, 'reviews': last_reviews})
    # récupérer les tickets et reviews de l'utilisateur
    # puis les livres correspondants
    else:
        return render(request, 'bookViewpoints/user_posts.html')

def create_review(request):
    formulaire = ReviewForm(request.POST if request.method == 'POST' else None)
    if request.method == 'POST':
        if formulaire.is_valid():
            formulaire.save()
        return redirect('flow')
    else:
        return render(request, 'bookViewpoints/new_review.html', locals())


def ticket_to_review(request):
    # récupérer les objets tickets, review, book
    return render(request, 'bookViewpoints/ticket_answer.html')

def create_ticket(request):
    formulaire = TicketForm(request.POST if request.method == 'POST' else None)
    if request.method == 'POST':
        if formulaire.is_valid():
            formulaire.save()
        return redirect('flow')
    else:
        # récupérer les ticket et book
        return render(request, 'bookViewpoints/new_ticket.html', locals())
