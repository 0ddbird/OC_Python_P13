.. module:: models
   :synopsis: Django models for address and letting.

.. automodule:: models
   :members:
   :undoc-members:
   :show-inheritance:

Address Model
=============

.. autoclass:: Address
   :members:
   :undoc-members:
   :show-inheritance:
   :exclude-members: __str__

   Represents an address with number, street, city, state, zip code, and country ISO code.

   Attributes:
       number (int): Positive integer field for address number.
       street (str): Character field for street name.
       city (str): Character field for city name.
       state (str): Character field for state code (2 characters).
       zip_code (int): Positive integer field for ZIP code.
       country_iso_code (str): Character field for country ISO code (3 characters).

   Meta:
       verbose_name_plural = "Addresses"

   Methods:
       __str__(): Returns a formatted string of the address.

Letting Model
=============

.. autoclass:: Letting
   :members:
   :undoc-members:
   :show-inheritance:
   :exclude-members: __str__

   Represents a letting in the system.

   Attributes:
       title (str): Character field for letting title.
       address (:class:`Address`): One-to-one relationship with :class:`Address`.

   Methods:
       __str__(): Returns the title of the letting.
