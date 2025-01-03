from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Reward(models.Model):
    reward_name = models.CharField(max_length=100, unique=True)
    points_cost = models.PositiveIntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to=None, height_field=None, width_field=None)
    stock_quantity = models.IntegerField(default=0)
    # admin = models.ForeignKey('User', on_delete=models.CASCADE) # Referencing the built-in User model

    def __str__(self):
         return self.reward_name

