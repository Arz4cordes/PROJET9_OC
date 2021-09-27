from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from bookViewpoints.models import Review, Ticket
from bookViewpoints.forms import ReviewForm, TicketForm
from django.utils import timezone
from operator import itemgetter

def even_flow(request):
    """ récupération des 5 derniers tickets publiés
        et des 5 dernières critiques publiées, puis
        classement des 5 dernières dates dans une liste
        contenant un trinome (date, type de post, id du post),
        :return: chemin vers le template qui affiche
        les 5 derniers posts, ainsi que deux listes
        tickets_list et reviews_list classées par ordre chronologique
        """
    # GERER L'ABSENCE DE TICKETS ou DE REVIEWS CI-DESSOUS
    last_tickets = Ticket.objects.filter(time_created__lte=timezone.now()).order_by('-time_created')[:5]
    last_reviews = Review.objects.filter(time_created__lte=timezone.now()).order_by('-time_created')[:5]
    dates_posts = []
    the_type = 1
    for ticket in last_tickets:
        the_date = str(ticket.time_created)
        identification = ticket.pk
        dates_posts.append([the_date, the_type, identification])
    the_type = 2
    for review in last_reviews:
        the_date = str(review.time_created)
        identification = review.pk
        dates_posts.append([the_date, the_type, identification])
    dates_arranged = sorted(dates_posts, key=itemgetter(0), reverse=True)
    dates_list = dates_arranged[:5]
    tickets_list = []
    reviews_list = []
    i = 0
    j = 0
    for a_date in dates_list:
        if a_date[1] == 1:
            if i < len(last_tickets):
                tickets_list.append(last_tickets[i])
                i += 1
        else:
            if j < len(last_reviews):
                reviews_list.append(last_reviews[j])
                j += 1
    return render(request, 'bookViewpoints/flow.html',
                  {'tickets': tickets_list, 'reviews': reviews_list})

def posts_list(request):
    if request.user.id is not None:
        last_tickets = Ticket.objects.filter(user=request.user)
        last_reviews = Review.objects.filter(user=request.user)
        return render(request, 'bookViewpoints/user_posts.html',
                      {'tickets': last_tickets, 'reviews': last_reviews})
    # récupérer les tickets et reviews de l'utilisateur
    # puis les livres correspondants
    else:
        return render(request, 'bookViewpoints/user_posts.html')


def subscriptions(request):
    # récupérer les followers de l'user et les users que suit l'user
    return render(request, 'bookViewpoints/followers.html')


def create_review(request):
    if request.method == 'POST':
        form_ticket = TicketForm(request.POST)
        form_review = ReviewForm(request.POST)
        if form_ticket.is_valid():
            ticket = form_ticket.save(commit=False)
            ticket.user = request.user
            ticket.save()
            ticket_id = ticket.id
            if form_review.is_valid():
                ticket_created = Ticket.objects.get(pk=ticket_id)
                review = form_review.save(commit=False)
                review.user = request.user
                review.ticket = ticket_created
                review.save()
                ticket.answer = True
                ticket.save()
        return redirect('bookViewpoints:flow')
    else:
        form_ticket = TicketForm()
        form_review = ReviewForm()
        return render(request, 'bookViewpoints/new_review.html', locals())


def ticket_to_review(request, ticket_id):
    if request.method == 'POST':
        formulaire = ReviewForm(request.POST)
        if formulaire.is_valid():
            ticket = Ticket.objects.get(pk=ticket_id)
            review = formulaire.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            ticket.answer = True
            ticket.save()
            return redirect('bookViewpoints:flow')
        else:
            print("Formulaire pour une réponse au ticket: non valide")
            return render(request, 'bookViewpoints/ticket_answer.html', locals())
    else:
        ticket = get_object_or_404(Ticket, pk=ticket_id)
        formulaire = ReviewForm()
        return render(request, 'bookViewpoints/ticket_answer.html',
                      {'formulaire': formulaire, 'ticket': ticket})

def modify_review(request, review_id):
    if request.method == 'POST':
        formulaire = ReviewForm(request.POST)
        if formulaire.is_valid():
            review = formulaire.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('bookViewpoints:flow')
        else:
            print("Formulaire pour modifier une critique: non valide")
    else:
        review_to_update = get_object_or_404(Review, pk=review_id)
        ticket = review_to_update.ticket
        formulaire = ReviewForm(instance=review_to_update)
        return render(request, 'bookViewpoints/update_review.html', locals())

def del_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    return redirect('bookViewpoints:flow')


def create_ticket(request):
    if request.method == 'POST':
        formulaire = TicketForm(request.POST)
        if formulaire.is_valid():
            ticket = formulaire.save(commit=False) #ici le modèle est récupéré en sortie
            ticket.user = request.user
            ticket.save()
            return redirect('bookViewpoints:flow')
        else:
            print("Formulaire pour un nouveau ticket: non valide")
            return render(request, 'bookViewpoints/new_ticket.html', locals())
    else:
        formulaire = TicketForm()
        return render(request, 'bookViewpoints/new_ticket.html', locals())

def modify_ticket(request, ticket_id):
    print("ARRIVEE DANS LA FONCTION MODIFY TICKET")
    if request.method == 'POST':
        formulaire = TicketForm(request.POST)
        if formulaire.is_valid():
            ticket = formulaire.save(commit=False) #ici le modèle est récupéré en sortie
            ticket.user = request.user
            ticket.save()
            return redirect('bookViewpoints:flow')
        else:
            print("Formulaire pour modifier un ticket: non valide")
    else:
        print("TENTATIVE DE RECUPERATION D'OBJET")
        print(ticket_id)
        ticket_to_update = Ticket.objects.get(pk=ticket_id)
        print("OBJET RECUPERE")
        formulaire = TicketForm(instance=ticket_to_update)
        return render(request, 'bookViewpoints/update_ticket.html', locals())

def del_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    ticket.delete()
    return redirect('bookViewpoints:flow')
