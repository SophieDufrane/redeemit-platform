from django.contrib import admin
from .models import CatalogueItem, Redemption, RedemptionItem


@admin.register(CatalogueItem)
class CatalogueItemAdmin(admin.ModelAdmin):
    """
    Admin configuration for rewards catalogue.
    Displays name, points cost, stock and reward value.
    """
    list_display = (
        'reward_name',
        'points_cost',
        'stock_quantity',
        'reward_value',
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
        'reward_terms_and_conditions',
        )
    prepopulated_fields = {'slug': ('reward_name',)}
    search_fields = ('reward_name',)


class RedemptionItemInline(admin.TabularInline):
    """
    Inline model to display Redemption Items inside the Redemption admin page.
    """
    model = RedemptionItem
    extra = 0


@admin.register(Redemption)
class RedemptionAdmin(admin.ModelAdmin):
    """
    Admin configuration for Redemption.
    Displays user, points, and date in the list view.
    Shows related RedemptionItems in the detailed view.
    """
    list_display = ('id', 'user', 'redeemed_on', 'total_points_spent',)
    inlines = [RedemptionItemInline]
    ordering = ('-redeemed_on',)
    search_fields = ('user__username',)
