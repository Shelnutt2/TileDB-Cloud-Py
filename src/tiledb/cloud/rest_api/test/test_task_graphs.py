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
from tiledb.cloud.rest_api.models.task_graphs import TaskGraphs  # noqa: E501
from tiledb.cloud.rest_api.rest import ApiException


class TestTaskGraphs(unittest.TestCase):
    """TaskGraphs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TaskGraphs
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # model = tiledb.cloud.rest_api.models.task_graphs.TaskGraphs()  # noqa: E501
        if include_optional:
            return TaskGraphs(
                graphs=[
                    tiledb.cloud.rest_api.models.task_graph.TaskGraph(
                        uuid="0",
                        namespace="0",
                        created_by="0",
                        name="0",
                        created_at=datetime.datetime.strptime(
                            "2013-10-20 19:20:30.00", "%Y-%m-%d %H:%M:%S.%f"
                        ),
                        nodes=[
                            tiledb.cloud.rest_api.models.task_graph_node.TaskGraphNode(
                                client_node_id="0",
                                name="0",
                                depends_on=["0"],
                                array_node=tiledb.cloud.rest_api.models.udf_array_details.UDFArrayDetails(
                                    parameter_id="0",
                                    uri="0",
                                    ranges=tiledb.cloud.rest_api.models.query_ranges.QueryRanges(
                                        layout="row-major",
                                    ),
                                    buffers=["0"],
                                ),
                                input_node=tiledb.cloud.rest_api.models.tg_input_node_data.TGInputNodeData(
                                    default_value=tiledb.cloud.rest_api.models.tg_arg_value.TGArgValue(),
                                    datatype="0",
                                ),
                                sql_node=tiledb.cloud.rest_api.models.tgsql_node_data.TGSQLNodeData(
                                    init_commands=["0"],
                                    query="0",
                                    parameters=[
                                        tiledb.cloud.rest_api.models.tg_arg_value.TGArgValue()
                                    ],
                                    result_format="python_pickle",
                                    namespace="0",
                                ),
                                udf_node=tiledb.cloud.rest_api.models.tgudf_node_data.TGUDFNodeData(
                                    registered_udf_name="0",
                                    executable_code="0",
                                    source_text="0",
                                    environment=tiledb.cloud.rest_api.models.tgudf_environment.TGUDFEnvironment(
                                        language="python",
                                        language_version="0",
                                        image_name="0",
                                        namespace="0",
                                        resource_class="0",
                                        resources=tiledb.cloud.rest_api.models.tgudf_environment_resources.TGUDFEnvironment_resources(
                                            cpu="500m",
                                            memory="8Gi",
                                        ),
                                        run_client_side=True,
                                    ),
                                    arguments=[
                                        tiledb.cloud.rest_api.models.tgudf_argument.TGUDFArgument(
                                            name="0",
                                            value=tiledb.cloud.rest_api.models.tg_arg_value.TGArgValue(),
                                        )
                                    ],
                                ),
                                retry_strategy=tiledb.cloud.rest_api.models.retry_strategy.RetryStrategy(
                                    backoff=tiledb.cloud.rest_api.models.backoff.Backoff(
                                        duration="0",
                                        factor=56,
                                        max_duration="0",
                                    ),
                                    expression="0",
                                    limit=56,
                                    retry_policy="Always",
                                ),
                            )
                        ],
                        parallelism=56,
                        retry_strategy=tiledb.cloud.rest_api.models.retry_strategy.RetryStrategy(
                            expression="0",
                            limit=56,
                        ),
                    )
                ]
            )
        else:
            return TaskGraphs()

    def testTaskGraphs(self):
        """Test TaskGraphs"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
