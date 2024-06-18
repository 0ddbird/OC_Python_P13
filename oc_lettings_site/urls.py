from django.contrib import admin
from django.urls import include, path

from . import views

"""
URL Configuration for the OC Lettings Site.

This module defines the URL patterns for the OC Lettings Site. It includes the
following patterns:

- The root URL pattern, which maps to the index view.
- The "admin/" URL pattern, which maps to the Django admin site.
- The "lettings/" URL pattern, which includes the URL patterns defined in the
"lettings.urls" module.
- The "profiles/" URL  pattern, which includes the URL patterns defined in the
"profiles.urls" module.
"""


def trigger_error(request):
    return 1 / 0


urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
    path("sentry-debug/", trigger_error),
]
