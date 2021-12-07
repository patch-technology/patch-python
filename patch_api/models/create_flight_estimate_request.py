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


class CreateFlightEstimateRequest(object):
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
        "origin_airport": "str",
        "destination_airport": "str",
        "aircraft_code": "str",
        "cabin_class": "str",
        "passenger_count": "int",
        "project_id": "str",
        "create_order": "bool",
    }

    attribute_map = {
        "distance_m": "distance_m",
        "origin_airport": "origin_airport",
        "destination_airport": "destination_airport",
        "aircraft_code": "aircraft_code",
        "cabin_class": "cabin_class",
        "passenger_count": "passenger_count",
        "project_id": "project_id",
        "create_order": "create_order",
    }

    def __init__(
        self,
        distance_m=None,
        origin_airport=None,
        destination_airport=None,
        aircraft_code=None,
        cabin_class=None,
        passenger_count=None,
        project_id=None,
        create_order=False,
        local_vars_configuration=None,
    ):  # noqa: E501
        """CreateFlightEstimateRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._distance_m = None
        self._origin_airport = None
        self._destination_airport = None
        self._aircraft_code = None
        self._cabin_class = None
        self._passenger_count = None
        self._project_id = None
        self._create_order = None
        self.discriminator = None

        self.distance_m = distance_m
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.aircraft_code = aircraft_code
        self.cabin_class = cabin_class
        self.passenger_count = passenger_count
        self.project_id = project_id
        self.create_order = create_order

    @property
    def distance_m(self):
        """Gets the distance_m of this CreateFlightEstimateRequest.  # noqa: E501


        :return: The distance_m of this CreateFlightEstimateRequest.  # noqa: E501
        :rtype: int
        """
        return self._distance_m

    @distance_m.setter
    def distance_m(self, distance_m):
        """Sets the distance_m of this CreateFlightEstimateRequest.


        :param distance_m: The distance_m of this CreateFlightEstimateRequest.  # noqa: E501
        :type: int
        """
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
    def origin_airport(self):
        """Gets the origin_airport of this CreateFlightEstimateRequest.  # noqa: E501


        :return: The origin_airport of this CreateFlightEstimateRequest.  # noqa: E501
        :rtype: str
        """
        return self._origin_airport

    @origin_airport.setter
    def origin_airport(self, origin_airport):
        """Sets the origin_airport of this CreateFlightEstimateRequest.


        :param origin_airport: The origin_airport of this CreateFlightEstimateRequest.  # noqa: E501
        :type: str
        """

        self._origin_airport = origin_airport

    @property
    def destination_airport(self):
        """Gets the destination_airport of this CreateFlightEstimateRequest.  # noqa: E501


        :return: The destination_airport of this CreateFlightEstimateRequest.  # noqa: E501
        :rtype: str
        """
        return self._destination_airport

    @destination_airport.setter
    def destination_airport(self, destination_airport):
        """Sets the destination_airport of this CreateFlightEstimateRequest.


        :param destination_airport: The destination_airport of this CreateFlightEstimateRequest.  # noqa: E501
        :type: str
        """

        self._destination_airport = destination_airport

    @property
    def aircraft_code(self):
        """Gets the aircraft_code of this CreateFlightEstimateRequest.  # noqa: E501


        :return: The aircraft_code of this CreateFlightEstimateRequest.  # noqa: E501
        :rtype: str
        """
        return self._aircraft_code

    @aircraft_code.setter
    def aircraft_code(self, aircraft_code):
        """Sets the aircraft_code of this CreateFlightEstimateRequest.


        :param aircraft_code: The aircraft_code of this CreateFlightEstimateRequest.  # noqa: E501
        :type: str
        """

        self._aircraft_code = aircraft_code

    @property
    def cabin_class(self):
        """Gets the cabin_class of this CreateFlightEstimateRequest.  # noqa: E501


        :return: The cabin_class of this CreateFlightEstimateRequest.  # noqa: E501
        :rtype: str
        """
        return self._cabin_class

    @cabin_class.setter
    def cabin_class(self, cabin_class):
        """Sets the cabin_class of this CreateFlightEstimateRequest.


        :param cabin_class: The cabin_class of this CreateFlightEstimateRequest.  # noqa: E501
        :type: str
        """

        self._cabin_class = cabin_class

    @property
    def passenger_count(self):
        """Gets the passenger_count of this CreateFlightEstimateRequest.  # noqa: E501


        :return: The passenger_count of this CreateFlightEstimateRequest.  # noqa: E501
        :rtype: int
        """
        return self._passenger_count

    @passenger_count.setter
    def passenger_count(self, passenger_count):
        """Sets the passenger_count of this CreateFlightEstimateRequest.


        :param passenger_count: The passenger_count of this CreateFlightEstimateRequest.  # noqa: E501
        :type: int
        """

        self._passenger_count = passenger_count

    @property
    def project_id(self):
        """Gets the project_id of this CreateFlightEstimateRequest.  # noqa: E501


        :return: The project_id of this CreateFlightEstimateRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateFlightEstimateRequest.


        :param project_id: The project_id of this CreateFlightEstimateRequest.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def create_order(self):
        """Gets the create_order of this CreateFlightEstimateRequest.  # noqa: E501


        :return: The create_order of this CreateFlightEstimateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._create_order

    @create_order.setter
    def create_order(self, create_order):
        """Sets the create_order of this CreateFlightEstimateRequest.


        :param create_order: The create_order of this CreateFlightEstimateRequest.  # noqa: E501
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
        if not isinstance(other, CreateFlightEstimateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateFlightEstimateRequest):
            return True

        return self.to_dict() != other.to_dict()
