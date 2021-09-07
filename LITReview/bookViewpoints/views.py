from django.shortcuts import render

# Create your views here.

def even_flow(request):
    return render(request, 'bookViewpoints/flow.html')