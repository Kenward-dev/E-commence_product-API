from django.test import TestCase
from django.contrib.auth import get_user_model
from products.models import Product
from products.serializers import ProductSerializer
from decimal import Decimal

User = get_user_model()

class ProductSerializerTest(TestCase):
    def setUp(self):
        self.seller = User.objects.create_user(
            email='seller@google.com',
            username='seller', 
            password='password', 
            role='seller'
            )
        self.product_data = {
            'name': 'Test Product',
            'description': 'This is a test product',
            'price': '10.00',
            'stock_quantity': 10,
            'category': ['electronics', 'gadgets']
        }

    def test_serializer_with_valid_data(self):
        serializer = ProductSerializer(data=self.product_data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_with_invalid_stock_quantity(self):
        self.product_data['stock_quantity'] = -1
        serializer = ProductSerializer(data=self.product_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('stock_quantity', serializer.errors)

    def test_create_product_with_categories(self):
        serializer = ProductSerializer(data=self.product_data)
        self.assertTrue(serializer.is_valid())
        product = serializer.save(seller=self.seller)
        self.assertEqual(product.category.count(), 2)
        self.assertTrue(product.category.filter(name='electronics').exists())
        self.assertTrue(product.category.filter(name='gadgets').exists())

    def test_formatted_price(self):
        product = Product.objects.create(
            name='Test Product',
            description='This is a test product',
            price=Decimal('10.00'),
            stock_quantity=10,
            seller=self.seller
        )
        serializer = ProductSerializer(product)
        self.assertEqual(serializer.data['formatted_price'], '$10.00')