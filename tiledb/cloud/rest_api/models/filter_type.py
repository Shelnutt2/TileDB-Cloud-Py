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


class FilterType(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    NONE = "FILTER_NONE"
    GZIP = "FILTER_GZIP"
    ZSTD = "FILTER_ZSTD"
    LZ4 = "FILTER_LZ4"
    RLE = "FILTER_RLE"
    BZIP2 = "FILTER_BZIP2"
    DOUBLE_DELTA = "FILTER_DOUBLE_DELTA"
    BIT_WIDTH_REDUCTION = "FILTER_BIT_WIDTH_REDUCTION"
    BITSHUFFLE = "FILTER_BITSHUFFLE"
    BYTESHUFFLE = "FILTER_BYTESHUFFLE"
    POSITIVE_DELTA = "FILTER_POSITIVE_DELTA"

    allowable_values = [
        NONE,
        GZIP,
        ZSTD,
        LZ4,
        RLE,
        BZIP2,
        DOUBLE_DELTA,
        BIT_WIDTH_REDUCTION,
        BITSHUFFLE,
        BYTESHUFFLE,
        POSITIVE_DELTA,
    ]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {}

    attribute_map = {}

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """FilterType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
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
        if not isinstance(other, FilterType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FilterType):
            return True

        return self.to_dict() != other.to_dict()
