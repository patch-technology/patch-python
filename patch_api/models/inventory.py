# coding: utf-8

"""
    Patch API V2

    The core API used to integrate with Patch's service  # noqa: E501

    The version of the OpenAPI document: 2.1.0
    Contact: engineering@usepatch.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from patch_api.configuration import Configuration


class Inventory(object):
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
        "vintage_year": "int",
        "vintage_start_year": "int",
        "vintage_end_year": "int",
        "amount_available": "int",
        "price": "int",
        "currency": "str",
        "unit": "str",
    }

    attribute_map = {
        "vintage_year": "vintage_year",
        "vintage_start_year": "vintage_start_year",
        "vintage_end_year": "vintage_end_year",
        "amount_available": "amount_available",
        "price": "price",
        "currency": "currency",
        "unit": "unit",
    }

    def __init__(
        self,
        vintage_year=None,
        vintage_start_year=None,
        vintage_end_year=None,
        amount_available=None,
        price=None,
        currency=None,
        unit=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """Inventory - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._vintage_year = None
        self._vintage_start_year = None
        self._vintage_end_year = None
        self._amount_available = None
        self._price = None
        self._currency = None
        self._unit = None
        self.discriminator = None

        self.vintage_year = vintage_year
        self.vintage_start_year = vintage_start_year
        self.vintage_end_year = vintage_end_year
        self.amount_available = amount_available
        self.price = price
        self.currency = currency
        self.unit = unit

    @property
    def vintage_year(self):
        """Gets the vintage_year of this Inventory.  # noqa: E501

        The year in which the climate impacts of the project occurred, or will occur.  # noqa: E501

        :return: The vintage_year of this Inventory.  # noqa: E501
        :rtype: int
        """
        return self._vintage_year

    @vintage_year.setter
    def vintage_year(self, vintage_year):
        """Sets the vintage_year of this Inventory.

        The year in which the climate impacts of the project occurred, or will occur.  # noqa: E501

        :param vintage_year: The vintage_year of this Inventory.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and vintage_year is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `vintage_year`, must not be `None`"
            )  # noqa: E501

        self._vintage_year = vintage_year

    @property
    def vintage_start_year(self):
        """Gets the vintage_start_year of this Inventory.  # noqa: E501

        The starting year in which the climate impacts of the project occurred, or will occur.  # noqa: E501

        :return: The vintage_start_year of this Inventory.  # noqa: E501
        :rtype: int
        """
        return self._vintage_start_year

    @vintage_start_year.setter
    def vintage_start_year(self, vintage_start_year):
        """Sets the vintage_start_year of this Inventory.

        The starting year in which the climate impacts of the project occurred, or will occur.  # noqa: E501

        :param vintage_start_year: The vintage_start_year of this Inventory.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and vintage_start_year is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `vintage_start_year`, must not be `None`"
            )  # noqa: E501

        self._vintage_start_year = vintage_start_year

    @property
    def vintage_end_year(self):
        """Gets the vintage_end_year of this Inventory.  # noqa: E501

        The ending year in which the climate impacts of the project occurred, or will occur.  # noqa: E501

        :return: The vintage_end_year of this Inventory.  # noqa: E501
        :rtype: int
        """
        return self._vintage_end_year

    @vintage_end_year.setter
    def vintage_end_year(self, vintage_end_year):
        """Sets the vintage_end_year of this Inventory.

        The ending year in which the climate impacts of the project occurred, or will occur.  # noqa: E501

        :param vintage_end_year: The vintage_end_year of this Inventory.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and vintage_end_year is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `vintage_end_year`, must not be `None`"
            )  # noqa: E501

        self._vintage_end_year = vintage_end_year

    @property
    def amount_available(self):
        """Gets the amount_available of this Inventory.  # noqa: E501

        The amount available for this vintage year.  # noqa: E501

        :return: The amount_available of this Inventory.  # noqa: E501
        :rtype: int
        """
        return self._amount_available

    @amount_available.setter
    def amount_available(self, amount_available):
        """Sets the amount_available of this Inventory.

        The amount available for this vintage year.  # noqa: E501

        :param amount_available: The amount_available of this Inventory.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and amount_available is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `amount_available`, must not be `None`"
            )  # noqa: E501

        self._amount_available = amount_available

    @property
    def price(self):
        """Gets the price of this Inventory.  # noqa: E501

        The price per tonne (1,000,000 g) or MWh (1,000,000 Wh) of inventory. Prices are always represented in the smallest currency unit (ie cents for USD).  # noqa: E501

        :return: The price of this Inventory.  # noqa: E501
        :rtype: int
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Inventory.

        The price per tonne (1,000,000 g) or MWh (1,000,000 Wh) of inventory. Prices are always represented in the smallest currency unit (ie cents for USD).  # noqa: E501

        :param price: The price of this Inventory.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation and price is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `price`, must not be `None`"
            )  # noqa: E501

        self._price = price

    @property
    def currency(self):
        """Gets the currency of this Inventory.  # noqa: E501

        The currency code for `price`.  # noqa: E501

        :return: The currency of this Inventory.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Inventory.

        The currency code for `price`.  # noqa: E501

        :param currency: The currency of this Inventory.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and currency is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `currency`, must not be `None`"
            )  # noqa: E501

        self._currency = currency

    @property
    def unit(self):
        """Gets the unit of this Inventory.  # noqa: E501

        The unit of measurement (ie \"g\" or \"Wh\") for `amount_available`.  # noqa: E501

        :return: The unit of this Inventory.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Inventory.

        The unit of measurement (ie \"g\" or \"Wh\") for `amount_available`.  # noqa: E501

        :param unit: The unit of this Inventory.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and unit is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `unit`, must not be `None`"
            )  # noqa: E501

        self._unit = unit

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
        if not isinstance(other, Inventory):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Inventory):
            return True

        return self.to_dict() != other.to_dict()
