# coding: utf-8

"""
    TileDB Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 0.3.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from tiledb.cloud.rest_api.api_client import ApiClient
from tiledb.cloud.rest_api.exceptions import (
    ApiTypeError,
    ApiValueError
)


class QueryApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def finalize_query(self, namespace, array, type, content_type, query, **kwargs):  # noqa: E501
        """finalize_query  # noqa: E501

        send a query to run against a specified array/URI registered to a group/project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.finalize_query(namespace, array, type, content_type, query, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str namespace: namespace array is in (an organization name or user's username) (required)
        :param str array: name/uri of array that is url-encoded (required)
        :param str type: type of query (required)
        :param str content_type: Content Type of input and return mime (required)
        :param Query query: query to run (required)
        :param str x_payer: Name of organization or user who should be charged for this request
        :param int open_at: open_at for array in unix epoch
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Query
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.finalize_query_with_http_info(namespace, array, type, content_type, query, **kwargs)  # noqa: E501

    def finalize_query_with_http_info(self, namespace, array, type, content_type, query, **kwargs):  # noqa: E501
        """finalize_query  # noqa: E501

        send a query to run against a specified array/URI registered to a group/project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.finalize_query_with_http_info(namespace, array, type, content_type, query, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str namespace: namespace array is in (an organization name or user's username) (required)
        :param str array: name/uri of array that is url-encoded (required)
        :param str type: type of query (required)
        :param str content_type: Content Type of input and return mime (required)
        :param Query query: query to run (required)
        :param str x_payer: Name of organization or user who should be charged for this request
        :param int open_at: open_at for array in unix epoch
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Query, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['namespace', 'array', 'type', 'content_type', 'query', 'x_payer', 'open_at']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method finalize_query" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'namespace' is set
        if ('namespace' not in local_var_params or
                local_var_params['namespace'] is None):
            raise ApiValueError("Missing the required parameter `namespace` when calling `finalize_query`")  # noqa: E501
        # verify the required parameter 'array' is set
        if ('array' not in local_var_params or
                local_var_params['array'] is None):
            raise ApiValueError("Missing the required parameter `array` when calling `finalize_query`")  # noqa: E501
        # verify the required parameter 'type' is set
        if ('type' not in local_var_params or
                local_var_params['type'] is None):
            raise ApiValueError("Missing the required parameter `type` when calling `finalize_query`")  # noqa: E501
        # verify the required parameter 'content_type' is set
        if ('content_type' not in local_var_params or
                local_var_params['content_type'] is None):
            raise ApiValueError("Missing the required parameter `content_type` when calling `finalize_query`")  # noqa: E501
        # verify the required parameter 'query' is set
        if ('query' not in local_var_params or
                local_var_params['query'] is None):
            raise ApiValueError("Missing the required parameter `query` when calling `finalize_query`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']  # noqa: E501
        if 'array' in local_var_params:
            path_params['array'] = local_var_params['array']  # noqa: E501

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))  # noqa: E501
        if 'open_at' in local_var_params:
            query_params.append(('open_at', local_var_params['open_at']))  # noqa: E501

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']  # noqa: E501
        if 'x_payer' in local_var_params:
            header_params['X-Payer'] = local_var_params['x_payer']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'query' in local_var_params:
            body_params = local_var_params['query']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/capnp'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/capnp'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/arrays/{namespace}/{array}/query/finalize', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Query',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def submit_query(self, namespace, array, type, content_type, query, **kwargs):  # noqa: E501
        """submit_query  # noqa: E501

        send a query to run against a specified array/URI registered to a group/project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.submit_query(namespace, array, type, content_type, query, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str namespace: namespace array is in (an organization name or user's username) (required)
        :param str array: name/uri of array that is url-encoded (required)
        :param str type: type of query (required)
        :param str content_type: Content Type of input and return mime (required)
        :param Query query: query to run (required)
        :param str x_payer: Name of organization or user who should be charged for this request
        :param int open_at: open_at for array in unix epoch
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Query
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.submit_query_with_http_info(namespace, array, type, content_type, query, **kwargs)  # noqa: E501

    def submit_query_with_http_info(self, namespace, array, type, content_type, query, **kwargs):  # noqa: E501
        """submit_query  # noqa: E501

        send a query to run against a specified array/URI registered to a group/project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.submit_query_with_http_info(namespace, array, type, content_type, query, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str namespace: namespace array is in (an organization name or user's username) (required)
        :param str array: name/uri of array that is url-encoded (required)
        :param str type: type of query (required)
        :param str content_type: Content Type of input and return mime (required)
        :param Query query: query to run (required)
        :param str x_payer: Name of organization or user who should be charged for this request
        :param int open_at: open_at for array in unix epoch
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Query, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['namespace', 'array', 'type', 'content_type', 'query', 'x_payer', 'open_at']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method submit_query" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'namespace' is set
        if ('namespace' not in local_var_params or
                local_var_params['namespace'] is None):
            raise ApiValueError("Missing the required parameter `namespace` when calling `submit_query`")  # noqa: E501
        # verify the required parameter 'array' is set
        if ('array' not in local_var_params or
                local_var_params['array'] is None):
            raise ApiValueError("Missing the required parameter `array` when calling `submit_query`")  # noqa: E501
        # verify the required parameter 'type' is set
        if ('type' not in local_var_params or
                local_var_params['type'] is None):
            raise ApiValueError("Missing the required parameter `type` when calling `submit_query`")  # noqa: E501
        # verify the required parameter 'content_type' is set
        if ('content_type' not in local_var_params or
                local_var_params['content_type'] is None):
            raise ApiValueError("Missing the required parameter `content_type` when calling `submit_query`")  # noqa: E501
        # verify the required parameter 'query' is set
        if ('query' not in local_var_params or
                local_var_params['query'] is None):
            raise ApiValueError("Missing the required parameter `query` when calling `submit_query`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']  # noqa: E501
        if 'array' in local_var_params:
            path_params['array'] = local_var_params['array']  # noqa: E501

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))  # noqa: E501
        if 'open_at' in local_var_params:
            query_params.append(('open_at', local_var_params['open_at']))  # noqa: E501

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']  # noqa: E501
        if 'x_payer' in local_var_params:
            header_params['X-Payer'] = local_var_params['x_payer']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'query' in local_var_params:
            body_params = local_var_params['query']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/capnp'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/capnp'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/arrays/{namespace}/{array}/query/submit', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Query',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
