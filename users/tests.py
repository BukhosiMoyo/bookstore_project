from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTests(TestCase):


    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="maxx", 
            email="maxx@email.com", 
            password="testpass123"
        )

        self.assertEqual(user.username, "maxx")
        self.assertEqual(user.email, "maxx@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="superadmin",
            email="superadmin@email.com",
            password="testpass123"
        )

        self.assertTrue(admin_user.username, "superadmin")
        self.assertTrue(admin_user.email, "superadmin@email.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
