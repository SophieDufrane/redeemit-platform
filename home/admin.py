from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'first_name',
        'last_name',
        'email',
        'point_balance',
        'join_date'
    )
    fields = (
        'user',
        'first_name', 
        'last_name', 
        'email',
        'point_balance',
        'join_date',
    )
    readonly_fields = ('join_date',)
    search_fields = (
        'user__username',
        'email',
        'first_name',
        'last_name'
    )
    list_filter = ('join_date',)
