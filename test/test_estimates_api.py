# coding: utf-8

"""
    Patch API V1

    The core API used to integrate with Patch's service  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: developers@usepatch.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import os

from patch_api.api_client import ApiClient


class TestEstimatesApi(unittest.TestCase):
    """EstimatesApi unit test stubs"""

    def setUp(self):
        api_client = ApiClient(api_key=os.environ.get("SANDBOX_API_KEY"))
        self.api = api_client.estimates  # noqa: E501

    def tearDown(self):
        self.api = None

    def test_create_and_retrieve_mass_estimate(self):
        """Test case for create_mass_estimate

        Create an estimate based on mass of CO2  # noqa: E501
        """
        mass_g = 100
        project_id = "pro_test_2b67b11a030b66e0a6dd61a56b49079a"
        estimate = self.api.create_mass_estimate(mass_g=mass_g, project_id=project_id)
        self.assertTrue(estimate)
        self.assertEqual(estimate.data.order.mass_g, mass_g)

        retrieved_estimate = self.api.retrieve_estimate(id=estimate.data.id)
        self.assertTrue(retrieved_estimate)

    def test_create_and_retrieve_flight_estimate(self):
        """Test case for create_mass_estimate

        Create an estimate based on mass of CO2  # noqa: E501
        """
        distance_m = 100
        estimate = self.api.create_mass_estimate(distance_m=distance_m)
        self.assertTrue(estimate)
        self.assertEqual(estimate.data.order.distance_m, distance_m)

        retrieved_estimate = self.api.retrieve_estimate(id=estimate.data.id)
        self.assertTrue(retrieved_estimate)


if __name__ == "__main__":
    unittest.main()
