from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    """
    Extends the default User model with additional fields for user data.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='userprofile',
        help_text="The associated user account."
        )
    point_balance = models.IntegerField(
        default=0,
        help_text="The number of points the user currently has for redemption."
        )
    join_date = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time when the user joined the platform."
        )

    @property
    def user_first_letter(self):
        first_name = self.user.first_name or ""
        last_name = self.user.last_name or ""
        return f"{first_name[:1]}.{last_name[:1]}.".upper()

    def __str__(self):
         return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal to create a UserProfile instance whenever a new User is created.
    """
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal to save the UserProfile instance whenever the user is saved.
    """
    instance.userprofile.save()