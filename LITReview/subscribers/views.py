from django.shortcuts import render, redirect
from subscribers.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login


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
