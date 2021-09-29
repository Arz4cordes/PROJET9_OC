from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from bookViewpoints.models import Review, Ticket
from subscribers.models import UserFollows
from bookViewpoints.forms import ReviewForm, TicketForm, FollowForm
from django.utils import timezone
from operator import itemgetter
from django.contrib.auth.decorators import login_required

@login_required
def even_flow(request):
    """ récupération des 5 derniers tickets publiés
    et des 5 dernières critiques publiées, puis
    classement des 5 dernières dates dans une liste
    contenant un trinome (date, type de post, id du post),
    :return: chemin vers le template qui affiche
    les 5 derniers posts, et envoie deux listes
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

@login_required
def posts_list(request):
    """ récupère les tickets et les critiques de l'utilisateur connecté
    :return: renvoie vers le template affichant les posts de l'utilisateur,
    et envoie les deux listes last_tickets et last_reviews à afficher
    classées par ordre chronologique
    """
    if request.user.id is not None:
        last_tickets = Ticket.objects.filter(user=request.user).order_by('-time_created')
        last_reviews = Review.objects.filter(user=request.user).order_by('-time_created')
        return render(request, 'bookViewpoints/user_posts.html',
                      {'tickets': last_tickets, 'reviews': last_reviews})
    # récupérer les tickets et reviews de l'utilisateur
    # puis les livres correspondants
    else:
        return render(request, 'bookViewpoints/user_posts.html')

@login_required
def subscriptions(request):
    # récupérer les followers de l'user et les users que suit l'user
    actually_follow = UserFollows.objects.filter(user=request.user)
    my_followers = UserFollows.objects.filter(followed_user=request.user)
    formulaire = FollowForm()
    return render(request, 'bookViewpoints/followers.html', locals())

@login_required
def confirm_delete_follow(request, follow_id):
    follower = get_object_or_404(UserFollows, pk=follow_id)
    return render(request, 'bookViewpoints/confirm_delete_follow.html', locals())

@login_required
def del_follow(request, follow_id):
    follower = get_object_or_404(UserFollows, pk=follow_id)
    follower.delete()
    return redirect('bookViewpoints:followers')

@login_required
def add_follow(request):
    if request.method == 'POST':
        formulaire = FollowForm(request.POST)
        if formulaire.is_valid():
            user_follow = formulaire.save(commit=False)
            user_follow.user = request.user
            user_follow.save()
            return redirect('bookViewpoints:followers')
        else:
            print("Formulaire pour un nouvel abonnement: non valide")
            return render(request, 'bookViewpoints/followers.html', locals())

@login_required
def create_ticket(request):
    """ Crée une instance de formulaire Ticket,
    puis chemin vers le template affichant le formulaire de création d'un ticket
    ou bien, en cas de requète POST:
    récupère l'objet Ticket, ajoute son attribut user et enregistre dans la BDD le ticket
    """
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

@login_required
def modify_ticket(request, ticket_id):
    """ Crée une instance du formulaire Ticket,
    puis chemin vers le template affichant le formulaire,
    en envoyant les données existantes du ticket à modifier,
    ou bien, en cas de requète POST:
    récupère l'objet Ticket à modifier, ajoute son attribut user,
    puis enregistre la MAJ de l'objet Ticket dans la BDD
    (l'instance du formulaire est liée à l'objet ticket_to_update existant)
    """
    ticket_to_update = Ticket.objects.get(pk=ticket_id)
    if request.method == 'POST':
        formulaire = TicketForm(request.POST, instance=ticket_to_update)
        if formulaire.is_valid():
            ticket = formulaire.save(commit=False) #ici le modèle est récupéré en sortie
            ticket.user = request.user
            ticket.save()
            return redirect('bookViewpoints:flow')
        else:
            print("Formulaire pour modifier un ticket: non valide")
    else:
        formulaire = TicketForm(instance=ticket_to_update)
        return render(request, 'bookViewpoints/update_ticket.html', locals())

@login_required
def confirm_delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    return render(request, 'bookViewpoints/confirm_delete_ticket.html', locals())

@login_required
def del_ticket(request, ticket_id):
    ticket_to_delete = get_object_or_404(Ticket, pk=ticket_id)
    if ticket_to_delete.answer:
        review = Review.objects.filter(ticket=ticket_to_delete)
        if review is not None:
            review.delete()
    ticket_to_delete.delete()
    return redirect('bookViewpoints:user_posts')

@login_required
def create_review(request):
    """ Crée des instances de formulaires Ticket et Review
    puis chemin vers le template affichant le formulaire de création d'une critique
    ou bien, en cas de requète POST:
    récupère un objet Ticket, ajoute son attribut user, enregistre dans la BDD le ticket,
    puis récupère un objet Review, ajoute son attribut user et son attribut ticket,
    enregistre la critique dans la BDD et met à jour l'attribut answer du ticket
    """
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

@login_required
def ticket_to_review(request, ticket_id):
    """ Récupère l'objet Ticket auquel on veut répondre, crée une instance du formulaire Review,
    puis chemin vers le template affichant le formulaire de création d'une critique
    ou bien, en cas de requète POST:
    récupère l'objet Ticket et l'objet Review correspondant,
    ajoute l'attribut user et l'attribut ticket à l'objet Review,
    enregistre dans la BDD la review et met à jour l'attribut answer du ticket
    """
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

@login_required
def modify_review(request, review_id, ticket_id):
    """ recupère l'objet Ticket auquel l'objet Review est associé,
    crée une instance de formulaire Review,
    puis chemin vers le template affichant le formulaire,
    en envoyant les données existantes de la critique à modifier,
    ou bien, en cas de requète POST:
    récupère l'objet Review à modifier, ajoute son attribut user,
    puis enregistre la MAJ de l'objet Review dans la BDD
    (l'instance du formulaire est liée à l'objet review_to_update existant)
    """
    review_to_update = Review.objects.get(pk=review_id)
    if request.method == 'POST':
        formulaire = ReviewForm(request.POST, instance=review_to_update)
        if formulaire.is_valid():
            ticket = Ticket.objects.get(pk=ticket_id)
            review = formulaire.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('bookViewpoints:flow')
        else:
            print("Formulaire pour modifier une critique: non valide")
    else:
        ticket = review_to_update.ticket
        formulaire = ReviewForm(instance=review_to_update)
        return render(request, 'bookViewpoints/update_review.html', locals())

@login_required
def confirm_delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'bookViewpoints/confirm_delete_review.html', locals())

@login_required
def del_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    ticket = review.ticket
    review.delete()
    ticket.answer = False
    ticket.save(update_fields=['answer'])
    return redirect('bookViewpoints:user_posts')
