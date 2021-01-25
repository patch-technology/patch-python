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


class CreateMembershipRequest(object):
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
    openapi_types = {"email": "str", "role": "str", "organization_id": "str"}

    attribute_map = {
        "email": "email",
        "role": "role",
        "organization_id": "organization_id",
    }

    def __init__(
        self, email=None, role=None, organization_id=None, local_vars_configuration=None
    ):  # noqa: E501
        """CreateMembershipRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._email = None
        self._role = None
        self._organization_id = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if role is not None:
            self.role = role
        if organization_id is not None:
            self.organization_id = organization_id

    @property
    def email(self):
        """Gets the email of this CreateMembershipRequest.  # noqa: E501


        :return: The email of this CreateMembershipRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CreateMembershipRequest.


        :param email: The email of this CreateMembershipRequest.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def role(self):
        """Gets the role of this CreateMembershipRequest.  # noqa: E501


        :return: The role of this CreateMembershipRequest.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this CreateMembershipRequest.


        :param role: The role of this CreateMembershipRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["admin", "developer", "member"]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and role not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}".format(  # noqa: E501
                    role, allowed_values
                )
            )

        self._role = role

    @property
    def organization_id(self):
        """Gets the organization_id of this CreateMembershipRequest.  # noqa: E501


        :return: The organization_id of this CreateMembershipRequest.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this CreateMembershipRequest.


        :param organization_id: The organization_id of this CreateMembershipRequest.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

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
        if not isinstance(other, CreateMembershipRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateMembershipRequest):
            return True

        return self.to_dict() != other.to_dict()
