# tests/test_models.py

from django.test import TestCase
from django.contrib.auth import get_user_model
from decimal import Decimal
from products.models import Product

User = get_user_model()

class ProductModelTest(TestCase):
    def setUp(self):
        self.seller = User.objects.create_user(
            email='seller@google.com',
            username='seller', 
            password='password', 
            role='seller'
            )
        self.product = Product.objects.create(
            name='Test Product',
            description='This is a test product',
            price=Decimal('10.00'),
            stock_quantity=10,
            seller=self.seller
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.seller, self.seller)
        self.assertEqual(str(self.product), 'Test Product')

    def test_decrease_stock(self):
        self.product.decrease_stock(3)
        self.assertEqual(self.product.stock_quantity, 7)

    def test_decrease_stock_not_enough(self):
        with self.assertRaises(ValueError):
            self.product.decrease_stock(11)

    def test_increase_stock(self):
        self.product.increase_stock(5)
        self.assertEqual(self.product.stock_quantity, 15)

    def test_category_creation(self):
        self.product.category.add('electronics', 'gadgets')
        self.assertEqual(self.product.category.count(), 2)
        self.assertTrue(self.product.category.filter(name='electronics').exists())
        self.assertTrue(self.product.category.filter(name='gadgets').exists())