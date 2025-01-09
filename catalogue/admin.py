from django.contrib import admin
from .models import CatalogueItem

@admin.register(CatalogueItem)
class CatalogueItemAdmin(admin.ModelAdmin):

    list_display = ('reward_name', 'points_cost', 'stock_quantity', 'reward_Terms_And_Conditions')
    search_fields = ['reward_name',]
    list_filter = ('points_cost',)

# Register your models here.
