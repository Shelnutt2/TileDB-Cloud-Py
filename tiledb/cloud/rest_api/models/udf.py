# coding: utf-8

"""
    TileDB Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 1.5.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class UDF(object):
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
        "language": "UDFLanguage",
        "version": "str",
        "image_name": "str",
        "subarray": "UDFSubarray",
        "_exec": "str",
        "buffers": "list[str]",
    }

    attribute_map = {
        "language": "language",
        "version": "version",
        "image_name": "image_name",
        "subarray": "subarray",
        "_exec": "exec",
        "buffers": "buffers",
    }

    def __init__(
        self,
        language=None,
        version=None,
        image_name=None,
        subarray=None,
        _exec=None,
        buffers=None,
    ):  # noqa: E501
        """UDF - a model defined in OpenAPI"""  # noqa: E501

        self._language = None
        self._version = None
        self._image_name = None
        self._subarray = None
        self.__exec = None
        self._buffers = None
        self.discriminator = None

        if language is not None:
            self.language = language
        if version is not None:
            self.version = version
        if image_name is not None:
            self.image_name = image_name
        if subarray is not None:
            self.subarray = subarray
        if _exec is not None:
            self._exec = _exec
        if buffers is not None:
            self.buffers = buffers

    @property
    def language(self):
        """Gets the language of this UDF.  # noqa: E501


        :return: The language of this UDF.  # noqa: E501
        :rtype: UDFLanguage
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this UDF.


        :param language: The language of this UDF.  # noqa: E501
        :type: UDFLanguage
        """

        self._language = language

    @property
    def version(self):
        """Gets the version of this UDF.  # noqa: E501

        Type-specific version  # noqa: E501

        :return: The version of this UDF.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this UDF.

        Type-specific version  # noqa: E501

        :param version: The version of this UDF.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def image_name(self):
        """Gets the image_name of this UDF.  # noqa: E501

        Docker image name to use for udf  # noqa: E501

        :return: The image_name of this UDF.  # noqa: E501
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this UDF.

        Docker image name to use for udf  # noqa: E501

        :param image_name: The image_name of this UDF.  # noqa: E501
        :type: str
        """

        self._image_name = image_name

    @property
    def subarray(self):
        """Gets the subarray of this UDF.  # noqa: E501


        :return: The subarray of this UDF.  # noqa: E501
        :rtype: UDFSubarray
        """
        return self._subarray

    @subarray.setter
    def subarray(self, subarray):
        """Sets the subarray of this UDF.


        :param subarray: The subarray of this UDF.  # noqa: E501
        :type: UDFSubarray
        """

        self._subarray = subarray

    @property
    def _exec(self):
        """Gets the _exec of this UDF.  # noqa: E501

        Type-specific executable text  # noqa: E501

        :return: The _exec of this UDF.  # noqa: E501
        :rtype: str
        """
        return self.__exec

    @_exec.setter
    def _exec(self, _exec):
        """Sets the _exec of this UDF.

        Type-specific executable text  # noqa: E501

        :param _exec: The _exec of this UDF.  # noqa: E501
        :type: str
        """

        self.__exec = _exec

    @property
    def buffers(self):
        """Gets the buffers of this UDF.  # noqa: E501

        List of buffers to fetch (attributes + coordinates)  # noqa: E501

        :return: The buffers of this UDF.  # noqa: E501
        :rtype: list[str]
        """
        return self._buffers

    @buffers.setter
    def buffers(self, buffers):
        """Sets the buffers of this UDF.

        List of buffers to fetch (attributes + coordinates)  # noqa: E501

        :param buffers: The buffers of this UDF.  # noqa: E501
        :type: list[str]
        """

        self._buffers = buffers

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
        if not isinstance(other, UDF):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
