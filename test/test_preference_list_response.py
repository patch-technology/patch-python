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
from patch_api.models.preference_list_response import (
    PreferenceListResponse,
)  # noqa: E501
from factories import MetaIndexObjectFactory, PreferenceFactory
from patch_api.rest import ApiException


class TestPreferenceListResponse(unittest.TestCase):
    """PreferenceListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PreferenceListResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = patch_api.models.preference_list_response.PreferenceListResponse()  # noqa: E501
        if include_optional:
            return PreferenceListResponse(
                success=True,
                error=None,
                data=[PreferenceFactory()],
                meta=MetaIndexObjectFactory(),
            )
        else:
            return PreferenceListResponse(
                success=True,
                error=None,
                data=[PreferenceFactory()],
                meta=MetaIndexObjectFactory(),
            )

    def testPreferenceListResponse(self):
        """Test PreferenceListResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

        self.assertTrue(inst_req_only)
        self.assertTrue(inst_req_and_optional)


if __name__ == "__main__":
    unittest.main()
