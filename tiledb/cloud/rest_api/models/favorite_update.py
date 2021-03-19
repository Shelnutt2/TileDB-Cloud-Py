# coding: utf-8

"""
    TileDB Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 2.2.19
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from tiledb.cloud.rest_api.configuration import Configuration


class FavoriteUpdate(object):
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
    openapi_types = {"name": "str", "namespace": "str", "object_type": "FavoriteType"}

    attribute_map = {
        "name": "name",
        "namespace": "namespace",
        "object_type": "object_type",
    }

    def __init__(
        self, name=None, namespace=None, object_type=None, local_vars_configuration=None
    ):  # noqa: E501
        """FavoriteUpdate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._namespace = None
        self._object_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if object_type is not None:
            self.object_type = object_type

    @property
    def name(self):
        """Gets the name of this FavoriteUpdate.  # noqa: E501


        :return: The name of this FavoriteUpdate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FavoriteUpdate.


        :param name: The name of this FavoriteUpdate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this FavoriteUpdate.  # noqa: E501


        :return: The namespace of this FavoriteUpdate.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this FavoriteUpdate.


        :param namespace: The namespace of this FavoriteUpdate.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def object_type(self):
        """Gets the object_type of this FavoriteUpdate.  # noqa: E501


        :return: The object_type of this FavoriteUpdate.  # noqa: E501
        :rtype: FavoriteType
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this FavoriteUpdate.


        :param object_type: The object_type of this FavoriteUpdate.  # noqa: E501
        :type: FavoriteType
        """

        self._object_type = object_type

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
        if not isinstance(other, FavoriteUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FavoriteUpdate):
            return True

        return self.to_dict() != other.to_dict()
