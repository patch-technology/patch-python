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
from patch_api.models.offset_response import OffsetResponse  # noqa: E501
from factories import OffsetFactory
from patch_api.rest import ApiException

class TestOffsetResponse(unittest.TestCase):
    """OffsetResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OffsetResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = patch_api.models.offset_response.OffsetResponse()  # noqa: E501
        if include_optional :
            return OffsetResponse(
                success = True,
                error = None,
                data = OffsetFactory()
            )
        else :
            return OffsetResponse(
                success = True,
                error = None,
                data = OffsetFactory(),
        )

    def testOffsetResponse(self):
        """Test OffsetResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

        self.assertTrue(inst_req_only)
        self.assertTrue(inst_req_and_optional)


if __name__ == '__main__':
    unittest.main()
