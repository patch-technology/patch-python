# coding: utf-8

from __future__ import absolute_import

import unittest
import os

from patch_api.api_client import ApiClient


class TestTechnologyTypesApi(unittest.TestCase):
    def setUp(self):
        api_client = ApiClient(api_key=os.environ.get("SANDBOX_API_KEY"))
        self.api = api_client.technology_types  # noqa: E501

    def tearDown(self):
        self.api = None

    def test_retrieve_project(self):
        """Test case for retrieve_technology_types

        Retrieves technology_types  # noqa: E501
        """
        technology_types = self.api.retrieve_technology_types().data

        self.assertTrue(isinstance(technology_types, list))
        self.assertGreater(len(technology_types), 1)

        technology_type = technology_types[0]
        self.assertTrue(isinstance(technology_type.name, str))
        self.assertTrue(isinstance(technology_type.slug, str))

        parent_technology_type = technology_type.parent_technology_type
        self.assertTrue(isinstance(parent_technology_type.name, str))
        self.assertTrue(isinstance(parent_technology_type.slug, str))
