Address Model
=============

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
