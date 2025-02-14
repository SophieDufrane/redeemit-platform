from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class HomeViewsTests(TestCase):
    def setUp(self):
        """Create a test user"""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_homepage_uses_correct_template(self):
        """Test if the home page uses the correct template"""
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    def test_homepage_logged_out(self):
        """
        Test if home page shows login and register buttons when logged out
        """
        response = self.client.get(reverse('home'))
        # Ensure Register button appears
        self.assertContains(response, 'Register')
        # Ensure Log In button appears
        self.assertContains(response, 'Log In')

    def test_homepage_logged_in(self):
        """Test if home page shows catalogue access when logged in"""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('home'))
        # Check Welcome message appears
        self.assertContains(response, 'Welcome Back')
        # Check Go to Catalogue button appears
        self.assertContains(response, "GO")
