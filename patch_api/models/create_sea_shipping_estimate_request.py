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


class CreateSeaShippingEstimateRequest(object):
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
        "destination_country_code": "str",
        "destination_locode": "str",
        "destination_postal_code": "str",
        "origin_country_code": "str",
        "origin_locode": "str",
        "origin_postal_code": "str",
        "container_size_code": "str",
        "emissions_scope": "str",
        "freight_mass_g": "int",
        "freight_volume_cubic_m": "int",
        "number_of_containers": "int",
        "vessel_imo": "int",
        "project_id": "str",
        "create_order": "bool",
    }

    attribute_map = {
        "destination_country_code": "destination_country_code",
        "destination_locode": "destination_locode",
        "destination_postal_code": "destination_postal_code",
        "origin_country_code": "origin_country_code",
        "origin_locode": "origin_locode",
        "origin_postal_code": "origin_postal_code",
        "container_size_code": "container_size_code",
        "emissions_scope": "emissions_scope",
        "freight_mass_g": "freight_mass_g",
        "freight_volume_cubic_m": "freight_volume_cubic_m",
        "number_of_containers": "number_of_containers",
        "vessel_imo": "vessel_imo",
        "project_id": "project_id",
        "create_order": "create_order",
    }

    def __init__(
        self,
        destination_country_code=None,
        destination_locode=None,
        destination_postal_code=None,
        origin_country_code=None,
        origin_locode=None,
        origin_postal_code=None,
        container_size_code=None,
        emissions_scope="ttw",
        freight_mass_g=None,
        freight_volume_cubic_m=None,
        number_of_containers=None,
        vessel_imo=None,
        project_id=None,
        create_order=False,
        local_vars_configuration=None,
    ):  # noqa: E501
        """CreateSeaShippingEstimateRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._destination_country_code = None
        self._destination_locode = None
        self._destination_postal_code = None
        self._origin_country_code = None
        self._origin_locode = None
        self._origin_postal_code = None
        self._container_size_code = None
        self._emissions_scope = None
        self._freight_mass_g = None
        self._freight_volume_cubic_m = None
        self._number_of_containers = None
        self._vessel_imo = None
        self._project_id = None
        self._create_order = None
        self.discriminator = None

        self.destination_country_code = destination_country_code
        self.destination_locode = destination_locode
        self.destination_postal_code = destination_postal_code
        self.origin_country_code = origin_country_code
        self.origin_locode = origin_locode
        self.origin_postal_code = origin_postal_code
        if container_size_code is not None:
            self.container_size_code = container_size_code
        self.emissions_scope = emissions_scope
        if freight_mass_g is not None:
            self.freight_mass_g = freight_mass_g
        self.freight_volume_cubic_m = freight_volume_cubic_m
        self.number_of_containers = number_of_containers
        self.vessel_imo = vessel_imo
        self.project_id = project_id
        self.create_order = create_order

    @property
    def destination_country_code(self):
        """Gets the destination_country_code of this CreateSeaShippingEstimateRequest.  # noqa: E501


        :return: The destination_country_code of this CreateSeaShippingEstimateRequest.  # noqa: E501
        :rtype: str
        """
        return self._destination_country_code

    @destination_country_code.setter
    def destination_country_code(self, destination_country_code):
        """Sets the destination_country_code of this CreateSeaShippingEstimateRequest.


        :param destination_country_code: The destination_country_code of this CreateSeaShippingEstimateRequest.  # noqa: E501
        :type: str
        """

        self._destination_country_code = destination_country_code

    @property
    def destination_locode(self):
        """Gets the destination_locode of this CreateSeaShippingEstimateRequest.  # noqa: E501


        :return: The destination_locode of this CreateSeaShippingEstimateRequest.  # noqa: E501
        :rtype: str
        """
        return self._destination_locode

    @destination_locode.setter
    def destination_locode(self, destination_locode):
        """Sets the destination_locode of this CreateSeaShippingEstimateRequest.


        :param destination_locode: The destination_locode of this CreateSeaShippingEstimateRequest.  # noqa: E501
        :type: str
        """

        self._destination_locode = destination_locode

    @property
    def destination_postal_code(self):
        """Gets the destination_postal_code of this CreateSeaShippingEstimateRequest.  # noqa: E501


        :return: The destination_postal_code of this CreateSeaShippingEstimateRequest.  # noqa: E501
        :rtype: str
        """
        return self._destination_postal_code

    @destination_postal_code.setter
    def destination_postal_code(self, destination_postal_code):
        """Sets the destination_postal_code of this CreateSeaShippingEstimateRequest.


        :param destination_postal_code: The destination_postal_code of this CreateSeaShippingEstimateRequest.  # noqa: E501
        :type: str
        """

        self._destination_postal_code = destination_postal_code

    @property
    def origin_country_code(self):
        """Gets the origin_country_code of this CreateSeaShippingEstimateRequest.  # noqa: E501


        :return: The origin_country_code of this CreateSeaShippingEstimateRequest.  # noqa: E501
        :rtype: str
        """
        return self._origin_country_code

    @origin_country_code.setter
    def origin_country_code(self, origin_country_code):
        """Sets the origin_country_code of this CreateSeaShippingEstimateRequest.


        :param origin_country_code: The origin_country_code of this CreateSeaShippingEstimateRequest.  # noqa: E501
        :type: str
        """

        self._origin_country_code = origin_country_code

    @property
    def origin_locode(self):
        """Gets the origin_locode of this CreateSeaShippingEstimateRequest.  # noqa: E501


        :return: The origin_locode of this CreateSeaShippingEstimateRequest.  # noqa: E501
        :rtype: str
        """
        return self._origin_locode

    @origin_locode.setter
    def origin_locode(self, origin_locode):
        """Sets the origin_locode of this CreateSeaShippingEstimateRequest.


        :param origin_locode: The origin_locode of this CreateSeaShippingEstimateRequest.  # noqa: E501
        :type: str
        """

        self._origin_locode = origin_locode

    @property
    def origin_postal_code(self):
        """Gets the origin_postal_code of this CreateSeaShippingEstimateRequest.  # noqa: E501


        :return: The origin_postal_code of this CreateSeaShippingEstimateRequest.  # noqa: E501
        :rtype: str
        """
        return self._origin_postal_code

    @origin_postal_code.setter
    def origin_postal_code(self, origin_postal_code):
        """Sets the origin_postal_code of this CreateSeaShippingEstimateRequest.


        :param origin_postal_code: The origin_postal_code of this CreateSeaShippingEstimateRequest.  # noqa: E501
        :type: str
        """

        self._origin_postal_code = origin_postal_code

    @property
    def container_size_code(self):
        """Gets the container_size_code of this CreateSeaShippingEstimateRequest.  # noqa: E501


        :return: The container_size_code of this CreateSeaShippingEstimateRequest.  # noqa: E501
        :rtype: str
        """
        return self._container_size_code

    @container_size_code.setter
    def container_size_code(self, container_size_code):
        """Sets the container_size_code of this CreateSeaShippingEstimateRequest.


        :param container_size_code: The container_size_code of this CreateSeaShippingEstimateRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["20GP", "40GP", "22G1", "42G1", "40HC", "45G1"]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and container_size_code not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `container_size_code` ({0}), must be one of {1}".format(  # noqa: E501
                    container_size_code, allowed_values
                )
            )

        self._container_size_code = container_size_code

    @property
    def emissions_scope(self):
        """Gets the emissions_scope of this CreateSeaShippingEstimateRequest.  # noqa: E501


        :return: The emissions_scope of this CreateSeaShippingEstimateRequest.  # noqa: E501
        :rtype: str
        """
        return self._emissions_scope

    @emissions_scope.setter
    def emissions_scope(self, emissions_scope):
        """Sets the emissions_scope of this CreateSeaShippingEstimateRequest.


        :param emissions_scope: The emissions_scope of this CreateSeaShippingEstimateRequest.  # noqa: E501
        :type: str
        """
        allowed_values = [None, "wtt", "ttw", "wtw"]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and emissions_scope not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `emissions_scope` ({0}), must be one of {1}".format(  # noqa: E501
                    emissions_scope, allowed_values
                )
            )

        self._emissions_scope = emissions_scope

    @property
    def freight_mass_g(self):
        """Gets the freight_mass_g of this CreateSeaShippingEstimateRequest.  # noqa: E501


        :return: The freight_mass_g of this CreateSeaShippingEstimateRequest.  # noqa: E501
        :rtype: int
        """
        return self._freight_mass_g

    @freight_mass_g.setter
    def freight_mass_g(self, freight_mass_g):
        """Sets the freight_mass_g of this CreateSeaShippingEstimateRequest.


        :param freight_mass_g: The freight_mass_g of this CreateSeaShippingEstimateRequest.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and freight_mass_g is not None
            and freight_mass_g > 2000000000
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `freight_mass_g`, must be a value less than or equal to `2000000000`"
            )  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and freight_mass_g is not None
            and freight_mass_g < 0
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `freight_mass_g`, must be a value greater than or equal to `0`"
            )  # noqa: E501

        self._freight_mass_g = freight_mass_g

    @property
    def freight_volume_cubic_m(self):
        """Gets the freight_volume_cubic_m of this CreateSeaShippingEstimateRequest.  # noqa: E501


        :return: The freight_volume_cubic_m of this CreateSeaShippingEstimateRequest.  # noqa: E501
        :rtype: int
        """
        return self._freight_volume_cubic_m

    @freight_volume_cubic_m.setter
    def freight_volume_cubic_m(self, freight_volume_cubic_m):
        """Sets the freight_volume_cubic_m of this CreateSeaShippingEstimateRequest.


        :param freight_volume_cubic_m: The freight_volume_cubic_m of this CreateSeaShippingEstimateRequest.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and freight_volume_cubic_m is not None
            and freight_volume_cubic_m < 0
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `freight_volume_cubic_m`, must be a value greater than or equal to `0`"
            )  # noqa: E501

        self._freight_volume_cubic_m = freight_volume_cubic_m

    @property
    def number_of_containers(self):
        """Gets the number_of_containers of this CreateSeaShippingEstimateRequest.  # noqa: E501


        :return: The number_of_containers of this CreateSeaShippingEstimateRequest.  # noqa: E501
        :rtype: int
        """
        return self._number_of_containers

    @number_of_containers.setter
    def number_of_containers(self, number_of_containers):
        """Sets the number_of_containers of this CreateSeaShippingEstimateRequest.


        :param number_of_containers: The number_of_containers of this CreateSeaShippingEstimateRequest.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and number_of_containers is not None
            and number_of_containers < 0
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `number_of_containers`, must be a value greater than or equal to `0`"
            )  # noqa: E501

        self._number_of_containers = number_of_containers

    @property
    def vessel_imo(self):
        """Gets the vessel_imo of this CreateSeaShippingEstimateRequest.  # noqa: E501


        :return: The vessel_imo of this CreateSeaShippingEstimateRequest.  # noqa: E501
        :rtype: int
        """
        return self._vessel_imo

    @vessel_imo.setter
    def vessel_imo(self, vessel_imo):
        """Sets the vessel_imo of this CreateSeaShippingEstimateRequest.


        :param vessel_imo: The vessel_imo of this CreateSeaShippingEstimateRequest.  # noqa: E501
        :type: int
        """

        self._vessel_imo = vessel_imo

    @property
    def project_id(self):
        """Gets the project_id of this CreateSeaShippingEstimateRequest.  # noqa: E501


        :return: The project_id of this CreateSeaShippingEstimateRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateSeaShippingEstimateRequest.


        :param project_id: The project_id of this CreateSeaShippingEstimateRequest.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def create_order(self):
        """Gets the create_order of this CreateSeaShippingEstimateRequest.  # noqa: E501


        :return: The create_order of this CreateSeaShippingEstimateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._create_order

    @create_order.setter
    def create_order(self, create_order):
        """Sets the create_order of this CreateSeaShippingEstimateRequest.


        :param create_order: The create_order of this CreateSeaShippingEstimateRequest.  # noqa: E501
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
        if not isinstance(other, CreateSeaShippingEstimateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateSeaShippingEstimateRequest):
            return True

        return self.to_dict() != other.to_dict()
