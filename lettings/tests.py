from django.test import RequestFactory, TestCase
from django.urls import reverse

from lettings.models import Letting
from lettings.views import letting, lettings_index

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

        This method is called before each test case to set up any necessary objects or variables.
        In this case, it initializes a RequestFactory, sets the URL for the "lettings_index" view,
        and creates two Letting objects for testing purposes.
        """
        self.factory = RequestFactory()
        self.url = reverse("lettings_index")
        self.letting1 = Letting.objects.create(title="Letting 1", address="Address 1")
        self.letting2 = Letting.objects.create(title="Letting 2", address="Address 2")

    def test_lettings_index(self):
        """
        Test case for the lettings_index view.

        This test verifies that the lettings_index view returns a response with status code 200,
        uses the correct template, and contains the expected content.

        It creates a GET request using the test client's factory, calls the lettings_index view,
        and then asserts various conditions on the response.

        Assertions:
        - The response status code should be 200.
        - The response should use the "lettings/index.html" template.
        - The response should contain the title and address of self.letting1.
        - The response should contain the title and address of self.letting2.
        """
        request = self.factory.get(self.url)
        response = lettings_index(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/index.html")
        self.assertContains(response, self.letting1.title)
        self.assertContains(response, self.letting1.address)
        self.assertContains(response, self.letting2.title)
        self.assertContains(response, self.letting2.address)


class LettingViewTestCase(TestCase):
    """
    Test case for the LettingView view.
    """

    def setUp(self):
        """
        Set up the test environment before each test case.

        This method is called before each test case to set up any necessary
        objects or configurations. In this case, it initializes a `RequestFactory`
        object and creates a `Letting` object for testing purposes.

        """
        self.factory = RequestFactory()
        self.letting = Letting.objects.create(
            title="Test Letting", address="123 Test Street"
        )

    def test_letting_view(self):
        """
        Test case for the letting view.

        This method tests the behavior of the letting view by making a GET request to the '/lettings/1' URL
        and asserting that the response status code is 200 (OK). It also checks if the response contains
        the letting's title and address.

        """
        request = self.factory.get("/lettings/1")
        response = letting(request, letting_id=self.letting.id)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.letting.title)
        self.assertContains(response, self.letting.address)

    def test_letting_view_invalid_id(self):
        """
        Test case to verify the behavior of the letting view when an invalid ID is provided.
        It should return a 404 status code.
        """
        request = self.factory.get("/lettings/999")
        response = letting(request, letting_id=999)
        self.assertEqual(response.status_code, 404)
