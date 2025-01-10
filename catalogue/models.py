from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class CatalogueItem(models.Model):
    reward_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    points_cost = models.PositiveIntegerField(default=0)
    description = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    stock_quantity = models.IntegerField(default=0)
    reward_value = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    reward_Terms_And_Conditions = models.TextField(default='Terms & Conditions')

    def __str__(self):
         return self.reward_name

