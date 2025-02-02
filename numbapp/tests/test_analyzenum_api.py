"""
Test analyzeNum api
"""


from rest_framework.test import APITestCase
from django.urls import reverse
from unittest.mock import patch
from rest_framework import status

class AnalzeNumTest(APITestCase):
    """
    Tests for getting values for the analyze API
    """

    @patch("numbapp.utils.get_funfact_for_number")
    def test_analyzeNum_api_is_successful(self, mock_fun_fact):

        """Check if API returns a status 200 response code"""
        mock_fun_fact.return_value = "Mocked fun fact"

        url = reverse("app:analyze-num")
        res = self.client.get(url, {"number": 28})  # Make sure 'number' is passed as a query parameter

        self.assertEqual(res.status_code, status.HTTP_200_OK)


    def test_analyze_num_with_invalid_number(self):
        """Check if API handles invalid number gracefully"""

        test_number = "abc"  # Invalid number
        url = reverse("app:analyze-num")
        params = {"number": test_number}

        response = self.client.get(url, params=params)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  # Expecting a bad request

    @patch("numbapp.utils.get_funfact_for_number")
    def test_analyze_num_api_returns_correct_data(self, mock_fun_fact):
        """Test if API returns the correct data for a number"""

        mock_fun_fact.return_value = "Mocked fun fact"

        url = reverse("app:analyze-num")
        res = self.client.get(url, {"number": "28"})  # Make sure 'number' is passed as a query parameter

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        data = res.data  # Ensure this is parsed as JSON

        # Assertions
        self.assertEqual(data["number"], 28)
        self.assertFalse(data["is_prime"])
        self.assertTrue(data["is_perfect"])
        self.assertIn("even", data["properties"])
        self.assertEqual(data["digit_sum"], 10)
        self.assertEqual(data["fun_fact"], "Mocked fun fact")

