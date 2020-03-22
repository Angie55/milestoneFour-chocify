from django.test import TestCase
from .models import Product


class ProductTests(TestCase):
    """
    This test runs against the Product model
    """

    def test_str(self):
        test_title = Product(title='Product title')
        self.assertEqual(str(test_title), 'Product title')
