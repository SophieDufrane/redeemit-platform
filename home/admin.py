from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin panel customisation for UserProfile.
    """
    list_display = (
        'user',
        'first_name',
        'last_name',
        'user_email',
        'role',
        'point_balance',
        'join_date'
    )
    fields = (
        'user',
        'role',
        'point_balance'
    )
    search_fields = (
        'user__username',
        'user__email',
        'user__first_name',
        'user__last_name'
    )
    list_filter = ('role', 'join_date',)
    readonly_fields = ('join_date',)

    @admin.display(description="First Name")
    def first_name(self, obj):
        return obj.user.first_name

    @admin.display(description="Last Name")
    def last_name(self, obj):
        return obj.user.last_name

    @admin.display(description="Email")
    def user_email(self, obj):
        return obj.user.email
