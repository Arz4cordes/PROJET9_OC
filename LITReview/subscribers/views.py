from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, 'subscribers/home_page.html')

def subscribe_page(request):
    return render(request, 'subscribers/subscribe.html')
