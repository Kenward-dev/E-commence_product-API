from django.test import TestCase
from django.contrib.auth import get_user_model
from account.models import Profile

User = get_user_model()

class TestUserModel(TestCase):
    def setUp(self):
        self.user_data = {
            'email': 'testuser@google.com',
            'username': 'testuser',
            'password': 'testpassword123',
            'role': 'customer'
        }
        self.user = User.objects.create_user(**self.user_data)
    
    def test_create_user(self):
        self.assertEqual(self.user.email, self.user_data['email'])
        self.assertEqual(self.user.username, self.user_data['username'])
        self.assertEqual(self.user.role, self.user_data['role'])
        self.assertTrue(self.user.check_password(self.user_data['password']))
    
    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(
            email='admin@example.com',
            username='admin',
            password='adminpassword123'
        )
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertEqual(admin_user.role, 'admin')
        
    def test_user_str_method(self):
        self.assertEqual(str(self.user), f"{self.user.username}|{self.user.role}")

    def test_user_roles(self):
        self.assertTrue(self.user.is_customer())
        self.assertFalse(self.user.is_admin())
        self.assertFalse(self.user.is_seller())

class TestProfileCreation(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='profile@google.com',
            username='profileuser',
            password='profilepassword123'
        )
        self.profile = self.user.profile

    def test_profile_creation(self):
        self.assertIsInstance(self.profile, Profile)
        self.assertEqual(self.profile.user, self.user)

    def test_profile_str_method(self):
        self.assertEqual(str(self.profile), f"{self.user.username}'s Profile")