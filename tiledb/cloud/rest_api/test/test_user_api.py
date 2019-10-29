# coding: utf-8

"""
    TileDB Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 0.6.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import rest_api
from tiledb.cloud.rest_api.api.user_api import UserApi  # noqa: E501
from tiledb.cloud.rest_api.rest import ApiException


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = tiledb.cloud.rest_api.api.user_api.UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_aws_access_credentials(self):
        """Test case for add_aws_access_credentials

        """
        pass

    def test_add_user_to_organization(self):
        """Test case for add_user_to_organization

        """
        pass

    def test_check_aws_access_credentials(self):
        """Test case for check_aws_access_credentials

        """
        pass

    def test_check_aws_access_credentials_by_name(self):
        """Test case for check_aws_access_credentials_by_name

        """
        pass

    def test_confirm_email(self):
        """Test case for confirm_email

        """
        pass

    def test_create_user(self):
        """Test case for create_user

        """
        pass

    def test_delete_aws_access_credentials(self):
        """Test case for delete_aws_access_credentials

        """
        pass

    def test_delete_user(self):
        """Test case for delete_user

        """
        pass

    def test_delete_user_from_organization(self):
        """Test case for delete_user_from_organization

        """
        pass

    def test_get_organization_user(self):
        """Test case for get_organization_user

        """
        pass

    def test_get_user(self):
        """Test case for get_user

        """
        pass

    def test_get_user_with_username(self):
        """Test case for get_user_with_username

        """
        pass

    def test_request_token(self):
        """Test case for request_token

        """
        pass

    def test_reset_user_password(self):
        """Test case for reset_user_password

        """
        pass

    def test_revoke_token(self):
        """Test case for revoke_token

        """
        pass

    def test_tokens_get(self):
        """Test case for tokens_get

        """
        pass

    def test_update_aws_access_credentials(self):
        """Test case for update_aws_access_credentials

        """
        pass

    def test_update_user(self):
        """Test case for update_user

        """
        pass

    def test_update_user_in_organization(self):
        """Test case for update_user_in_organization

        """
        pass


if __name__ == '__main__':
    unittest.main()
