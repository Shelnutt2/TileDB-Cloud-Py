# coding: utf-8

"""
    TileDB Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 2.2.19
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import datetime
import unittest

import tiledb.cloud.rest_api
from tiledb.cloud.rest_api.models.favorites_data import FavoritesData  # noqa: E501
from tiledb.cloud.rest_api.rest import ApiException


class TestFavoritesData(unittest.TestCase):
    """FavoritesData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FavoritesData
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # model = tiledb.cloud.rest_api.models.favorites_data.FavoritesData()  # noqa: E501
        if include_optional:
            return FavoritesData(
                favorites=[
                    tiledb.cloud.rest_api.models.favorite.Favorite(
                        id="0",
                        object_type="ARRAY",
                        namespace="0",
                        name="0",
                        created_at=datetime.datetime.strptime(
                            "2013-10-20 19:20:30.00", "%Y-%m-%d %H:%M:%S.%f"
                        ),
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
            return FavoritesData()

    def testFavoritesData(self):
        """Test FavoritesData"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
