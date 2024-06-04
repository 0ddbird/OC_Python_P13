from django.contrib import admin

from lettings.models import Address, Letting

"""
Lettings app admin classes module.
"""


@admin.register(Letting)
class LettingAdmin(admin.ModelAdmin):
    """
    Admin class for managing Letting model in the Django admin interface.
    """

    list_display = ("title",)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    """
    Admin class for managing Address model in the Django admin interface.
    """

    list_display = (
        "number",
        "street",
        "city",
        "state",
        "zip_code",
        "country_iso_code",
    )
