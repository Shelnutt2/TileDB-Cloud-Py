# coding: utf-8

"""
    TileDB Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 0.6.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class UDFSubarrayRange(object):
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
        'dimension_id': 'int',
        'range_start': 'DimensionCoordinate',
        'range_end': 'DimensionCoordinate'
    }

    attribute_map = {
        'dimension_id': 'dimension_id',
        'range_start': 'range_start',
        'range_end': 'range_end'
    }

    def __init__(self, dimension_id=None, range_start=None, range_end=None):  # noqa: E501
        """UDFSubarrayRange - a model defined in OpenAPI"""  # noqa: E501

        self._dimension_id = None
        self._range_start = None
        self._range_end = None
        self.discriminator = None

        if dimension_id is not None:
            self.dimension_id = dimension_id
        if range_start is not None:
            self.range_start = range_start
        if range_end is not None:
            self.range_end = range_end

    @property
    def dimension_id(self):
        """Gets the dimension_id of this UDFSubarrayRange.  # noqa: E501

        The dimension index  # noqa: E501

        :return: The dimension_id of this UDFSubarrayRange.  # noqa: E501
        :rtype: int
        """
        return self._dimension_id

    @dimension_id.setter
    def dimension_id(self, dimension_id):
        """Sets the dimension_id of this UDFSubarrayRange.

        The dimension index  # noqa: E501

        :param dimension_id: The dimension_id of this UDFSubarrayRange.  # noqa: E501
        :type: int
        """

        self._dimension_id = dimension_id

    @property
    def range_start(self):
        """Gets the range_start of this UDFSubarrayRange.  # noqa: E501


        :return: The range_start of this UDFSubarrayRange.  # noqa: E501
        :rtype: DimensionCoordinate
        """
        return self._range_start

    @range_start.setter
    def range_start(self, range_start):
        """Sets the range_start of this UDFSubarrayRange.


        :param range_start: The range_start of this UDFSubarrayRange.  # noqa: E501
        :type: DimensionCoordinate
        """

        self._range_start = range_start

    @property
    def range_end(self):
        """Gets the range_end of this UDFSubarrayRange.  # noqa: E501


        :return: The range_end of this UDFSubarrayRange.  # noqa: E501
        :rtype: DimensionCoordinate
        """
        return self._range_end

    @range_end.setter
    def range_end(self, range_end):
        """Sets the range_end of this UDFSubarrayRange.


        :param range_end: The range_end of this UDFSubarrayRange.  # noqa: E501
        :type: DimensionCoordinate
        """

        self._range_end = range_end

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
        if not isinstance(other, UDFSubarrayRange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
