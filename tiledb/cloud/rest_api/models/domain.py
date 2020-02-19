# coding: utf-8

"""
    TileDB Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 1.5.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Domain(object):
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
        "type": "Datatype",
        "tile_order": "Layout",
        "cell_order": "Layout",
        "dimensions": "list[Dimension]",
    }

    attribute_map = {
        "type": "type",
        "tile_order": "tileOrder",
        "cell_order": "cellOrder",
        "dimensions": "dimensions",
    }

    def __init__(
        self, type=None, tile_order=None, cell_order=None, dimensions=None
    ):  # noqa: E501
        """Domain - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._tile_order = None
        self._cell_order = None
        self._dimensions = None
        self.discriminator = None

        self.type = type
        self.tile_order = tile_order
        self.cell_order = cell_order
        self.dimensions = dimensions

    @property
    def type(self):
        """Gets the type of this Domain.  # noqa: E501


        :return: The type of this Domain.  # noqa: E501
        :rtype: Datatype
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Domain.


        :param type: The type of this Domain.  # noqa: E501
        :type: Datatype
        """
        if type is None:
            raise ValueError(
                "Invalid value for `type`, must not be `None`"
            )  # noqa: E501

        self._type = type

    @property
    def tile_order(self):
        """Gets the tile_order of this Domain.  # noqa: E501


        :return: The tile_order of this Domain.  # noqa: E501
        :rtype: Layout
        """
        return self._tile_order

    @tile_order.setter
    def tile_order(self, tile_order):
        """Sets the tile_order of this Domain.


        :param tile_order: The tile_order of this Domain.  # noqa: E501
        :type: Layout
        """
        if tile_order is None:
            raise ValueError(
                "Invalid value for `tile_order`, must not be `None`"
            )  # noqa: E501

        self._tile_order = tile_order

    @property
    def cell_order(self):
        """Gets the cell_order of this Domain.  # noqa: E501


        :return: The cell_order of this Domain.  # noqa: E501
        :rtype: Layout
        """
        return self._cell_order

    @cell_order.setter
    def cell_order(self, cell_order):
        """Sets the cell_order of this Domain.


        :param cell_order: The cell_order of this Domain.  # noqa: E501
        :type: Layout
        """
        if cell_order is None:
            raise ValueError(
                "Invalid value for `cell_order`, must not be `None`"
            )  # noqa: E501

        self._cell_order = cell_order

    @property
    def dimensions(self):
        """Gets the dimensions of this Domain.  # noqa: E501

        Array of dimensions  # noqa: E501

        :return: The dimensions of this Domain.  # noqa: E501
        :rtype: list[Dimension]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this Domain.

        Array of dimensions  # noqa: E501

        :param dimensions: The dimensions of this Domain.  # noqa: E501
        :type: list[Dimension]
        """
        if dimensions is None:
            raise ValueError(
                "Invalid value for `dimensions`, must not be `None`"
            )  # noqa: E501

        self._dimensions = dimensions

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
        if not isinstance(other, Domain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
