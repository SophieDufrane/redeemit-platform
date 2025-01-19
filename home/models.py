from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """
    Extends the default User model with additional fields.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    point_balance = models.IntegerField(default=0)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.user.username