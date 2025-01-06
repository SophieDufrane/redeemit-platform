from django.shortcuts import render
from .models import CatalogueItem

def catalogue_home(request):
    items = CatalogueItem.objects.all()
    return render(request, 'catalogue/catalogue.html', {'items': items})
