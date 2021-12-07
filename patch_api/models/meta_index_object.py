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


class MetaIndexObject(object):
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
    openapi_types = {"prev_page": "int", "next_page": "int"}

    attribute_map = {"prev_page": "prev_page", "next_page": "next_page"}

    def __init__(
        self, prev_page=None, next_page=None, local_vars_configuration=None
    ):  # noqa: E501
        """MetaIndexObject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._prev_page = None
        self._next_page = None
        self.discriminator = None

        self.prev_page = prev_page
        self.next_page = next_page

    @property
    def prev_page(self):
        """Gets the prev_page of this MetaIndexObject.  # noqa: E501


        :return: The prev_page of this MetaIndexObject.  # noqa: E501
        :rtype: int
        """
        return self._prev_page

    @prev_page.setter
    def prev_page(self, prev_page):
        """Sets the prev_page of this MetaIndexObject.


        :param prev_page: The prev_page of this MetaIndexObject.  # noqa: E501
        :type: int
        """

        self._prev_page = prev_page

    @property
    def next_page(self):
        """Gets the next_page of this MetaIndexObject.  # noqa: E501


        :return: The next_page of this MetaIndexObject.  # noqa: E501
        :rtype: int
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        """Sets the next_page of this MetaIndexObject.


        :param next_page: The next_page of this MetaIndexObject.  # noqa: E501
        :type: int
        """

        self._next_page = next_page

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
        if not isinstance(other, MetaIndexObject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MetaIndexObject):
            return True

        return self.to_dict() != other.to_dict()
