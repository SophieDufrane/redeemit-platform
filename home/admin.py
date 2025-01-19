from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user', 
        'get_first_name',
        'get_last_name', 
        'get_email', 
        'point_balance', 
        'join_date'
    )
    fields = (
        'user', 
        'point_balance', 
        'join_date',
    )
    readonly_fields = ('join_date',)
    search_fields = (
        'user__username', 
        'user__email', 
        'user__first_name', 
        'user__last_name'
    )
    list_filter = ('join_date',)

    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = 'First Name'

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = 'Last Name'

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'
