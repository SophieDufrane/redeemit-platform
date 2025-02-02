from django.contrib import admin
from .models import CatalogueItem, Redemption

@admin.register(CatalogueItem)
class CatalogueItemAdmin(admin.ModelAdmin):
    list_display = (
        'reward_name',
        'points_cost',
        'stock_quantity',
        'reward_value'
        )
    fields = (
        'reward_name',
        'slug',
        'points_cost',
        'description',
        'image',
        'image_description',
        'stock_quantity',
        'reward_value',
        'reward_terms_and_conditions'
        )
    prepopulated_fields = {'slug': ('reward_name',)}
    search_fields = ('reward_name',)


@admin.register(Redemption)
class RedemptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'redeemed_on', 'total_points_spent')
    ordering = ('-redeemed_on',)
    search_fields = ('user__username',)

