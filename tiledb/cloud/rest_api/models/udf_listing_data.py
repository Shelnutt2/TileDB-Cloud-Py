# coding: utf-8

"""
    TileDB Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 2.1.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from tiledb.cloud.rest_api.configuration import Configuration


class UDFListingData(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'udf_info_list': 'list[UDFInfo]',
        'pagination_metadata': 'PaginationMetadata'
    }

    attribute_map = {
        'udf_info_list': 'udf_info_list',
        'pagination_metadata': 'pagination_metadata'
    }

    def __init__(self, udf_info_list=None, pagination_metadata=None, local_vars_configuration=None):  # noqa: E501
        """UDFListingData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._udf_info_list = None
        self._pagination_metadata = None
        self.discriminator = None

        if udf_info_list is not None:
            self.udf_info_list = udf_info_list
        if pagination_metadata is not None:
            self.pagination_metadata = pagination_metadata

    @property
    def udf_info_list(self):
        """Gets the udf_info_list of this UDFListingData.  # noqa: E501

        List of UDFInfo  # noqa: E501

        :return: The udf_info_list of this UDFListingData.  # noqa: E501
        :rtype: list[UDFInfo]
        """
        return self._udf_info_list

    @udf_info_list.setter
    def udf_info_list(self, udf_info_list):
        """Sets the udf_info_list of this UDFListingData.

        List of UDFInfo  # noqa: E501

        :param udf_info_list: The udf_info_list of this UDFListingData.  # noqa: E501
        :type: list[UDFInfo]
        """

        self._udf_info_list = udf_info_list

    @property
    def pagination_metadata(self):
        """Gets the pagination_metadata of this UDFListingData.  # noqa: E501


        :return: The pagination_metadata of this UDFListingData.  # noqa: E501
        :rtype: PaginationMetadata
        """
        return self._pagination_metadata

    @pagination_metadata.setter
    def pagination_metadata(self, pagination_metadata):
        """Sets the pagination_metadata of this UDFListingData.


        :param pagination_metadata: The pagination_metadata of this UDFListingData.  # noqa: E501
        :type: PaginationMetadata
        """

        self._pagination_metadata = pagination_metadata

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UDFListingData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UDFListingData):
            return True

        return self.to_dict() != other.to_dict()
