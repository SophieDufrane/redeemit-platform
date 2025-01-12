from django.shortcuts import render, get_object_or_404, redirect
from .models import CatalogueItem

def catalogue_home(request):
    catalogue_items = CatalogueItem.objects.all()
    return render(request, 'catalogue/catalogue.html', {'catalogue_items': catalogue_items})

def catalogue_detail(request, slug):
    selected_item = get_object_or_404(CatalogueItem, slug=slug)  # Fetch item by slug
    return render(request, 'catalogue/catalogue_detail.html', {'selected_item': selected_item})

def cart_page(request):
    cart = request.session.get('cart', [])  # Get the cart from the session (defaults to an empty list)
    items = CatalogueItem.objects.filter(slug__in=cart)  # Fetch items by slug from the database
    return render(request, 'catalogue/cart.html', {'items': items})

def add_to_cart(request, slug):
    cart = request.session.get('cart', [])
    cart.append(slug)
    request.session['cart'] = cart
    return redirect('catalogue_home')