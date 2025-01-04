from django.shortcuts import render

def catalogue_home(request):
    return render(request, 'catalogue/catalogue.html')

# Create your views here.
