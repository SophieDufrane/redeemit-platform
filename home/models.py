from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    """
    Extends the default User model with additional fields.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    point_balance = models.IntegerField(default=0)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()