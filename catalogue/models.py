from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class CatalogueItem(models.Model):
    """
    An item available for redemption in the catalogue.
    """
    reward_name = models.CharField(
        max_length=100, 
        unique=True
        )
    slug = models.SlugField(
        max_length=200, 
        unique=True, 
        blank=True
        )
    points_cost = models.PositiveIntegerField(default=0)
    description = models.TextField()
    image = CloudinaryField(
        'image',
        default='placeholder'
        )
    image_description = models.CharField(
        max_length=255,
        default='Image description not provided',
        help_text="Provide image description for accessibility purposes."
    )
    stock_quantity = models.IntegerField(default=0)
    reward_value = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0
        )
    reward_terms_and_conditions = models.TextField(
        default='Terms & Conditions'
        )

    def resized_image_url(self, width=400):
        return self.image.url.replace(
            '/upload/', 
            f'/upload/w_{width},q_auto/'
            )

    def __str__(self):
         return self.reward_name


class Cart(models.Model):
    """
    A shopping cart for a user (supports anonymous users for now).
    """
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    # null and blank to be changed once user authentification will be in place.
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True
        )

    def __str__(self):
         return f"Cart {self.id}"


class CartItem(models.Model):
    """
    An item added to a shopping cart.
    """
    cart = models.ForeignKey(
        Cart, 
        on_delete=models.CASCADE
        )
    item = models.ForeignKey(
        CatalogueItem, 
        on_delete=models.CASCADE
        )
    quantity = models.PositiveIntegerField(default=1)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item.reward_name} (x{self.quantity})"
