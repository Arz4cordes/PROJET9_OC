from django.shortcuts import render, redirect
from subscribers.forms import ConnectionForm


def subscription(request):
    # if request.user.is_authenticated:
    #    return redirect('bookViewpoints:flow')
    formulaire = ConnectionForm()
    return render(request, 'subscribers/subscribe.html', locals())

def connected_page(request):
        formulaire = ConnectionForm(request.POST)
        if formulaire.is_valid():
            formulaire.save()
            subscription_done = True
            return render(request, 'subscribers/login.html', locals())
        