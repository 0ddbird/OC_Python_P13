from django.urls import path

from . import views

"""
Profiles app urls module.

This module defines the URL patterns for the profiles app. It includes two patterns:
- An empty path that maps to the profiles_index view.
- A path with a username parameter that maps to the profile view.

These URL patterns are used to route incoming requests to the appropriate views.
"""


urlpatterns = [
    path("", views.profiles_index, name="profiles_index"),
    path("<str:username>/", views.profile, name="profile"),
]
