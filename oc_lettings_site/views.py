from django.shortcuts import render

"""
oc_lettings_site app Views module.
"""


# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie quam
# lobortis leo consectetur ullamcorper non id est. Praesent dictum, nulla eget
# feugiat sagittis, sem mi convallis eros, vitae dapibus nisi lorem dapibus sem.
# Maecenas pharetra purus ipsum, eget consequat ipsum lobortis quis. Phasellus
# eleifend ex auctor venenatis tempus. Aliquam vitae erat ac orci placerat luctus.
# Nullam elementum urna nisi, pellentesque iaculis enim cursus in. Praesent volutpat
# porttitor magna, non finibus neque cursus id.
def index(request):
    """
    Renders the index.html template.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - The rendered index.html template.
    """
    return render(request, "oc_lettings_site/index.html")
