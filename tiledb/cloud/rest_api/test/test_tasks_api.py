# coding: utf-8

"""
    TileDB Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 2.1.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import rest_api
from tiledb.cloud.rest_api.api.tasks_api import TasksApi  # noqa: E501
from tiledb.cloud.rest_api.rest import ApiException


class TestTasksApi(unittest.TestCase):
    """TasksApi unit test stubs"""

    def setUp(self):
        self.api = tiledb.cloud.rest_api.api.tasks_api.TasksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_run_sql(self):
        """Test case for run_sql

        """
        pass

    def test_task_id_get(self):
        """Test case for task_id_get

        """
        pass

    def test_tasks_get(self):
        """Test case for tasks_get

        """
        pass


if __name__ == '__main__':
    unittest.main()
