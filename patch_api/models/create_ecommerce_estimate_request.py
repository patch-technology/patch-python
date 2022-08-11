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


class CreateEcommerceEstimateRequest(object):
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
        "distance_m": "int",
        "package_mass_g": "int",
        "transportation_method": "str",
        "project_id": "str",
        "create_order": "bool",
    }

    attribute_map = {
        "distance_m": "distance_m",
        "package_mass_g": "package_mass_g",
        "transportation_method": "transportation_method",
        "project_id": "project_id",
        "create_order": "create_order",
    }

    def __init__(
        self,
        distance_m=None,
        package_mass_g=None,
        transportation_method=None,
        project_id=None,
        create_order=False,
        local_vars_configuration=None,
    ):  # noqa: E501
        """CreateEcommerceEstimateRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._distance_m = None
        self._package_mass_g = None
        self._transportation_method = None
        self._project_id = None
        self._create_order = None
        self.discriminator = None

        self.distance_m = distance_m
        self.package_mass_g = package_mass_g
        self.transportation_method = transportation_method
        self.project_id = project_id
        self.create_order = create_order

    @property
    def distance_m(self):
        """Gets the distance_m of this CreateEcommerceEstimateRequest.  # noqa: E501


        :return: The distance_m of this CreateEcommerceEstimateRequest.  # noqa: E501
        :rtype: int
        """
        return self._distance_m

    @distance_m.setter
    def distance_m(self, distance_m):
        """Sets the distance_m of this CreateEcommerceEstimateRequest.


        :param distance_m: The distance_m of this CreateEcommerceEstimateRequest.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation and distance_m is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `distance_m`, must not be `None`"
            )  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and distance_m is not None
            and distance_m > 400000000
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `distance_m`, must be a value less than or equal to `400000000`"
            )  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and distance_m is not None
            and distance_m < 0
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `distance_m`, must be a value greater than or equal to `0`"
            )  # noqa: E501

        self._distance_m = distance_m

    @property
    def package_mass_g(self):
        """Gets the package_mass_g of this CreateEcommerceEstimateRequest.  # noqa: E501


        :return: The package_mass_g of this CreateEcommerceEstimateRequest.  # noqa: E501
        :rtype: int
        """
        return self._package_mass_g

    @package_mass_g.setter
    def package_mass_g(self, package_mass_g):
        """Sets the package_mass_g of this CreateEcommerceEstimateRequest.


        :param package_mass_g: The package_mass_g of this CreateEcommerceEstimateRequest.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and package_mass_g is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `package_mass_g`, must not be `None`"
            )  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and package_mass_g is not None
            and package_mass_g > 2000000000
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `package_mass_g`, must be a value less than or equal to `2000000000`"
            )  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and package_mass_g is not None
            and package_mass_g < 0
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `package_mass_g`, must be a value greater than or equal to `0`"
            )  # noqa: E501

        self._package_mass_g = package_mass_g

    @property
    def transportation_method(self):
        """Gets the transportation_method of this CreateEcommerceEstimateRequest.  # noqa: E501


        :return: The transportation_method of this CreateEcommerceEstimateRequest.  # noqa: E501
        :rtype: str
        """
        return self._transportation_method

    @transportation_method.setter
    def transportation_method(self, transportation_method):
        """Sets the transportation_method of this CreateEcommerceEstimateRequest.


        :param transportation_method: The transportation_method of this CreateEcommerceEstimateRequest.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and transportation_method is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `transportation_method`, must not be `None`"
            )  # noqa: E501
        allowed_values = ["air", "rail", "road", "sea"]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and transportation_method not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `transportation_method` ({0}), must be one of {1}".format(  # noqa: E501
                    transportation_method, allowed_values
                )
            )

        self._transportation_method = transportation_method

    @property
    def project_id(self):
        """Gets the project_id of this CreateEcommerceEstimateRequest.  # noqa: E501


        :return: The project_id of this CreateEcommerceEstimateRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateEcommerceEstimateRequest.


        :param project_id: The project_id of this CreateEcommerceEstimateRequest.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def create_order(self):
        """Gets the create_order of this CreateEcommerceEstimateRequest.  # noqa: E501


        :return: The create_order of this CreateEcommerceEstimateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._create_order

    @create_order.setter
    def create_order(self, create_order):
        """Sets the create_order of this CreateEcommerceEstimateRequest.


        :param create_order: The create_order of this CreateEcommerceEstimateRequest.  # noqa: E501
        :type: bool
        """

        self._create_order = create_order

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
        if not isinstance(other, CreateEcommerceEstimateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateEcommerceEstimateRequest):
            return True

        return self.to_dict() != other.to_dict()
