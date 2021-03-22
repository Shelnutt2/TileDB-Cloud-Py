# coding: utf-8

"""
    TileDB Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 2.2.19
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import rest_api
from tiledb.cloud.rest_api.models.udf_info_update import UDFInfoUpdate  # noqa: E501
from tiledb.cloud.rest_api.rest import ApiException


class TestUDFInfoUpdate(unittest.TestCase):
    """UDFInfoUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UDFInfoUpdate
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # model = tiledb.cloud.rest_api.models.udf_info_update.UDFInfoUpdate()  # noqa: E501
        if include_optional:
            return UDFInfoUpdate(
                name="0",
                language="python",
                version="0",
                image_name="0",
                type="single_array",
                _exec="0",
                exec_raw="0",
                readme="0",
                license_id="0",
                license_text="0",
                tags=["0"],
            )
        else:
            return UDFInfoUpdate()

    def testUDFInfoUpdate(self):
        """Test UDFInfoUpdate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
