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


class EstimateResponse(object):
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
    openapi_types = {"success": "bool", "error": "object", "data": "Estimate"}

    attribute_map = {"success": "success", "error": "error", "data": "data"}

    def __init__(
        self, success=None, error=None, data=None, local_vars_configuration=None
    ):  # noqa: E501
        """EstimateResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._success = None
        self._error = None
        self._data = None
        self.discriminator = None

        self.success = success
        self.error = error
        self.data = data

    @property
    def success(self):
        """Gets the success of this EstimateResponse.  # noqa: E501


        :return: The success of this EstimateResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this EstimateResponse.


        :param success: The success of this EstimateResponse.  # noqa: E501
        :type: bool
        """
        if (
            self.local_vars_configuration.client_side_validation and success is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `success`, must not be `None`"
            )  # noqa: E501

        self._success = success

    @property
    def error(self):
        """Gets the error of this EstimateResponse.  # noqa: E501


        :return: The error of this EstimateResponse.  # noqa: E501
        :rtype: object
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this EstimateResponse.


        :param error: The error of this EstimateResponse.  # noqa: E501
        :type: object
        """

        self._error = error

    @property
    def data(self):
        """Gets the data of this EstimateResponse.  # noqa: E501


        :return: The data of this EstimateResponse.  # noqa: E501
        :rtype: Estimate
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this EstimateResponse.


        :param data: The data of this EstimateResponse.  # noqa: E501
        :type: Estimate
        """
        if (
            self.local_vars_configuration.client_side_validation and data is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `data`, must not be `None`"
            )  # noqa: E501

        self._data = data

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
        if not isinstance(other, EstimateResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EstimateResponse):
            return True

        return self.to_dict() != other.to_dict()
