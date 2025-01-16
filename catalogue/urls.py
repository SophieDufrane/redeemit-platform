from django.urls import path
from .views import catalogue_home, catalogue_detail, cart_page, add_to_cart

urlpatterns = [
    path('', catalogue_home, name='catalogue_home'),
    path('cart/', cart_page, name='cart_page'),
    path('<slug:slug>/', catalogue_detail, name='catalogue_detail'),
    path('<slug:slug>/add-to-cart/', add_to_cart, name='add_to_cart'),
]