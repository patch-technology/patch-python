from __future__ import absolute_import

from patch_api.configuration import Configuration
from patch_api import rest

import unittest
import os

from patch_api.api_client import ApiClient


class TestRESTClientObject(unittest.TestCase):
    def test_recursive_urlencode(self):
        """Test that the correct query params get encoded"""

        api_key = os.environ.get("SANDBOX_API_KEY")
        configuration = Configuration()
        client = rest.RESTClientObject(api_key, configuration)

        encoded_params = client.recursive_urlencode({})
        self.assertEqual(encoded_params, "")

        encoded_params = client.recursive_urlencode({"page": 1})
        self.assertEqual(encoded_params, "page=1")

        encoded_params = client.recursive_urlencode({"string": "value"})
        self.assertEqual(encoded_params, "string=value")

        encoded_params = client.recursive_urlencode(
            {"multiple": "values", "top": "level"}
        )
        self.assertEqual(encoded_params, "multiple=values&top=level")

        encoded_params = client.recursive_urlencode({"metadata": {"some": "arg"}})
        self.assertEqual(encoded_params, "metadata[some]=arg")

        encoded_params = client.recursive_urlencode(
            {"deeply": {"nested": {"hash": {"of": "args"}}}}
        )
        self.assertEqual(encoded_params, "deeply[nested][hash][of]=args")

    def test_encoded_query_params(self):
        """Test that the correct query params get encoded"""

        api_key = os.environ.get("SANDBOX_API_KEY")
        configuration = Configuration()
        client = rest.RESTClientObject(api_key, configuration)

        encoded_params = client.encoded_query_params([])
        self.assertEqual(encoded_params, "")

        encoded_params = client.encoded_query_params([("mass_g", 100)])
        self.assertEqual(encoded_params, "?mass_g=100")

        encoded_params = client.encoded_query_params(
            [("mass_g", 100), ("metadata", {"external_id": "abc-123"})]
        )
        self.assertEqual(encoded_params, "?metadata[external_id]=abc-123&mass_g=100")
