from django.urls import path
from .views import catalogue_home, catalogue_detail, cart_page, add_to_cart, update_cart_quantity, delete_cart_item

urlpatterns = [
    path('', catalogue_home, name='catalogue_home'),
    path('cart/', cart_page, name='cart_page'),
    path('<slug:slug>/', catalogue_detail, name='catalogue_detail'),
    path('<slug:slug>/add-to-cart/', add_to_cart, name='add_to_cart'),
    path(
        '<slug:slug>/update-quantity/',
        update_cart_quantity,
        name='update_cart_quantity'
        ),
    path(
        '<slug:slug>/delete/',
        delete_cart_item,
        name='delete_cart_item'
        ),
]