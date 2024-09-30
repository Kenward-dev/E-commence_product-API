from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from products.models import Product
from reviews.models import Review

class TestReviewModel(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@google.com',
            password='testpassword123',
            role='customer'
        )
        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=9.99,
            seller_id=1
        )

    def test_review_creation(self):
        review = Review.objects.create(
            product=self.product,
            user=self.user,
            rating=4,
            comment='Great product!'
        )
        self.assertEqual(str(review), f"Review by {self.user.username} for {self.product.name}")
        self.assertEqual(review.rating, 4)
        self.assertEqual(review.comment, 'Great product!')

    def test_review_rating_validators(self):
        with self.assertRaises(ValidationError):
            review = Review(
                product=self.product,
                user=self.user,
                rating=0,
                comment='Invalid rating'
            )
            review.full_clean()

        with self.assertRaises(ValidationError):
            review = Review(
                product=self.product,
                user=self.user,
                rating=6,
                comment='Invalid rating'
            )
            review.full_clean()

    def test_review_optional_comment(self):
        review = Review.objects.create(
            product=self.product,
            user=self.user,
            rating=5
        )
        self.assertIsNone(review.comment)