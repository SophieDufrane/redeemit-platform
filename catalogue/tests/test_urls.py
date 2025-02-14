from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from catalogue.models import CatalogueItem


class CatalogueTests(TestCase):
    def setUp(self):
        """Create a test user and a sample reward"""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.item = CatalogueItem.objects.create(
            reward_name="Test Reward",
            slug="test-reward",
            points_cost=100
        )

    def test_catalogue_home_url_logged_in(self):
        """Test if catalogue home loads successfully when logged in"""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('catalogue_home'))
        self.assertEqual(
            response.status_code, 200,
            "Expected catalogue home page to load (200 OK) but got a different status code."
        )

    def test_catalogue_detail_url_not_found(self):
        """Test if non-existing reward detail page returns 404"""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('catalogue_detail', args=['non-existent-slug']))
        self.assertEqual(
            response.status_code, 404,
            "Expected 404 Not Found for non-existent reward detail page, but got a different status code."
        )
