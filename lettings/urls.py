from django.urls import path

from . import views

"""
Lettings app urls modules.

This module defines the URL patterns for the lettings app. It includes two patterns:
- An empty path that maps to the `lettings_index` view function.
- A path with an integer parameter `letting_id` that maps to the `letting` view function.

These URL patterns are used to route incoming requests to the appropriate view functions.
"""


urlpatterns = [
    path("", views.lettings_index, name="lettings_index"),
    path("<int:letting_id>/", views.letting, name="letting"),
]
