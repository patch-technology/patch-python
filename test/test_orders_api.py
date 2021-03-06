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


class TestOrdersApi(unittest.TestCase):
    """OrdersApi unit test stubs"""

    def setUp(self):
        api_client = ApiClient(api_key=os.environ.get("SANDBOX_API_KEY"))
        self.api = api_client.orders  # noqa: E501

    def tearDown(self):
        self.api = None

    def test_interactions_with_an_order(self):
        """Test case for create_order, retrieve_order"""

        """Create an order
        """
        order = self.api.create_order(mass_g=100)

        self.assertTrue(order)

        """Create an order on price
        """
        order = self.api.create_order(total_price_cents_usd=100)

        self.assertTrue(order)

        """Retrieve an order
        """
        order = self.api.create_order(mass_g=100)
        retrieved_order = self.api.retrieve_order(id=order.data.id)

        self.assertTrue(retrieved_order)

    def test_retrieve_orders(self):
        """Test case for retrieve_orders

        Retrieves a list of orders  # noqa: E501
        """
        orders = self.api.retrieve_orders().data
        self.assertTrue(isinstance(orders, list))

        if len(orders) > 1:
            retrieved_order = orders[0]

            self.assertTrue(retrieved_order.id)
            self.assertEqual(retrieved_order.production, False)
            self.assertEqual(retrieved_order.state, "placed")
            self.assertEqual(retrieved_order.metadata, {})
            self.assertTrue(isinstance(retrieved_order.allocations, list))


if __name__ == "__main__":
    unittest.main()
