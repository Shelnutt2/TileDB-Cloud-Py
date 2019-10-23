# coding: utf-8

"""
    TileDB Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 0.3.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class AttributeBufferSize(object):
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
        'attribute': 'str',
        'offset_bytes': 'int',
        'data_bytes': 'int'
    }

    attribute_map = {
        'attribute': 'attribute',
        'offset_bytes': 'offsetBytes',
        'data_bytes': 'dataBytes'
    }

    def __init__(self, attribute=None, offset_bytes=None, data_bytes=None):  # noqa: E501
        """AttributeBufferSize - a model defined in OpenAPI"""  # noqa: E501

        self._attribute = None
        self._offset_bytes = None
        self._data_bytes = None
        self.discriminator = None

        self.attribute = attribute
        self.offset_bytes = offset_bytes
        self.data_bytes = data_bytes

    @property
    def attribute(self):
        """Gets the attribute of this AttributeBufferSize.  # noqa: E501

        name of attribute  # noqa: E501

        :return: The attribute of this AttributeBufferSize.  # noqa: E501
        :rtype: str
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        """Sets the attribute of this AttributeBufferSize.

        name of attribute  # noqa: E501

        :param attribute: The attribute of this AttributeBufferSize.  # noqa: E501
        :type: str
        """
        if attribute is None:
            raise ValueError("Invalid value for `attribute`, must not be `None`")  # noqa: E501

        self._attribute = attribute

    @property
    def offset_bytes(self):
        """Gets the offset_bytes of this AttributeBufferSize.  # noqa: E501

        buffer size (in bytes) of offset buffer  # noqa: E501

        :return: The offset_bytes of this AttributeBufferSize.  # noqa: E501
        :rtype: int
        """
        return self._offset_bytes

    @offset_bytes.setter
    def offset_bytes(self, offset_bytes):
        """Sets the offset_bytes of this AttributeBufferSize.

        buffer size (in bytes) of offset buffer  # noqa: E501

        :param offset_bytes: The offset_bytes of this AttributeBufferSize.  # noqa: E501
        :type: int
        """
        if offset_bytes is None:
            raise ValueError("Invalid value for `offset_bytes`, must not be `None`")  # noqa: E501

        self._offset_bytes = offset_bytes

    @property
    def data_bytes(self):
        """Gets the data_bytes of this AttributeBufferSize.  # noqa: E501

        buffer size (in bytes) of data buffer  # noqa: E501

        :return: The data_bytes of this AttributeBufferSize.  # noqa: E501
        :rtype: int
        """
        return self._data_bytes

    @data_bytes.setter
    def data_bytes(self, data_bytes):
        """Sets the data_bytes of this AttributeBufferSize.

        buffer size (in bytes) of data buffer  # noqa: E501

        :param data_bytes: The data_bytes of this AttributeBufferSize.  # noqa: E501
        :type: int
        """
        if data_bytes is None:
            raise ValueError("Invalid value for `data_bytes`, must not be `None`")  # noqa: E501

        self._data_bytes = data_bytes

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
        if not isinstance(other, AttributeBufferSize):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
