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
from tiledb.cloud.rest_api.models.array_browser_data import (
    ArrayBrowserData,
)  # noqa: E501
from tiledb.cloud.rest_api.rest import ApiException


class TestArrayBrowserData(unittest.TestCase):
    """ArrayBrowserData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ArrayBrowserData
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # model = tiledb.cloud.rest_api.models.array_browser_data.ArrayBrowserData()  # noqa: E501
        if include_optional:
            return ArrayBrowserData(
                arrays=[
                    tiledb.cloud.rest_api.models.array_info.ArrayInfo(
                        id="00000000-0000-0000-0000-000000000000",
                        file_type="notebook",
                        file_properties={"key": "0"},
                        uri="s3://bucket/array",
                        namespace="user1",
                        size=1024.0,
                        last_accessed=datetime.datetime.strptime(
                            "2013-10-20 19:20:30.00", "%Y-%m-%d %H:%M:%S.%f"
                        ),
                        description="0",
                        name="myarray1",
                        allowed_actions=["read"],
                        pricing=[
                            tiledb.cloud.rest_api.models.pricing.Pricing(
                                id="planID",
                                array_uuid="00000000-0000-0000-0000-000000000000",
                                pricing_name="0",
                                pricing_type="egress",
                                product_name="0",
                                product_statement_descriptor="0",
                                product_unit_label="byte",
                                currency="USD",
                                aggregate_usage="sum",
                                interval="month",
                                divided_by=1048576,
                                charge=1.337,
                                activated=False,
                            )
                        ],
                        subscriptions=[
                            tiledb.cloud.rest_api.models.subscription.Subscription(
                                id="subscriptionID",
                                owner_namespace_uuid="00000000-0000-0000-0000-000000000000",
                                customer_namespace_uuid="00000000-0000-0000-0000-000000000000",
                            )
                        ],
                        logo="0",
                        access_credentials_name="0",
                        type="sparse",
                        share_count=1.337,
                        public_share=True,
                        namespace_subscribed=False,
                        tiledb_uri="0",
                        tags=["0"],
                        license_id="0",
                        license_text="0",
                    )
                ],
                pagination_metadata=tiledb.cloud.rest_api.models.pagination_metadata.PaginationMetadata(
                    page=1.0,
                    per_page=10.0,
                    total_pages=14.0,
                    total_items=138.0,
                ),
            )
        else:
            return ArrayBrowserData()

    def testArrayBrowserData(self):
        """Test ArrayBrowserData"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
