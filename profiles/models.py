from django.contrib.auth.models import User
from django.db import models

"""
Profile app models module.
"""


class Profile(models.Model):
    """
    Represents a user profile.

    Attributes:
        user (User): The user associated with the profile.
        favorite_city (str): The favorite city of the user.

    Methods:
        __str__(): Returns a string representation of the profile.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
