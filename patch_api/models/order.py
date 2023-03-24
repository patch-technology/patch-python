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


class Order(object):
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
        "created_at": "datetime",
        "production": "bool",
        "state": "str",
        "amount": "int",
        "unit": "str",
        "price": "int",
        "patch_fee": "int",
        "currency": "str",
        "registry_url": "str",
        "metadata": "object",
        "line_items": "list[OrderLineItem]",
        "issued_to": "OrderIssuedTo",
    }

    attribute_map = {
        "id": "id",
        "created_at": "created_at",
        "production": "production",
        "state": "state",
        "amount": "amount",
        "unit": "unit",
        "price": "price",
        "patch_fee": "patch_fee",
        "currency": "currency",
        "registry_url": "registry_url",
        "metadata": "metadata",
        "line_items": "line_items",
        "issued_to": "issued_to",
    }

    def __init__(
        self,
        id=None,
        created_at=None,
        production=None,
        state=None,
        amount=None,
        unit=None,
        price=None,
        patch_fee=None,
        currency=None,
        registry_url=None,
        metadata=None,
        line_items=None,
        issued_to=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """Order - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created_at = None
        self._production = None
        self._state = None
        self._amount = None
        self._unit = None
        self._price = None
        self._patch_fee = None
        self._currency = None
        self._registry_url = None
        self._metadata = None
        self._line_items = None
        self._issued_to = None
        self.discriminator = None

        self.id = id
        if created_at is not None:
            self.created_at = created_at
        self.production = production
        self.state = state
        self.amount = amount
        self.unit = unit
        self.price = price
        self.patch_fee = patch_fee
        self.currency = currency
        if registry_url is not None:
            self.registry_url = registry_url
        self.metadata = metadata
        if line_items is not None:
            self.line_items = line_items
        if issued_to is not None:
            self.issued_to = issued_to

    @property
    def id(self):
        """Gets the id of this Order.  # noqa: E501

        A unique uid for the record. UIDs will be prepended by ord_prod or ord_test depending on the mode it was created in.  # noqa: E501

        :return: The id of this Order.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Order.

        A unique uid for the record. UIDs will be prepended by ord_prod or ord_test depending on the mode it was created in.  # noqa: E501

        :param id: The id of this Order.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and id is None
        ):  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this Order.  # noqa: E501

        The timestamp at which the order was created  # noqa: E501

        :return: The created_at of this Order.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Order.

        The timestamp at which the order was created  # noqa: E501

        :param created_at: The created_at of this Order.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def production(self):
        """Gets the production of this Order.  # noqa: E501

        A boolean indicating if this order is a production or demo mode order.  # noqa: E501

        :return: The production of this Order.  # noqa: E501
        :rtype: bool
        """
        return self._production

    @production.setter
    def production(self, production):
        """Sets the production of this Order.

        A boolean indicating if this order is a production or demo mode order.  # noqa: E501

        :param production: The production of this Order.  # noqa: E501
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
    def state(self):
        """Gets the state of this Order.  # noqa: E501

        The current state of the order.  # noqa: E501

        :return: The state of this Order.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Order.

        The current state of the order.  # noqa: E501

        :param state: The state of this Order.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and state is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `state`, must not be `None`"
            )  # noqa: E501
        allowed_values = [
            "draft",
            "reserved",
            "placed",
            "processing",
            "complete",
            "cancelled",
        ]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and state not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}".format(  # noqa: E501
                    state, allowed_values
                )
            )

        self._state = state

    @property
    def amount(self):
        """Gets the amount of this Order.  # noqa: E501

        The amount in `unit`s purchased through this order.  # noqa: E501

        :return: The amount of this Order.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Order.

        The amount in `unit`s purchased through this order.  # noqa: E501

        :param amount: The amount of this Order.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation and amount is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `amount`, must not be `None`"
            )  # noqa: E501
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
        """Gets the unit of this Order.  # noqa: E501

        The unit of measurement (ie \"g\" or \"Wh\") for the `amount` ordered.  # noqa: E501

        :return: The unit of this Order.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Order.

        The unit of measurement (ie \"g\" or \"Wh\") for the `amount` ordered.  # noqa: E501

        :param unit: The unit of this Order.  # noqa: E501
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
        """Gets the price of this Order.  # noqa: E501

        The total price for the `amount` ordered. Prices are always represented in the smallest currency unit (ie cents for USD).  # noqa: E501

        :return: The price of this Order.  # noqa: E501
        :rtype: int
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Order.

        The total price for the `amount` ordered. Prices are always represented in the smallest currency unit (ie cents for USD).  # noqa: E501

        :param price: The price of this Order.  # noqa: E501
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
    def patch_fee(self):
        """Gets the patch_fee of this Order.  # noqa: E501

        The Patch Fee for this order. Patch Fee is always represented in the smallest currency unit (ie cents for USD).  # noqa: E501

        :return: The patch_fee of this Order.  # noqa: E501
        :rtype: int
        """
        return self._patch_fee

    @patch_fee.setter
    def patch_fee(self, patch_fee):
        """Sets the patch_fee of this Order.

        The Patch Fee for this order. Patch Fee is always represented in the smallest currency unit (ie cents for USD).  # noqa: E501

        :param patch_fee: The patch_fee of this Order.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation and patch_fee is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `patch_fee`, must not be `None`"
            )  # noqa: E501

        self._patch_fee = patch_fee

    @property
    def currency(self):
        """Gets the currency of this Order.  # noqa: E501

        The currency code for the `price` and `patch_fee`.  # noqa: E501

        :return: The currency of this Order.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Order.

        The currency code for the `price` and `patch_fee`.  # noqa: E501

        :param currency: The currency of this Order.  # noqa: E501
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
    def registry_url(self):
        """Gets the registry_url of this Order.  # noqa: E501

        The url of this order in the public registry.  # noqa: E501

        :return: The registry_url of this Order.  # noqa: E501
        :rtype: str
        """
        return self._registry_url

    @registry_url.setter
    def registry_url(self, registry_url):
        """Sets the registry_url of this Order.

        The url of this order in the public registry.  # noqa: E501

        :param registry_url: The registry_url of this Order.  # noqa: E501
        :type: str
        """

        self._registry_url = registry_url

    @property
    def metadata(self):
        """Gets the metadata of this Order.  # noqa: E501

        An optional JSON object containing metadata for this order.  # noqa: E501

        :return: The metadata of this Order.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Order.

        An optional JSON object containing metadata for this order.  # noqa: E501

        :param metadata: The metadata of this Order.  # noqa: E501
        :type: object
        """
        if (
            self.local_vars_configuration.client_side_validation and metadata is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `metadata`, must not be `None`"
            )  # noqa: E501

        self._metadata = metadata

    @property
    def line_items(self):
        """Gets the line_items of this Order.  # noqa: E501

        An array containing the line items allocated for this order. Line items are grouped by project, vintage year, and price.  # noqa: E501

        :return: The line_items of this Order.  # noqa: E501
        :rtype: list[OrderLineItem]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this Order.

        An array containing the line items allocated for this order. Line items are grouped by project, vintage year, and price.  # noqa: E501

        :param line_items: The line_items of this Order.  # noqa: E501
        :type: list[OrderLineItem]
        """

        self._line_items = line_items

    @property
    def issued_to(self):
        """Gets the issued_to of this Order.  # noqa: E501

        An object containing the name & email of the party the inventory will be issued to.  # noqa: E501

        :return: The issued_to of this Order.  # noqa: E501
        :rtype: OrderIssuedTo
        """
        return self._issued_to

    @issued_to.setter
    def issued_to(self, issued_to):
        """Sets the issued_to of this Order.

        An object containing the name & email of the party the inventory will be issued to.  # noqa: E501

        :param issued_to: The issued_to of this Order.  # noqa: E501
        :type: OrderIssuedTo
        """

        self._issued_to = issued_to

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
        if not isinstance(other, Order):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Order):
            return True

        return self.to_dict() != other.to_dict()
