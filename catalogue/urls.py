from django.urls import path
from .views import (
    catalogue_home,
    catalogue_detail,
    cart_page,
    add_to_cart,
    update_cart_quantity,
    delete_cart_item,
    redeem_cart
    )

urlpatterns = [
    # Catalogue home: Displays all available rewards
    path('', catalogue_home, name='catalogue_home'),

    # Cart: Displays the user's cart
    path('cart/', cart_page, name='cart_page'),

    # Reward detail: Displays details for a specific reward item
    path('<slug:slug>/', catalogue_detail, name='catalogue_detail'),

    # Add to cart: Adds a specific reward item to the user's cart
    path('<slug:slug>/add-to-cart/', add_to_cart, name='add_to_cart'),

    # Update quantity: Updates the quantity of an item in the cart
    path(
        '<slug:slug>/update-quantity/',
        update_cart_quantity,
        name='update_cart_quantity'
    ),

    # Delete from cart: Deletes a specific reward item from the cart
    path(
        '<slug:slug>/delete/',
        delete_cart_item,
        name='delete_cart_item'
    ),

    # Redeem cart: Processes the cart redemption
    path('cart/redeem/', redeem_cart, name='redeem_cart'),
]
