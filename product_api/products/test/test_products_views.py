from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from decimal import Decimal
from products.models import Product

User = get_user_model()

class TestProductView(APITestCase):
    def setUp(self):
        self.seller = User.objects.create_user(
            email='seller@google.com',
            username='seller', 
            password='password', 
            role = 'seller'
            )
        self.buyer = User.objects.create_user(
            email='buyer@google.com',
            username='buyer', 
            password='password',
            role='customer'
            )
        self.product = Product.objects.create(
            name='Test Product',
            description='This is a test product',
            price=Decimal('10.00'),
            stock_quantity=10,
            seller=self.seller
        )
        self.product.category.add('electronics')

    def test_product_list_view(self):
        self.client.force_authenticate(user=self.buyer)
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_product_create_view(self):
        self.client.force_authenticate(user=self.seller)
        url = reverse('product-create')
        data = {
            'name': 'New Product',
            'description': 'A new test product',
            'price': '15.00',
            'stock_quantity': 5,
            'category': ['books']
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)
        new_product = Product.objects.get(name='New Product')
        self.assertEqual(new_product.seller, self.seller)

    def test_product_update_view(self):
        self.client.force_authenticate(user=self.seller)
        url = reverse('product-update', kwargs={'pk': 1})
        data = {
            'name': 'Updated Product',
            'price': '12.00',
            'category': ['electronics', 'gadgets']
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'Updated Product')
        self.assertEqual(self.product.price, Decimal('12.00'))
        self.assertEqual(self.product.category.count(), 2)

    def test_product_delete_view(self):
        self.client.force_authenticate(user=self.seller)
        url = reverse('product-delete', kwargs={'pk': self.product.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)

    def test_product_list_filtering(self):
        self.client.force_authenticate(user=self.buyer)
        url = reverse('product-list')
        response = self.client.get(url, {'min_price': '9.00', 'max_price': '11.00'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

        response = self.client.get(url, {'min_price': '11.00'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 0)

    def test_product_list_search(self):
        self.client.force_authenticate(user=self.buyer)
        url = reverse('product-list')
        response = self.client.get(url, {'search': 'Test'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

        response = self.client.get(url, {'search': 'electronics'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_product_list_ordering(self):
        Product.objects.create(
            name='Cheaper Product',
            description='This is a cheaper product',
            price=Decimal('5.00'),
            stock_quantity=5,
            seller=self.seller
        )
        self.client.force_authenticate(user=self.buyer)
        url = reverse('product-list')
        response = self.client.get(url, {'ordering': 'price'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['name'], 'Cheaper Product')

    def test_unauthorized_access(self):
        self.client.force_authenticate(user=self.buyer)
        url = reverse('product-create')
        data = {
            'name': 'New Product',
            'description': 'A new test product',
            'price': '15.00',
            'stock_quantity': 5,
            'category': ['books']
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_seller_can_only_update_own_products(self):
        other_seller = User.objects.create_user(
            email='other_seller@google.com',
            username='other_seller', 
            password='password', 
            role='seller'
            )
        self.client.force_authenticate(user=other_seller)
        url = reverse('product-update', kwargs={'pk': 2})
        data = {'name': 'Attempt to Update'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_seller_can_only_delete_own_products(self):
        other_seller = User.objects.create_user(
            email='other_seller@google.com',
            username='other_seller', 
            password='password', 
            role='seller'
            )
        self.client.force_authenticate(user=other_seller)
        url = reverse('product-delete', kwargs={'pk': 3})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)