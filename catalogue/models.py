from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class CatalogueItem(models.Model):
    """
    Represents an item available for redemption in the catalogue.
    """
    reward_name = models.CharField(
        max_length=100, 
        unique=True,
        help_text="The name of the reward must be unique."
        )
    slug = models.SlugField(
        max_length=200, 
        unique=True, 
        blank=True
        )
    points_cost = models.PositiveIntegerField(
        default=0,
        help_text="The number of points required to redeem this item."
        )
    description = models.TextField(
        help_text="Detailed description of the reward."
    )
    image = CloudinaryField(
        'image',
        default='placeholder',
        help_text="The image of the reward."
        )
    image_description = models.CharField(
        max_length=255,
        default='Image description not provided',
        help_text="Provide an image description for accessibility purposes."
    )
    stock_quantity = models.IntegerField(
        default=0,
        help_text="The current stock quantity of the reward."
        )
    reward_value = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0,
        help_text="The points value of the reward."
        )
    reward_terms_and_conditions = models.TextField(
        default='Terms & Conditions',
        help_text="Terms and conditions for redeeming this reward."
        )

    def resized_image_url(self, width=400):
        """
        Returns the resized image URL with a specified width.
        Defaults to a width of 400 pixels.
        """
        return self.image.url.replace(
            '/upload/', 
            f'/upload/w_{width},q_auto/'
            )

    def __str__(self):
         return self.reward_name


class Cart(models.Model):
    """
    Represents a shopping cart associated with a user.
    """
    created_on = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time when the cart was created."
        )
    updated_on = models.DateTimeField(
        auto_now=True,
        help_text="The date and time when the cart was updated."
        )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        help_text="The user associated with this cart."
        )

    def __str__(self):
         return f"Cart {self.id}"


class CartItem(models.Model):
    """
    Represents an item added to a shopping cart.
    """
    cart = models.ForeignKey(
        Cart, 
        on_delete=models.CASCADE,
        help_text="The cart that this item belongs to."
        )
    item = models.ForeignKey(
        CatalogueItem, 
        on_delete=models.CASCADE,
        help_text="The item that was added to the cart."
        )
    quantity = models.PositiveIntegerField(
        default=1,
        help_text="The quantity of this item in the cart."
        )
    added_on = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time this item was added to the cart."
        )

    def total_points(self):
        """
        Calculates the total points cost for this cart item based on its quantity.
        """
        return self.item.points_cost * self.quantity

    def __str__(self):
        return f"{self.item.reward_name} (x{self.quantity})"
