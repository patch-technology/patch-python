# coding: utf-8

"""
    Patch API V1

    The core API used to integrate with Patch's service  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: developers@usepatch.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from patch_api.configuration import Configuration


class CreateMassEstimateRequest(object):
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
        'mass_g': 'int',
        'project_id': 'str'
    }

    attribute_map = {
        'mass_g': 'mass_g',
        'project_id': 'project_id'
    }

    def __init__(self, mass_g=None, project_id=None, local_vars_configuration=None):  # noqa: E501
        """CreateMassEstimateRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._mass_g = None
        self._project_id = None
        self.discriminator = None

        self.mass_g = mass_g
        if project_id is not None:
            self.project_id = project_id

    @property
    def mass_g(self):
        """Gets the mass_g of this CreateMassEstimateRequest.  # noqa: E501


        :return: The mass_g of this CreateMassEstimateRequest.  # noqa: E501
        :rtype: int
        """
        return self._mass_g

    @mass_g.setter
    def mass_g(self, mass_g):
        """Sets the mass_g of this CreateMassEstimateRequest.


        :param mass_g: The mass_g of this CreateMassEstimateRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and mass_g is None:  # noqa: E501
            raise ValueError("Invalid value for `mass_g`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                mass_g is not None and mass_g > 2000000000):  # noqa: E501
            raise ValueError("Invalid value for `mass_g`, must be a value less than or equal to `2000000000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                mass_g is not None and mass_g < 1):  # noqa: E501
            raise ValueError("Invalid value for `mass_g`, must be a value greater than or equal to `1`")  # noqa: E501

        self._mass_g = mass_g

    @property
    def project_id(self):
        """Gets the project_id of this CreateMassEstimateRequest.  # noqa: E501


        :return: The project_id of this CreateMassEstimateRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateMassEstimateRequest.


        :param project_id: The project_id of this CreateMassEstimateRequest.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
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
        if not isinstance(other, CreateMassEstimateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateMassEstimateRequest):
            return True

        return self.to_dict() != other.to_dict()
