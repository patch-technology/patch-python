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


class OrderLineItem(object):
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
        "project": "OrderLineItemProject",
        "vintage_year": "int",
        "vintage_start_year": "int",
        "vintage_end_year": "int",
        "amount": "int",
        "unit": "str",
        "price": "int",
        "currency": "str",
    }

    attribute_map = {
        "id": "id",
        "project": "project",
        "vintage_year": "vintage_year",
        "vintage_start_year": "vintage_start_year",
        "vintage_end_year": "vintage_end_year",
        "amount": "amount",
        "unit": "unit",
        "price": "price",
        "currency": "currency",
    }

    def __init__(
        self,
        id=None,
        project=None,
        vintage_year=None,
        vintage_start_year=None,
        vintage_end_year=None,
        amount=None,
        unit=None,
        price=None,
        currency=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """OrderLineItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._project = None
        self._vintage_year = None
        self._vintage_start_year = None
        self._vintage_end_year = None
        self._amount = None
        self._unit = None
        self._price = None
        self._currency = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.project = project
        self.vintage_year = vintage_year
        self.vintage_start_year = vintage_start_year
        self.vintage_end_year = vintage_end_year
        self.amount = amount
        self.unit = unit
        self.price = price
        self.currency = currency

    @property
    def id(self):
        """Gets the id of this OrderLineItem.  # noqa: E501

        The identifier for this order line item  # noqa: E501

        :return: The id of this OrderLineItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrderLineItem.

        The identifier for this order line item  # noqa: E501

        :param id: The id of this OrderLineItem.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def project(self):
        """Gets the project of this OrderLineItem.  # noqa: E501

        An object containing information about the project associated with the inventory allocated.  # noqa: E501

        :return: The project of this OrderLineItem.  # noqa: E501
        :rtype: OrderLineItemProject
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this OrderLineItem.

        An object containing information about the project associated with the inventory allocated.  # noqa: E501

        :param project: The project of this OrderLineItem.  # noqa: E501
        :type: OrderLineItemProject
        """
        if (
            self.local_vars_configuration.client_side_validation and project is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `project`, must not be `None`"
            )  # noqa: E501

        self._project = project

    @property
    def vintage_year(self):
        """Gets the vintage_year of this OrderLineItem.  # noqa: E501

        The year in which the climate impacts of the project occurred, or will occur.  # noqa: E501

        :return: The vintage_year of this OrderLineItem.  # noqa: E501
        :rtype: int
        """
        return self._vintage_year

    @vintage_year.setter
    def vintage_year(self, vintage_year):
        """Sets the vintage_year of this OrderLineItem.

        The year in which the climate impacts of the project occurred, or will occur.  # noqa: E501

        :param vintage_year: The vintage_year of this OrderLineItem.  # noqa: E501
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
        """Gets the vintage_start_year of this OrderLineItem.  # noqa: E501

        The starting_year in which the climate impacts of the project occurred, or will occur.  # noqa: E501

        :return: The vintage_start_year of this OrderLineItem.  # noqa: E501
        :rtype: int
        """
        return self._vintage_start_year

    @vintage_start_year.setter
    def vintage_start_year(self, vintage_start_year):
        """Sets the vintage_start_year of this OrderLineItem.

        The starting_year in which the climate impacts of the project occurred, or will occur.  # noqa: E501

        :param vintage_start_year: The vintage_start_year of this OrderLineItem.  # noqa: E501
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
        """Gets the vintage_end_year of this OrderLineItem.  # noqa: E501

        The ending year in which the climate impacts of the project occurred, or will occur.  # noqa: E501

        :return: The vintage_end_year of this OrderLineItem.  # noqa: E501
        :rtype: int
        """
        return self._vintage_end_year

    @vintage_end_year.setter
    def vintage_end_year(self, vintage_end_year):
        """Sets the vintage_end_year of this OrderLineItem.

        The ending year in which the climate impacts of the project occurred, or will occur.  # noqa: E501

        :param vintage_end_year: The vintage_end_year of this OrderLineItem.  # noqa: E501
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
    def amount(self):
        """Gets the amount of this OrderLineItem.  # noqa: E501

        The amount ordered for the given project and vintage year.  # noqa: E501

        :return: The amount of this OrderLineItem.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this OrderLineItem.

        The amount ordered for the given project and vintage year.  # noqa: E501

        :param amount: The amount of this OrderLineItem.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation and amount is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `amount`, must not be `None`"
            )  # noqa: E501

        self._amount = amount

    @property
    def unit(self):
        """Gets the unit of this OrderLineItem.  # noqa: E501

        The unit of measurement (ie \"g\" or \"Wh\") for the `amount` ordered for the given project and vintage year.  # noqa: E501

        :return: The unit of this OrderLineItem.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this OrderLineItem.

        The unit of measurement (ie \"g\" or \"Wh\") for the `amount` ordered for the given project and vintage year.  # noqa: E501

        :param unit: The unit of this OrderLineItem.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and unit is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `unit`, must not be `None`"
            )  # noqa: E501

        self._unit = unit

    @property
    def price(self):
        """Gets the price of this OrderLineItem.  # noqa: E501

        The price for the given amount ordered for the given project and vintage year. Does not include any Patch fee. Prices are always represented in the smallest currency unit (ie cents for USD).  # noqa: E501

        :return: The price of this OrderLineItem.  # noqa: E501
        :rtype: int
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this OrderLineItem.

        The price for the given amount ordered for the given project and vintage year. Does not include any Patch fee. Prices are always represented in the smallest currency unit (ie cents for USD).  # noqa: E501

        :param price: The price of this OrderLineItem.  # noqa: E501
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
        """Gets the currency of this OrderLineItem.  # noqa: E501

        The currency code for the `price`.  # noqa: E501

        :return: The currency of this OrderLineItem.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this OrderLineItem.

        The currency code for the `price`.  # noqa: E501

        :param currency: The currency of this OrderLineItem.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and currency is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `currency`, must not be `None`"
            )  # noqa: E501

        self._currency = currency

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
        if not isinstance(other, OrderLineItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrderLineItem):
            return True

        return self.to_dict() != other.to_dict()
