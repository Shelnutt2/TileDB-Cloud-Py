# coding: utf-8

"""
    TileDB Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 2.1.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import rest_api
from tiledb.cloud.rest_api.models.attribute_buffer_size import (
    AttributeBufferSize,
)  # noqa: E501
from tiledb.cloud.rest_api.rest import ApiException


class TestAttributeBufferSize(unittest.TestCase):
    """AttributeBufferSize unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AttributeBufferSize
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # model = tiledb.cloud.rest_api.models.attribute_buffer_size.AttributeBufferSize()  # noqa: E501
        if include_optional:
            return AttributeBufferSize(attribute="0", offset_bytes=56, data_bytes=56)
        else:
            return AttributeBufferSize(
                attribute="0",
                offset_bytes=56,
                data_bytes=56,
            )

    def testAttributeBufferSize(self):
        """Test AttributeBufferSize"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
