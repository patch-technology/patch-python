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


class CreateOrderLineItemRequest(object):
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
        "project_id": "str",
        "vintage_year": "int",
        "vintage_start_year": "int",
        "vintage_end_year": "int",
        "price": "int",
        "currency": "str",
        "amount": "int",
        "unit": "str",
    }

    attribute_map = {
        "project_id": "project_id",
        "vintage_year": "vintage_year",
        "vintage_start_year": "vintage_start_year",
        "vintage_end_year": "vintage_end_year",
        "price": "price",
        "currency": "currency",
        "amount": "amount",
        "unit": "unit",
    }

    def __init__(
        self,
        project_id=None,
        vintage_year=None,
        vintage_start_year=None,
        vintage_end_year=None,
        price=None,
        currency=None,
        amount=None,
        unit=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """CreateOrderLineItemRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._project_id = None
        self._vintage_year = None
        self._vintage_start_year = None
        self._vintage_end_year = None
        self._price = None
        self._currency = None
        self._amount = None
        self._unit = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        self.vintage_year = vintage_year
        self.vintage_start_year = vintage_start_year
        self.vintage_end_year = vintage_end_year
        self.price = price
        self.currency = currency
        self.amount = amount
        self.unit = unit

    @property
    def project_id(self):
        """Gets the project_id of this CreateOrderLineItemRequest.  # noqa: E501


        :return: The project_id of this CreateOrderLineItemRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateOrderLineItemRequest.


        :param project_id: The project_id of this CreateOrderLineItemRequest.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def vintage_year(self):
        """Gets the vintage_year of this CreateOrderLineItemRequest.  # noqa: E501


        :return: The vintage_year of this CreateOrderLineItemRequest.  # noqa: E501
        :rtype: int
        """
        return self._vintage_year

    @vintage_year.setter
    def vintage_year(self, vintage_year):
        """Sets the vintage_year of this CreateOrderLineItemRequest.


        :param vintage_year: The vintage_year of this CreateOrderLineItemRequest.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and vintage_year is not None
            and vintage_year > 2100
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `vintage_year`, must be a value less than or equal to `2100`"
            )  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and vintage_year is not None
            and vintage_year < 1900
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `vintage_year`, must be a value greater than or equal to `1900`"
            )  # noqa: E501

        self._vintage_year = vintage_year

    @property
    def vintage_start_year(self):
        """Gets the vintage_start_year of this CreateOrderLineItemRequest.  # noqa: E501


        :return: The vintage_start_year of this CreateOrderLineItemRequest.  # noqa: E501
        :rtype: int
        """
        return self._vintage_start_year

    @vintage_start_year.setter
    def vintage_start_year(self, vintage_start_year):
        """Sets the vintage_start_year of this CreateOrderLineItemRequest.


        :param vintage_start_year: The vintage_start_year of this CreateOrderLineItemRequest.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and vintage_start_year is not None
            and vintage_start_year > 2100
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `vintage_start_year`, must be a value less than or equal to `2100`"
            )  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and vintage_start_year is not None
            and vintage_start_year < 1900
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `vintage_start_year`, must be a value greater than or equal to `1900`"
            )  # noqa: E501

        self._vintage_start_year = vintage_start_year

    @property
    def vintage_end_year(self):
        """Gets the vintage_end_year of this CreateOrderLineItemRequest.  # noqa: E501


        :return: The vintage_end_year of this CreateOrderLineItemRequest.  # noqa: E501
        :rtype: int
        """
        return self._vintage_end_year

    @vintage_end_year.setter
    def vintage_end_year(self, vintage_end_year):
        """Sets the vintage_end_year of this CreateOrderLineItemRequest.


        :param vintage_end_year: The vintage_end_year of this CreateOrderLineItemRequest.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and vintage_end_year is not None
            and vintage_end_year > 2100
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `vintage_end_year`, must be a value less than or equal to `2100`"
            )  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and vintage_end_year is not None
            and vintage_end_year < 1900
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `vintage_end_year`, must be a value greater than or equal to `1900`"
            )  # noqa: E501

        self._vintage_end_year = vintage_end_year

    @property
    def price(self):
        """Gets the price of this CreateOrderLineItemRequest.  # noqa: E501


        :return: The price of this CreateOrderLineItemRequest.  # noqa: E501
        :rtype: int
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this CreateOrderLineItemRequest.


        :param price: The price of this CreateOrderLineItemRequest.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and price is not None
            and price < 2
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `price`, must be a value greater than or equal to `2`"
            )  # noqa: E501

        self._price = price

    @property
    def currency(self):
        """Gets the currency of this CreateOrderLineItemRequest.  # noqa: E501


        :return: The currency of this CreateOrderLineItemRequest.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CreateOrderLineItemRequest.


        :param currency: The currency of this CreateOrderLineItemRequest.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def amount(self):
        """Gets the amount of this CreateOrderLineItemRequest.  # noqa: E501


        :return: The amount of this CreateOrderLineItemRequest.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CreateOrderLineItemRequest.


        :param amount: The amount of this CreateOrderLineItemRequest.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and amount is not None
            and amount > 100000000000000
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `amount`, must be a value less than or equal to `100000000000000`"
            )  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and amount is not None
            and amount < 0
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `amount`, must be a value greater than or equal to `0`"
            )  # noqa: E501

        self._amount = amount

    @property
    def unit(self):
        """Gets the unit of this CreateOrderLineItemRequest.  # noqa: E501


        :return: The unit of this CreateOrderLineItemRequest.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this CreateOrderLineItemRequest.


        :param unit: The unit of this CreateOrderLineItemRequest.  # noqa: E501
        :type: str
        """
        allowed_values = [None, "g", "Wh"]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and unit not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `unit` ({0}), must be one of {1}".format(  # noqa: E501
                    unit, allowed_values
                )
            )

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
        if not isinstance(other, CreateOrderLineItemRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateOrderLineItemRequest):
            return True

        return self.to_dict() != other.to_dict()
