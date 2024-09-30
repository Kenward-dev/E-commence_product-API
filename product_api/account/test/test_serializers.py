from django.test import TestCase
from django.contrib.auth import get_user_model
from account.serializers import UserSerializer, ProfileSerializer
from account.models import Profile

User = get_user_model()

class TestUserSerializer(TestCase):
    def setUp(self):
        self.user_data = {
            'email': 'testuser@google.com',
            'username': 'testuser',
            'password': 'testpassword123',
            'role': 'customer'
        }
        self.serializer = UserSerializer(data=self.user_data)

    def test_contains_expected_fields(self):
        self.assertTrue(self.serializer.is_valid())
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['email', 'username', 'role'])

    def test_password_write_only(self):
        self.assertTrue(self.serializer.is_valid())
        self.assertNotIn('password', self.serializer.data)

    def test_create_user(self):
        self.assertTrue(self.serializer.is_valid())
        user = self.serializer.save()
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, self.user_data['email'])
        self.assertTrue(user.check_password(self.user_data['password']))

class TestProfileSerializer(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='profile@google.com',
            username='profileuser',
            password='profilepassword123'
        )
        self.profile_data = {
            'date_of_birth': '1990-01-01',
            'address': '123 Test St',
            'phone_number': '1234567890'
        }
        self.serializer = ProfileSerializer(instance=self.user.profile, data=self.profile_data, partial=True)

    def test_contains_expected_fields(self):
        self.assertTrue(self.serializer.is_valid())
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['id', 'username', 'user', 'role', 'date_of_birth', 'address', 'phone_number'])

    def test_update_profile(self):
        self.assertTrue(self.serializer.is_valid())
        updated_profile = self.serializer.save()
        self.assertEqual(updated_profile.date_of_birth.isoformat(), self.profile_data['date_of_birth'])
        self.assertEqual(updated_profile.address, self.profile_data['address'])
        self.assertEqual(updated_profile.phone_number, self.profile_data['phone_number'])

    def test_partial_update(self):
        partial_data = {'address': '456 Update St'}
        serializer = ProfileSerializer(instance=self.user.profile, data=partial_data, partial=True)
        self.assertTrue(serializer.is_valid())
        updated_profile = serializer.save()
        self.assertEqual(updated_profile.address, '456 Update St')
