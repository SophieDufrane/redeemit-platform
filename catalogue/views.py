from django.shortcuts import render, get_object_or_404, redirect
from .models import CatalogueItem, Cart, CartItem

def catalogue_home(request):
    catalogue_items = CatalogueItem.objects.all()
    return render(request, 'catalogue/catalogue.html', {'catalogue_items': catalogue_items})

def catalogue_detail(request, slug):
    selected_item = get_object_or_404(CatalogueItem, slug=slug)  # Fetch item by slug
    return render(request, 'catalogue/catalogue_detail.html', {'selected_item': selected_item})

def cart_page(request):
    """
    Displays the user's cart and total points cost.

    **Context**

    - `cart_items`: List of items in the user's cart.
    - `total_points_cost`: Total points cost for all items in the cart.

    **Template**

    - catalogue/cart.html

    """
    cart = Cart.objects.filter(user=request.user).first() # Get cart for the current user (Returns the first object matched by the queryset, or None))
    cart_items = cart.cartitem_set.all() if cart else [] # Fetch cart items if exists, else an empty cart
    total_points_cost = sum(item.item.points_cost * item.quantity for item in cart_items)

    return render(request, 'catalogue/cart.html', {
        'cart_items': cart_items,
        'total_points_cost': total_points_cost
        })

def add_to_cart(request, slug):
    """
    Adds an item to the cart for the current session or user.

    **Context**

    - `item_id`: ID of the CatalogueItem to add to the cart.

    **Flow**

    - Fetch the item to add using the slug.
    - Retrieve or create the cart.
    - Add the item to the cart OR increase the quantity if it already exists.
    - Redirect to the catalogue_detail page.
    """
    item = get_object_or_404(CatalogueItem, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('catalogue_detail', slug=item.slug)
