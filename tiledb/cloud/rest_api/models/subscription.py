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


class Subscription(object):
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
        "id": "str",
        "owner_namespace_uuid": "str",
        "customer_namespace_uuid": "str",
        "pricing": "list[Pricing]",
    }

    attribute_map = {
        "id": "id",
        "owner_namespace_uuid": "owner_namespace_uuid",
        "customer_namespace_uuid": "customer_namespace_uuid",
        "pricing": "pricing",
    }

    def __init__(
        self,
        id=None,
        owner_namespace_uuid=None,
        customer_namespace_uuid=None,
        pricing=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """Subscription - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._owner_namespace_uuid = None
        self._customer_namespace_uuid = None
        self._pricing = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if owner_namespace_uuid is not None:
            self.owner_namespace_uuid = owner_namespace_uuid
        if customer_namespace_uuid is not None:
            self.customer_namespace_uuid = customer_namespace_uuid
        if pricing is not None:
            self.pricing = pricing

    @property
    def id(self):
        """Gets the id of this Subscription.  # noqa: E501

        Unique id of subscription as defined by Stripe  # noqa: E501

        :return: The id of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Subscription.

        Unique id of subscription as defined by Stripe  # noqa: E501

        :param id: The id of this Subscription.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def owner_namespace_uuid(self):
        """Gets the owner_namespace_uuid of this Subscription.  # noqa: E501

        Unique id of the array (product) owner  # noqa: E501

        :return: The owner_namespace_uuid of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._owner_namespace_uuid

    @owner_namespace_uuid.setter
    def owner_namespace_uuid(self, owner_namespace_uuid):
        """Sets the owner_namespace_uuid of this Subscription.

        Unique id of the array (product) owner  # noqa: E501

        :param owner_namespace_uuid: The owner_namespace_uuid of this Subscription.  # noqa: E501
        :type: str
        """

        self._owner_namespace_uuid = owner_namespace_uuid

    @property
    def customer_namespace_uuid(self):
        """Gets the customer_namespace_uuid of this Subscription.  # noqa: E501

        Unique id of the array (product) user (customer)  # noqa: E501

        :return: The customer_namespace_uuid of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._customer_namespace_uuid

    @customer_namespace_uuid.setter
    def customer_namespace_uuid(self, customer_namespace_uuid):
        """Sets the customer_namespace_uuid of this Subscription.

        Unique id of the array (product) user (customer)  # noqa: E501

        :param customer_namespace_uuid: The customer_namespace_uuid of this Subscription.  # noqa: E501
        :type: str
        """

        self._customer_namespace_uuid = customer_namespace_uuid

    @property
    def pricing(self):
        """Gets the pricing of this Subscription.  # noqa: E501

        list of pricing used by this subscription  # noqa: E501

        :return: The pricing of this Subscription.  # noqa: E501
        :rtype: list[Pricing]
        """
        return self._pricing

    @pricing.setter
    def pricing(self, pricing):
        """Sets the pricing of this Subscription.

        list of pricing used by this subscription  # noqa: E501

        :param pricing: The pricing of this Subscription.  # noqa: E501
        :type: list[Pricing]
        """

        self._pricing = pricing

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
        if not isinstance(other, Subscription):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Subscription):
            return True

        return self.to_dict() != other.to_dict()
