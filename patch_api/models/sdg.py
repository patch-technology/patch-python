# coding: utf-8

"""
    Patch API V2

    The core API used to integrate with Patch's service  # noqa: E501

    The version of the OpenAPI document: 2
    Contact: engineering@usepatch.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from patch_api.configuration import Configuration


class Sdg(object):
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
        "title": "str",
        "number": "int",
        "description": "str",
        "url": "str",
    }

    attribute_map = {
        "title": "title",
        "number": "number",
        "description": "description",
        "url": "url",
    }

    def __init__(
        self,
        title=None,
        number=None,
        description=None,
        url=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """Sdg - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._title = None
        self._number = None
        self._description = None
        self._url = None
        self.discriminator = None

        self.title = title
        self.number = number
        self.description = description
        self.url = url

    @property
    def title(self):
        """Gets the title of this Sdg.  # noqa: E501

        The title of the Sustainable Development Goal.  # noqa: E501

        :return: The title of this Sdg.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Sdg.

        The title of the Sustainable Development Goal.  # noqa: E501

        :param title: The title of this Sdg.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and title is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `title`, must not be `None`"
            )  # noqa: E501

        self._title = title

    @property
    def number(self):
        """Gets the number of this Sdg.  # noqa: E501

        The Sustainable Development Goal number.  # noqa: E501

        :return: The number of this Sdg.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Sdg.

        The Sustainable Development Goal number.  # noqa: E501

        :param number: The number of this Sdg.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation and number is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `number`, must not be `None`"
            )  # noqa: E501

        self._number = number

    @property
    def description(self):
        """Gets the description of this Sdg.  # noqa: E501

        The description of the Sustainable Development Goal.  # noqa: E501

        :return: The description of this Sdg.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Sdg.

        The description of the Sustainable Development Goal.  # noqa: E501

        :param description: The description of this Sdg.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and description is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `description`, must not be `None`"
            )  # noqa: E501

        self._description = description

    @property
    def url(self):
        """Gets the url of this Sdg.  # noqa: E501

        The url to an information page for the Sustainable Development Goal.  # noqa: E501

        :return: The url of this Sdg.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Sdg.

        The url to an information page for the Sustainable Development Goal.  # noqa: E501

        :param url: The url of this Sdg.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and url is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `url`, must not be `None`"
            )  # noqa: E501

        self._url = url

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
        if not isinstance(other, Sdg):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Sdg):
            return True

        return self.to_dict() != other.to_dict()
