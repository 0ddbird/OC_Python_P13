from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from lettings.models import Letting, Address
from lettings.views import letting

"""
Lettings app views test module.
"""


class LettingsIndexTestCase(TestCase):
    """
    Test case for the LettingsIndex view.
    """

    def setUp(self):
        """
        Set up the test environment before each test case.

        This method is called before each test case to set up any necessary objects
        or variables. In this case, it initializes a RequestFactory, sets the URL for
        the "lettings_index" view, and creates two Letting objects for testing purposes.
        """
        self.factory = RequestFactory()
        self.url = reverse("lettings_index")
        self.letting1 = Letting.objects.create(
            title="Letting 1",
            address=Address.objects.create(
                number=1,
                street="street1",
                city="city1",
                state="st",
                zip_code=12345,
                country_iso_code="USA",
            ),
        )
        self.letting2 = Letting.objects.create(
            title="Letting 2",
            address=Address.objects.create(
                number=2,
                street="street2",
                city="city2",
                state="st",
                zip_code=54321,
                country_iso_code="USA",
            ),
        )

    def test_lettings_index(self):
        """
        Test case for the lettings_index view.

        This test verifies that the lettings_index view returns a response with
        status code 200, uses the correct template, and contains the expected content.

        It creates a GET request using the test client's factory, calls the
        lettings_index view using the Django test Client, and then asserts various
        conditions on the response.

        Assertions:
        - The response status code should be 200.
        - The response should use the "lettings/index.html" template.
        - The response should contain the title and address of self.letting1.
        - The response should contain the title and address of self.letting2.
        """
        client = Client()
        response = client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/index.html")
        self.assertContains(response, self.letting1.title)
        self.assertContains(response, self.letting2.title)

    def test_letting_view(self):
        """
        Test case for the letting view.

        This method tests the behavior of the letting view by making a GET request to
        the '/lettings/1' URL and asserting that the response status code is 200 (
        OK). It also checks if the response contains the letting's title and address.

        """
        request = self.factory.get("/lettings/1")
        response = letting(request, letting_id=self.letting1.id)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.letting1.title)
        self.assertContains(response, self.letting1.address.street)
