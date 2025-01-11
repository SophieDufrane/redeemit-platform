from django.shortcuts import render, get_object_or_404
from .models import CatalogueItem

def catalogue_home(request):
    catalogue_items = CatalogueItem.objects.all()
    return render(request, 'catalogue/catalogue.html', {'catalogue_items': catalogue_items})

def catalogue_detail(request, slug):
    selected_item = get_object_or_404(CatalogueItem, slug=slug)  # Fetch item by slug
    return render(request, 'catalogue/catalogue_detail.html', {'selected_item': selected_item})

def cart_page(request):
    cart = []  # Placeholder for the cart
    return render(request, 'catalogue/cart.html', {'cart': cart})