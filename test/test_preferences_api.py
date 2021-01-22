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
from urllib.error import HTTPError

import patch_api
from patch_api.api.preferences_api import PreferencesApi  # noqa: E501
from patch_api.models.create_preference_request import CreatePreferenceRequest
from patch_api.rest import ApiException


class TestPreferencesApi(unittest.TestCase):
    """PreferencesApi unit test stubs"""

    def setUp(self):
        configuration = patch_api.Configuration(api_key=os.environ.get('SANDBOX_API_KEY'))
        api_client = patch_api.ApiClient(configuration)
        self.api = PreferencesApi(api_client=api_client)  # noqa: E501

    def tearDown(self):
        pass

    # def test_delete_and_create_preference(self):
    #     """Test case for create_preference

    #     creates a project preference  # noqa: E501
    #     """
    #     # Try to create the preference
    #     try:
    #         project_id = "pro_test_2b67b11a030b66e0a6dd61a56b49079a"

    #         create_preference_request = CreatePreferenceRequest(project_id=project_id)
    #         preference = self.api.create_preference(create_preference_request)

    #     # Delete it if it exists
    #     except ApiException as err:
    #         print('err---------------->', err)
    #         deleted_preference = self.api.delete_preference(id=project_id)
    #         self.assertTrue(deleted_preference)

        # self.assertTrue(preference)
        # self.assertEqual(preference.data.project_id, project_id)


        # def test_retrieve_preference(self):
        #     """Test case for retrieve_preference

        #     Retrieve the preference  # noqa: E501
        #     """
        #     project_id = "pro_test_2b67b11a030b66e0a6dd61a56b49079a"

        #     create_preference_request = CreatePreferenceRequest(project_id=project_id)
        #     preference = self.api.create_preference(create_preference_request)

        #     preference = self.api.retrieve_preference()


    def test_retrieve_preferences(self):
        """Test case for retrieve_preferences

        Retrieves a list of preferences  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
