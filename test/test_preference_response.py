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
import datetime

import patch_api
from patch_api.models.preference_response import PreferenceResponse  # noqa: E501
from factories import PreferenceFactory
from patch_api.rest import ApiException


class TestPreferenceResponse(unittest.TestCase):
    """PreferenceResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PreferenceResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = patch_api.models.preference_response.PreferenceResponse()  # noqa: E501
        if include_optional:
            return PreferenceResponse(
                success=True, error=None, data=PreferenceFactory()
            )
        else:
            return PreferenceResponse(
                success=True, error=None, data=PreferenceFactory()
            )

    def testPreferenceResponse(self):
        """Test PreferenceResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

        self.assertTrue(inst_req_only)
        self.assertTrue(inst_req_and_optional)


if __name__ == "__main__":
    unittest.main()
