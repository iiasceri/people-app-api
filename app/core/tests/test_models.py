from django.test import TestCase
from django.contrib.auth import get_user_model

def sample_user(email='test@ll.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user when email is successful"""
        email = 'test@ll.com'
        password = 'Safepass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@LL.COM'
        user = get_user_model().objects.create_user(email, "password123")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_super_user(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@ll.com',
            'test123'
        )

        # PermissionMixin field:
        self.assertTrue(user.is_superuser)
        # Our custom field:
        self.assertTrue(user.is_staff)

    # def test_history(self):
    #     """Test history ... representation ?"""
    #     history = models.History.objects.create(
    #         user=sample_user(),
    #         name='TestUserHistory'
    #     )
    #
    #     # TODO: Test that history works properly [Nick]
    #     # history.id
    #     self.assertTrue(True)
