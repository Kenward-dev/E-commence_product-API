# tests/test_urls.py

from django.test import TestCase
from django.urls import reverse, resolve
from products import views

class TestProductURLs(TestCase):
    def test_product_list_url(self):
        url = reverse('product-list')
        self.assertEqual(resolve(url).func.view_class, views.ProductListView)

    def test_product_create_url(self):
        url = reverse('product-create')
        self.assertEqual(resolve(url).func.view_class, views.ProductCreateView)

    def test_product_update_url(self):
        url = reverse('product-update', args=[1])
        self.assertEqual(resolve(url).func.view_class, views.ProductUpdateView)

    def test_product_delete_url(self):
        url = reverse('product-delete', args=[1])
        self.assertEqual(resolve(url).func.view_class, views.ProductDeleteView)