from django.shortcuts import render

from profiles.models import Profile

"""
Profiles app views module.
"""


# Sed placerat quam in pulvinar commodo.
# Nullam laoreet consectetur ex, sed consequat libero pulvinar eget. Fusc
# faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum lacus d
def profiles_index(request):
    """
    View function for displaying the index page of profiles.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered index.html template.
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate.
# Sed tincidunt, dolor id facilisis fringilla, eros leo tristique lacus,
# it. Nam aliquam dignissim congue.
# Pellentesque habitant morbi tristique senectus et netus et males
def profile(request, username):
    """
    View function to display the profile of a user.

    Args:
        request (HttpRequest): The HTTP request object.
        username (str): The username of the user whose profile is being viewed.

    Returns:
        HttpResponse: The HTTP response object containing the rendered profile template.
    """
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
