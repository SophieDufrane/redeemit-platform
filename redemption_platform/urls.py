from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # Home app: Handles the landing page (home) and general navigation
    path('', include('home.urls')),

    # Accounts: Includes routes for user authentication
    path('accounts/', include('allauth.urls')),

    # Admin: Django's default admin interface
    path('admin/', admin.site.urls),

    # Catalogue: Handles routes related to catalogue
    path('catalogue/', include('catalogue.urls')),
]

handler404 = 'redemption_platform.views.handler404'
handler500 = 'redemption_platform.views.handler500'
