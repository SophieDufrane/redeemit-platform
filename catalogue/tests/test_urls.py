from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class CatalogueTests(TestCase):
    def setUp(self):
        """Create a test user"""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_catalogue_home_url_logged_in(self):
        """Test if catalogue home loads successfully when logged in"""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('catalogue_home'))
        self.assertEqual(response.status_code, 200)
