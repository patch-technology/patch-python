# coding: utf-8

"""
    Patch API V1

    The core API used to integrate with Patch's service  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: engineering@usepatch.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from patch_api.configuration import Configuration


class Estimate(object):
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
        "production": "bool",
        "type": "str",
        "mass_g": "int",
        "order": "Order",
    }

    attribute_map = {
        "id": "id",
        "production": "production",
        "type": "type",
        "mass_g": "mass_g",
        "order": "order",
    }

    def __init__(
        self,
        id=None,
        production=None,
        type=None,
        mass_g=None,
        order=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """Estimate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._production = None
        self._type = None
        self._mass_g = None
        self._order = None
        self.discriminator = None

        self.id = id
        self.production = production
        self.type = type
        if mass_g is not None:
            self.mass_g = mass_g
        self.order = order

    @property
    def id(self):
        """Gets the id of this Estimate.  # noqa: E501

        A unique uid for the record. UIDs will be prepended by est_prod or est_test depending on the mode it was created in.  # noqa: E501

        :return: The id of this Estimate.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Estimate.

        A unique uid for the record. UIDs will be prepended by est_prod or est_test depending on the mode it was created in.  # noqa: E501

        :param id: The id of this Estimate.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and id is None
        ):  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def production(self):
        """Gets the production of this Estimate.  # noqa: E501

        A boolean indicating if this estimate is a production or demo mode estimate.  # noqa: E501

        :return: The production of this Estimate.  # noqa: E501
        :rtype: bool
        """
        return self._production

    @production.setter
    def production(self, production):
        """Sets the production of this Estimate.

        A boolean indicating if this estimate is a production or demo mode estimate.  # noqa: E501

        :param production: The production of this Estimate.  # noqa: E501
        :type: bool
        """
        if (
            self.local_vars_configuration.client_side_validation and production is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `production`, must not be `None`"
            )  # noqa: E501

        self._production = production

    @property
    def type(self):
        """Gets the type of this Estimate.  # noqa: E501

        The type of estimate. Available types are mass, flight, shipping, vehicle, and crypto.  # noqa: E501

        :return: The type of this Estimate.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Estimate.

        The type of estimate. Available types are mass, flight, shipping, vehicle, and crypto.  # noqa: E501

        :param type: The type of this Estimate.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and type is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `type`, must not be `None`"
            )  # noqa: E501

        self._type = type

    @property
    def mass_g(self):
        """Gets the mass_g of this Estimate.  # noqa: E501

        The estimated mass in grams for this estimate.  # noqa: E501

        :return: The mass_g of this Estimate.  # noqa: E501
        :rtype: int
        """
        return self._mass_g

    @mass_g.setter
    def mass_g(self, mass_g):
        """Sets the mass_g of this Estimate.

        The estimated mass in grams for this estimate.  # noqa: E501

        :param mass_g: The mass_g of this Estimate.  # noqa: E501
        :type: int
        """

        self._mass_g = mass_g

    @property
    def order(self):
        """Gets the order of this Estimate.  # noqa: E501

        An object returning the order associated with this estimate. See the [Order section](/?id=orders) for the full schema.  # noqa: E501

        :return: The order of this Estimate.  # noqa: E501
        :rtype: Order
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this Estimate.

        An object returning the order associated with this estimate. See the [Order section](/?id=orders) for the full schema.  # noqa: E501

        :param order: The order of this Estimate.  # noqa: E501
        :type: Order
        """

        self._order = order

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
        if not isinstance(other, Estimate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Estimate):
            return True

        return self.to_dict() != other.to_dict()
