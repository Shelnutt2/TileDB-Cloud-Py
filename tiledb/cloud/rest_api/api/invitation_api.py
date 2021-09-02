# coding: utf-8

"""
    TileDB Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 2.2.19
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from tiledb.cloud.rest_api.api_client import ApiClient
from tiledb.cloud.rest_api.exceptions import ApiTypeError  # noqa: F401
from tiledb.cloud.rest_api.exceptions import ApiValueError


class InvitationApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def accept_invitation(self, invitation, **kwargs):  # noqa: E501
        """accept_invitation  # noqa: E501

        Accepts invitation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.accept_invitation(invitation, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str invitation: the id of invitation about to be accepted (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.accept_invitation_with_http_info(invitation, **kwargs)  # noqa: E501

    def accept_invitation_with_http_info(self, invitation, **kwargs):  # noqa: E501
        """accept_invitation  # noqa: E501

        Accepts invitation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.accept_invitation_with_http_info(invitation, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str invitation: the id of invitation about to be accepted (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["invitation"]
        all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
            ]
        )

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method accept_invitation" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'invitation' is set
        if self.api_client.client_side_validation and (
            "invitation" not in local_var_params
            or local_var_params["invitation"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `invitation` when calling `accept_invitation`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "invitation" in local_var_params:
            path_params["invitation"] = local_var_params["invitation"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["ApiKeyAuth", "BasicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/invitations/{invitation}",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def cancel_join_organization(
        self, invitation, organization, **kwargs
    ):  # noqa: E501
        """cancel_join_organization  # noqa: E501

        Cancels join organization invitation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_join_organization(invitation, organization, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str invitation: the id of invitation about to be cancelled (required)
        :param str organization: name or uuid of organization (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.cancel_join_organization_with_http_info(
            invitation, organization, **kwargs
        )  # noqa: E501

    def cancel_join_organization_with_http_info(
        self, invitation, organization, **kwargs
    ):  # noqa: E501
        """cancel_join_organization  # noqa: E501

        Cancels join organization invitation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_join_organization_with_http_info(invitation, organization, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str invitation: the id of invitation about to be cancelled (required)
        :param str organization: name or uuid of organization (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["invitation", "organization"]
        all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
            ]
        )

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_join_organization" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'invitation' is set
        if self.api_client.client_side_validation and (
            "invitation" not in local_var_params
            or local_var_params["invitation"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `invitation` when calling `cancel_join_organization`"
            )  # noqa: E501
        # verify the required parameter 'organization' is set
        if self.api_client.client_side_validation and (
            "organization" not in local_var_params
            or local_var_params["organization"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `organization` when calling `cancel_join_organization`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "invitation" in local_var_params:
            path_params["invitation"] = local_var_params["invitation"]  # noqa: E501
        if "organization" in local_var_params:
            path_params["organization"] = local_var_params["organization"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["ApiKeyAuth", "BasicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/invitations/{invitation}/{organization}/join",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def cancel_share_array_by_invite(
        self, namespace, invitation, array, **kwargs
    ):  # noqa: E501
        """cancel_share_array_by_invite  # noqa: E501

        Cancels array sharing invitation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_share_array_by_invite(namespace, invitation, array, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str namespace: namespace array is in (an organization name or user's username) (required)
        :param str invitation: the id of invitation about to be cancelled (required)
        :param str array: name/uri of array that is url-encoded (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.cancel_share_array_by_invite_with_http_info(
            namespace, invitation, array, **kwargs
        )  # noqa: E501

    def cancel_share_array_by_invite_with_http_info(
        self, namespace, invitation, array, **kwargs
    ):  # noqa: E501
        """cancel_share_array_by_invite  # noqa: E501

        Cancels array sharing invitation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_share_array_by_invite_with_http_info(namespace, invitation, array, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str namespace: namespace array is in (an organization name or user's username) (required)
        :param str invitation: the id of invitation about to be cancelled (required)
        :param str array: name/uri of array that is url-encoded (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["namespace", "invitation", "array"]
        all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
            ]
        )

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_share_array_by_invite" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'namespace' is set
        if self.api_client.client_side_validation and (
            "namespace" not in local_var_params
            or local_var_params["namespace"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `namespace` when calling `cancel_share_array_by_invite`"
            )  # noqa: E501
        # verify the required parameter 'invitation' is set
        if self.api_client.client_side_validation and (
            "invitation" not in local_var_params
            or local_var_params["invitation"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `invitation` when calling `cancel_share_array_by_invite`"
            )  # noqa: E501
        # verify the required parameter 'array' is set
        if self.api_client.client_side_validation and (
            "array" not in local_var_params
            or local_var_params["array"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `array` when calling `cancel_share_array_by_invite`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "namespace" in local_var_params:
            path_params["namespace"] = local_var_params["namespace"]  # noqa: E501
        if "invitation" in local_var_params:
            path_params["invitation"] = local_var_params["invitation"]  # noqa: E501
        if "array" in local_var_params:
            path_params["array"] = local_var_params["array"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["ApiKeyAuth", "BasicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/invitations/{invitation}/{namespace}/{array}/share",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def fetch_invitations(self, **kwargs):  # noqa: E501
        """fetch_invitations  # noqa: E501

        Fetch a list of invitations  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_invitations(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization: name or id of organization to filter
        :param str array: name/uri of array that is url-encoded to filter
        :param int start: start time for tasks to filter by
        :param int end: end time for tasks to filter by
        :param int page: pagination offset
        :param int per_page: pagination limit
        :param str type: invitation type, \"ARRAY_SHARE\", \"JOIN_ORGANIZATION\"
        :param str status: Filter to only return \"PENDING\", \"ACCEPTED\"
        :param str orderby: sort by which field valid values include timestamp, array_name, organization_name
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InvitationData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.fetch_invitations_with_http_info(**kwargs)  # noqa: E501

    def fetch_invitations_with_http_info(self, **kwargs):  # noqa: E501
        """fetch_invitations  # noqa: E501

        Fetch a list of invitations  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_invitations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization: name or id of organization to filter
        :param str array: name/uri of array that is url-encoded to filter
        :param int start: start time for tasks to filter by
        :param int end: end time for tasks to filter by
        :param int page: pagination offset
        :param int per_page: pagination limit
        :param str type: invitation type, \"ARRAY_SHARE\", \"JOIN_ORGANIZATION\"
        :param str status: Filter to only return \"PENDING\", \"ACCEPTED\"
        :param str orderby: sort by which field valid values include timestamp, array_name, organization_name
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InvitationData, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            "organization",
            "array",
            "start",
            "end",
            "page",
            "per_page",
            "type",
            "status",
            "orderby",
        ]
        all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
            ]
        )

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_invitations" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if (
            "organization" in local_var_params
            and local_var_params["organization"] is not None
        ):  # noqa: E501
            query_params.append(
                ("organization", local_var_params["organization"])
            )  # noqa: E501
        if (
            "array" in local_var_params and local_var_params["array"] is not None
        ):  # noqa: E501
            query_params.append(("array", local_var_params["array"]))  # noqa: E501
        if (
            "start" in local_var_params and local_var_params["start"] is not None
        ):  # noqa: E501
            query_params.append(("start", local_var_params["start"]))  # noqa: E501
        if (
            "end" in local_var_params and local_var_params["end"] is not None
        ):  # noqa: E501
            query_params.append(("end", local_var_params["end"]))  # noqa: E501
        if (
            "page" in local_var_params and local_var_params["page"] is not None
        ):  # noqa: E501
            query_params.append(("page", local_var_params["page"]))  # noqa: E501
        if (
            "per_page" in local_var_params and local_var_params["per_page"] is not None
        ):  # noqa: E501
            query_params.append(
                ("per_page", local_var_params["per_page"])
            )  # noqa: E501
        if (
            "type" in local_var_params and local_var_params["type"] is not None
        ):  # noqa: E501
            query_params.append(("type", local_var_params["type"]))  # noqa: E501
        if (
            "status" in local_var_params and local_var_params["status"] is not None
        ):  # noqa: E501
            query_params.append(("status", local_var_params["status"]))  # noqa: E501
        if (
            "orderby" in local_var_params and local_var_params["orderby"] is not None
        ):  # noqa: E501
            query_params.append(("orderby", local_var_params["orderby"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["ApiKeyAuth", "BasicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/invitations",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InvitationData",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def join_organization(self, organization, email_invite, **kwargs):  # noqa: E501
        """join_organization  # noqa: E501

        Sends email to multiple recipients with joining information regarding an organization  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.join_organization(organization, email_invite, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization: name or uuid of organization (required)
        :param InvitationOrganizationJoinEmail email_invite: list of email recipients (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.join_organization_with_http_info(
            organization, email_invite, **kwargs
        )  # noqa: E501

    def join_organization_with_http_info(
        self, organization, email_invite, **kwargs
    ):  # noqa: E501
        """join_organization  # noqa: E501

        Sends email to multiple recipients with joining information regarding an organization  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.join_organization_with_http_info(organization, email_invite, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization: name or uuid of organization (required)
        :param InvitationOrganizationJoinEmail email_invite: list of email recipients (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["organization", "email_invite"]
        all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
            ]
        )

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method join_organization" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'organization' is set
        if self.api_client.client_side_validation and (
            "organization" not in local_var_params
            or local_var_params["organization"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `organization` when calling `join_organization`"
            )  # noqa: E501
        # verify the required parameter 'email_invite' is set
        if self.api_client.client_side_validation and (
            "email_invite" not in local_var_params
            or local_var_params["email_invite"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `email_invite` when calling `join_organization`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "organization" in local_var_params:
            path_params["organization"] = local_var_params["organization"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "email_invite" in local_var_params:
            body_params = local_var_params["email_invite"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["ApiKeyAuth", "BasicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/invitations/{organization}/join",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def share_array_by_invite(
        self, namespace, array, email_invite, **kwargs
    ):  # noqa: E501
        """share_array_by_invite  # noqa: E501

        Sends email to multiple recipients with sharing information regarding an array  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.share_array_by_invite(namespace, array, email_invite, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str namespace: namespace array is in (an organization name or user's username) (required)
        :param str array: name/uri of array that is url-encoded (required)
        :param InvitationArrayShareEmail email_invite: list of email recipients (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.share_array_by_invite_with_http_info(
            namespace, array, email_invite, **kwargs
        )  # noqa: E501

    def share_array_by_invite_with_http_info(
        self, namespace, array, email_invite, **kwargs
    ):  # noqa: E501
        """share_array_by_invite  # noqa: E501

        Sends email to multiple recipients with sharing information regarding an array  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.share_array_by_invite_with_http_info(namespace, array, email_invite, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str namespace: namespace array is in (an organization name or user's username) (required)
        :param str array: name/uri of array that is url-encoded (required)
        :param InvitationArrayShareEmail email_invite: list of email recipients (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["namespace", "array", "email_invite"]
        all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
            ]
        )

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method share_array_by_invite" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'namespace' is set
        if self.api_client.client_side_validation and (
            "namespace" not in local_var_params
            or local_var_params["namespace"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `namespace` when calling `share_array_by_invite`"
            )  # noqa: E501
        # verify the required parameter 'array' is set
        if self.api_client.client_side_validation and (
            "array" not in local_var_params
            or local_var_params["array"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `array` when calling `share_array_by_invite`"
            )  # noqa: E501
        # verify the required parameter 'email_invite' is set
        if self.api_client.client_side_validation and (
            "email_invite" not in local_var_params
            or local_var_params["email_invite"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `email_invite` when calling `share_array_by_invite`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "namespace" in local_var_params:
            path_params["namespace"] = local_var_params["namespace"]  # noqa: E501
        if "array" in local_var_params:
            path_params["array"] = local_var_params["array"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "email_invite" in local_var_params:
            body_params = local_var_params["email_invite"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["ApiKeyAuth", "BasicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/invitations/{namespace}/{array}/share",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
