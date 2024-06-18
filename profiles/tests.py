from django.contrib.auth.models import User
from django.test import TestCase

from .models import Profile

"""
Profile app models test module.
"""


class ProfileModelTest(TestCase):
    """
    Test case for the Profile model.
    """

    def setUp(self):
        """
        Set up the test environment by creating a user and a profile.
        """
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.profile = Profile.objects.create(user=self.user, favorite_city="New York")

    def test_profile_str(self):
        """
        Test the string representation of the Profile model.

        The string representation of the Profile model should be equal to the
        username of the associated User model.
        """
        self.assertEqual(str(self.profile), self.user.username)

    def test_profile_user(self):
        """
        Test case to verify that the profile's user is equal to the provided user.
        """
        self.assertEqual(self.profile.user, self.user)

    def test_profile_favorite_city(self):
        """
        Test case to verify the favorite city of a profile.

        It checks if the favorite city of the profile matches the expected value "New
        York".
        """
        self.assertEqual(self.profile.favorite_city, "New York")
