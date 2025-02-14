from django.test import TestCase
from django.urls import reverse


class HomeTests(TestCase):
    def test_homepage(self):
        """Test if home page loads successfully"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
