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


class Allocation(object):
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
    openapi_types = {"id": "str", "production": "bool", "mass_g": "int"}

    attribute_map = {"id": "id", "production": "production", "mass_g": "mass_g"}

    def __init__(
        self, id=None, production=None, mass_g=None, local_vars_configuration=None
    ):  # noqa: E501
        """Allocation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._production = None
        self._mass_g = None
        self.discriminator = None

        self.id = id
        self.production = production
        self.mass_g = mass_g

    @property
    def id(self):
        """Gets the id of this Allocation.  # noqa: E501

        A unique uid for the record. UIDs will be prepended by all_prod or all_test depending on the mode it was created in.  # noqa: E501

        :return: The id of this Allocation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Allocation.

        A unique uid for the record. UIDs will be prepended by all_prod or all_test depending on the mode it was created in.  # noqa: E501

        :param id: The id of this Allocation.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and id is None
        ):  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def production(self):
        """Gets the production of this Allocation.  # noqa: E501

        A boolean indicating if this project is a production or test mode project.  # noqa: E501

        :return: The production of this Allocation.  # noqa: E501
        :rtype: bool
        """
        return self._production

    @production.setter
    def production(self, production):
        """Sets the production of this Allocation.

        A boolean indicating if this project is a production or test mode project.  # noqa: E501

        :param production: The production of this Allocation.  # noqa: E501
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
    def mass_g(self):
        """Gets the mass_g of this Allocation.  # noqa: E501

        The amount (in grams) of allocated carbon offsets.  # noqa: E501

        :return: The mass_g of this Allocation.  # noqa: E501
        :rtype: int
        """
        return self._mass_g

    @mass_g.setter
    def mass_g(self, mass_g):
        """Sets the mass_g of this Allocation.

        The amount (in grams) of allocated carbon offsets.  # noqa: E501

        :param mass_g: The mass_g of this Allocation.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation and mass_g is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `mass_g`, must not be `None`"
            )  # noqa: E501

        self._mass_g = mass_g

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
        if not isinstance(other, Allocation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Allocation):
            return True

        return self.to_dict() != other.to_dict()
