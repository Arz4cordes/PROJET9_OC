from django.shortcuts import render
# from subscribers.forms import ConnectionForm
# Create your views here.

def home_page(request):
    return render(request, 'subscribers/home_page.html')

#    if request.method == "GET":
#        form = ConnectionForm()
#        return render(request, 'subscribers/home_page.html', locals())
#    else:
#        form = "Pas de formulaire"
#        return render(request, 'subscribers/home_page.html', {'form': form})

def subscribe_page(request):
    return render(request, 'subscribers/subscribe.html')

def bookViewpoints_pages(request):
    return render(request, 'bookViewpoints/flow.html')
