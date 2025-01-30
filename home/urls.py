from django.urls import path
from .views import home, signup_view

urlpatterns = [
    path('', home, name='home'),
    path('accounts/signup/', signup_view, name='signup_view')
]