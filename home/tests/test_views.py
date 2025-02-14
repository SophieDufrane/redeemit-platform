from django.test import TestCase
from django.urls import reverse

class HomeViewsTests(TestCase):
    def test_homepage_uses_correct_template(self):
        """Test if the home page uses the correct template"""
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')
