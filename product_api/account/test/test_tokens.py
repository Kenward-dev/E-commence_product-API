from django.test import TestCase
from django.contrib.auth import get_user_model
from ..tokens import create_jwt_pair_for_user

User = get_user_model()

class TestTokenCreation(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="testuser@google.com", password="testpassword")

    def test_create_jwt_pair_for_user(self):
        tokens = create_jwt_pair_for_user(self.user)
        
        self.assertIn('access', tokens)
        self.assertIn('refresh', tokens)
        
        self.assertIsInstance(tokens['access'], str)
        self.assertIsInstance(tokens['refresh'], str)
        