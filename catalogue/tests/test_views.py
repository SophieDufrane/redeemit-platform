from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from catalogue.models import CatalogueItem, Cart, CartItem


class CatalogueViewsTests(TestCase):
    def setUp(self):
        """Create a test user and a sample reward"""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.item = CatalogueItem.objects.create(
            reward_name="Test Reward",
            slug="test-reward",
            points_cost=100,
            stock_quantity=5
        )

    def test_catalogue_uses_correct_template(self):
        """Test if the catalogue home page uses the correct template"""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('catalogue_home'))
        self.assertEqual(
            response.status_code, 200,
            "Expected catalogue home to return 200 OK "
            "but got a different status."
        )
        self.assertTemplateUsed(response, 'catalogue/catalogue.html')

    def test_catalogue_displays_items(self):
        """Test if catalogue home page displays available rewards"""
        self.client.login(username='testuser', password='testpassword')
        self.item.refresh_from_db()
        response = self.client.get(reverse('catalogue_home'))

        self.assertContains(
            response,
            "Test Reward",
            msg_prefix="Catalogue home does not display "
            "available rewards when it should."
        )

class CartViewsTests(TestCase):
    def setUp(self):
        """Create a test user and a sample reward"""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.item = CatalogueItem.objects.create(
            reward_name="Test Reward",
            slug="test-reward",
            points_cost=100,
            stock_quantity=5
        )

        self.cart = Cart.objects.create(user=self.user)
        self.cart_item = CartItem.objects.create(
            cart=self.cart,
            item=self.item,
            quantity=2
        )
    
    def test_cart_displays_items(self):
        """Test if cart page displays added rewards"""
        self.client.login(username='testuser', password='testpassword')
        self.cart.refresh_from_db()
        self.cart_item.refresh_from_db()
        response = self.client.get(reverse('cart_page'))

        self.assertContains(
            response,
            "Test Reward",
            msg_prefix="Cart page does not display "
            "added rewards when it should."
        )

        self.assertContains(
            response,
            "2",
            msg_prefix="Cart page does not display correct quantity."
        )
