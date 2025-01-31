from django.urls import path
from .views import home

urlpatterns = [
    # Home page: The landing page of the platform
    path('', home, name='home'),
]