from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from catalogue.models import CatalogueItem, Cart, CartItem
from home.models import UserProfile


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
        response = self.client.get(reverse('catalogue_home'))
        self.assertContains(response, "Test Reward")


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
        response = self.client.get(reverse('cart_page'))
        self.assertContains(response, "Test Reward")
        self.assertContains(response, "2")


class CartActionsFromCatalogueTests(TestCase):
    """
    Tests related to adding and updating items from the catalogue detail page
    """

    def setUp(self):
        """Create a test user, a sample reward and an empty cart"""
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

    def test_add_new_item_from_catalogue_detail_page(self):
        """
        Test if adding an item from the detail page works correctly
        """
        self.client.login(username='testuser', password='testpassword')
        self.assertFalse(
            CartItem.objects.filter(cart=self.cart, item=self.item).exists()
        )
        response = self.client.post(
            reverse('add_to_cart', args=[self.item.slug])
        )

        self.assertTrue(
            CartItem.objects.filter(cart=self.cart, item=self.item).exists()
        )
        cart_item = CartItem.objects.get(cart=self.cart, item=self.item)
        self.assertEqual(
            cart_item.quantity, 1,
            "Expected item to be added with quantity 1."
        )
        self.assertRedirects(
            response, reverse('catalogue_detail', args=[self.item.slug])
        )

    def test_increase_quantity_from_catalogue_detail_page(self):
        """Test if adding an existing item increases its quantity"""
        self.client.login(username='testuser', password='testpassword')
        self.client.post(reverse('add_to_cart', args=[self.item.slug]))
        response = self.client.post(
            reverse('add_to_cart', args=[self.item.slug])
        )

        cart_item = CartItem.objects.get(cart=self.cart, item=self.item)

        self.assertEqual(
            cart_item.quantity, 2,
            "Expected item quantity to increase when added again."
        )
        self.assertRedirects(
            response, reverse('catalogue_detail', args=[self.item.slug])
        )


class CartPageTests(TestCase):
    """Tests related to actions on the cart page itself"""

    def setUp(self):
        """Create a test user, a sample reward and an empty cart"""
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

    def test_increase_quantity_from_cart_page(self):
        """Test if updating quantity from the cart page works correctly"""
        self.client.login(username='testuser', password='testpassword')
        self.client.post(reverse('add_to_cart', args=[self.item.slug]))
        response = self.client.post(
            reverse('update_cart_quantity', args=[self.item.slug]),
            {'quantity': 2}
        )

        cart_item = CartItem.objects.get(cart=self.cart, item=self.item)
        self.assertEqual(cart_item.quantity, 2)
        self.assertRedirects(response, reverse('cart_page'))

    def test_delete_item_from_cart_page(self):
        """Test if deleting an item removes it from the cart"""
        self.client.login(username='testuser', password='testpassword')
        self.client.post(reverse('add_to_cart', args=[self.item.slug]))
        response = self.client.post(
            reverse('delete_cart_item', args=[self.item.slug])
        )

        self.assertFalse(
            CartItem.objects.filter(cart=self.cart, item=self.item).exists()
        )
        self.assertRedirects(response, reverse('cart_page'))


class RedemptionProcessTests(TestCase):
    """
    Tests the redemption process:
    - Deducts points from user balance
    - Reduces stock quantity
    - Clears the cart after successful redemption
    """

    def setUp(self):
        """Create a test user, a sample reward and an empty cart."""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        # Ensure no duplicate UserProfile exists
        UserProfile.objects.filter(user=self.user).delete()
        self.user_profile = UserProfile.objects.create(
            user=self.user,
            point_balance=500
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
            quantity=1
        )

    def test_redemption_deducts_points(self):
        """Ensure points are deducted after redemption"""
        self.client.login(username='testuser', password='testpassword')
        self.client.post(reverse('redeem_cart'))

        self.user_profile.refresh_from_db()

        self.assertEqual(
            self.user_profile.point_balance, 400,
            "Expected point balance to be 400 after redemption."
        )

    def test_redemption_deducts_stock(self):
        """Ensure stock quantity is reduced after redemption"""
        self.client.login(username='testuser', password='testpassword')
        self.client.post(reverse('redeem_cart'))

        self.item.refresh_from_db()

        self.assertEqual(
            self.item.stock_quantity, 4,
            "Expected stock quantity to decrease by 1 after redemption."
        )

    def test_cart_is_cleared_after_redemption(self):
        """Ensure the cart is cleared after a successful redemption"""
        self.client.login(username='testuser', password='testpassword')
        self.client.post(reverse('redeem_cart'))

        self.assertFalse(
            Cart.objects.filter(user=self.user).exists(),
            "Expected the cart to be deleted after redemption."
        )
