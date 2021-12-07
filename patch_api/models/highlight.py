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


class Highlight(object):
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
    openapi_types = {"slug": "str", "title": "str", "icon_url": "str"}

    attribute_map = {"slug": "slug", "title": "title", "icon_url": "icon_url"}

    def __init__(
        self, slug=None, title=None, icon_url=None, local_vars_configuration=None
    ):  # noqa: E501
        """Highlight - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._slug = None
        self._title = None
        self._icon_url = None
        self.discriminator = None

        self.slug = slug
        self.title = title
        self.icon_url = icon_url

    @property
    def slug(self):
        """Gets the slug of this Highlight.  # noqa: E501

        A unique identifier for each highlight.  # noqa: E501

        :return: The slug of this Highlight.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this Highlight.

        A unique identifier for each highlight.  # noqa: E501

        :param slug: The slug of this Highlight.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and slug is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `slug`, must not be `None`"
            )  # noqa: E501

        self._slug = slug

    @property
    def title(self):
        """Gets the title of this Highlight.  # noqa: E501

        A short string that spotlights a characteristic about the project.  # noqa: E501

        :return: The title of this Highlight.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Highlight.

        A short string that spotlights a characteristic about the project.  # noqa: E501

        :param title: The title of this Highlight.  # noqa: E501
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
    def icon_url(self):
        """Gets the icon_url of this Highlight.  # noqa: E501

        A URL for the corresponding icon.  # noqa: E501

        :return: The icon_url of this Highlight.  # noqa: E501
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this Highlight.

        A URL for the corresponding icon.  # noqa: E501

        :param icon_url: The icon_url of this Highlight.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and icon_url is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `icon_url`, must not be `None`"
            )  # noqa: E501

        self._icon_url = icon_url

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
        if not isinstance(other, Highlight):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Highlight):
            return True

        return self.to_dict() != other.to_dict()
