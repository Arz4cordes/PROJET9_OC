from django.shortcuts import render, redirect, get_object_or_404
from subscribers.forms import UserCreationForm, AuthenticationForm, FollowForm
from django.contrib.auth import authenticate, login
from subscribers.models import UserFollows
from django.contrib.auth.decorators import login_required

def subscription(request):
    if request.method == 'POST':
        formulaire = UserCreationForm(request.POST)
        if formulaire.is_valid():
            formulaire.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('bookViewpoints:flow')
            else:
                formulaire = UserCreationForm()
                return render(request, 'subscribers/subscribe.html', locals())
        else:
            print("Formulaire pour créer un compte:non valide")
            return render(request, 'subscribers/subscribe.html', locals())
    else:
        formulaire = UserCreationForm()
    return render(request, 'subscribers/subscribe.html', locals())


def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        the_user = authenticate(request, username=username, password=password)
        if the_user is not None:
            login(request, the_user)
            return redirect('bookViewpoints:flow')
        else:
            print("formulaire non valide")
            return redirect('subscribers:login')
    else:
        form = AuthenticationForm()
        return render(request, 'subscribers/login.html', {'form': form})

@login_required
def subscriptions(request):
    """ récupére les followers de l'user connecté
    et les utilisateurs que suit l'user connecté
    """
    actually_follow = UserFollows.objects.filter(user=request.user)
    my_followers = UserFollows.objects.filter(followed_user=request.user)
    formulaire = FollowForm()
    return render(request, 'subscribers/followers.html', locals())


@login_required
def confirm_delete_follow(request, follow_id):
    """ récupère un utilisateur de la liste que l'user connecté suit
    et renvoie vers une page de confirmation de la suppression
    """
    follower = get_object_or_404(UserFollows, pk=follow_id)
    return render(request, 'subscribers/confirm_delete_follow.html', locals())


@login_required
def del_follow(request, follow_id):
    """ récupère et supprime un utilisateur
    de la liste que l'user connecté suit
    """
    follower = get_object_or_404(UserFollows, pk=follow_id)
    follower.delete()
    return redirect('subscribers:followers')


@login_required
def add_follow(request):
    """ traite un formulaire d'ajout d'un abonné """
    if request.method == 'POST':
        formulaire = FollowForm(request.POST)
        if formulaire.is_valid():
            user_follow = formulaire.save(commit=False)
            user_follow.user = request.user
            user_follow.save()
            return redirect('subscribers:followers')
        else:
            print("Formulaire pour un nouvel abonnement: non valide")
            return render(request, 'subscribers/followers.html', locals())
