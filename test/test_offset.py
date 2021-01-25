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
from patch_api.models.offset import Offset  # noqa: E501
from patch_api.rest import ApiException


class TestOffset(unittest.TestCase):
    """Offset unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Offset
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = patch_api.models.offset.Offset()  # noqa: E501
        if include_optional:
            return Offset(
                id="0",
                allocated_mass_g=0,
                fulfilled_at="0",
                fulfillment_state="pending",
                mass_g=1,
                price_cents_usd="0",
                production=True,
                retired=True,
                serial_number="0",
                vintage_year=56,
                project_id="0",
            )
        else:
            return Offset(
                id="0",
                allocated_mass_g=0,
                fulfillment_state="pending",
                mass_g=1,
                price_cents_usd="0",
                production=True,
                retired=True,
                serial_number="0",
                vintage_year=56,
                project_id="0",
            )

    def testOffset(self):
        """Test Offset"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

        self.assertTrue(inst_req_only)
        self.assertTrue(inst_req_and_optional)


if __name__ == "__main__":
    unittest.main()
