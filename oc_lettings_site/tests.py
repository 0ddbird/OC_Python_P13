from django.test import TestCase
from django.urls import reverse

"""
OC Lettings Site app views test module.
"""


class IndexViewTest(TestCase):
    """
    Test case for the IndexView class.

    This class contains test methods to verify the behavior of the index view.

    Attributes:
        None

    Methods: test_index_view: Test method to verify that the index view returns a 200
    status code and uses the correct template.
    """

    def test_index_view(self):
        """
        Test case for the index view.

        This method tests whether the index view returns a response with a status
        code of 200 and uses the correct template.

        """
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "oc_lettings_site/index.html")
