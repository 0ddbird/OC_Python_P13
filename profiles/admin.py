from django.contrib import admin
from profiles.models import Profile

"""
Profile app admin module.
"""


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Admin class for managing Profile model in the Django admin interface.
    """

    list_display = (
        "user",
        "favorite_city",
    )
