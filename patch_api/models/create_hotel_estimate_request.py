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


class CreateHotelEstimateRequest(object):
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
        "country_code": "str",
        "city": "str",
        "region": "str",
        "star_rating": "int",
        "number_of_nights": "int",
        "number_of_rooms": "int",
        "project_id": "str",
        "create_order": "bool",
    }

    attribute_map = {
        "country_code": "country_code",
        "city": "city",
        "region": "region",
        "star_rating": "star_rating",
        "number_of_nights": "number_of_nights",
        "number_of_rooms": "number_of_rooms",
        "project_id": "project_id",
        "create_order": "create_order",
    }

    def __init__(
        self,
        country_code=None,
        city=None,
        region=None,
        star_rating=None,
        number_of_nights=None,
        number_of_rooms=None,
        project_id=None,
        create_order=False,
        local_vars_configuration=None,
    ):  # noqa: E501
        """CreateHotelEstimateRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._country_code = None
        self._city = None
        self._region = None
        self._star_rating = None
        self._number_of_nights = None
        self._number_of_rooms = None
        self._project_id = None
        self._create_order = None
        self.discriminator = None

        self.country_code = country_code
        if city is not None:
            self.city = city
        if region is not None:
            self.region = region
        if star_rating is not None:
            self.star_rating = star_rating
        if number_of_nights is not None:
            self.number_of_nights = number_of_nights
        if number_of_rooms is not None:
            self.number_of_rooms = number_of_rooms
        self.project_id = project_id
        self.create_order = create_order

    @property
    def country_code(self):
        """Gets the country_code of this CreateHotelEstimateRequest.  # noqa: E501


        :return: The country_code of this CreateHotelEstimateRequest.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this CreateHotelEstimateRequest.


        :param country_code: The country_code of this CreateHotelEstimateRequest.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and country_code is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `country_code`, must not be `None`"
            )  # noqa: E501

        self._country_code = country_code

    @property
    def city(self):
        """Gets the city of this CreateHotelEstimateRequest.  # noqa: E501


        :return: The city of this CreateHotelEstimateRequest.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this CreateHotelEstimateRequest.


        :param city: The city of this CreateHotelEstimateRequest.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def region(self):
        """Gets the region of this CreateHotelEstimateRequest.  # noqa: E501


        :return: The region of this CreateHotelEstimateRequest.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CreateHotelEstimateRequest.


        :param region: The region of this CreateHotelEstimateRequest.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def star_rating(self):
        """Gets the star_rating of this CreateHotelEstimateRequest.  # noqa: E501


        :return: The star_rating of this CreateHotelEstimateRequest.  # noqa: E501
        :rtype: int
        """
        return self._star_rating

    @star_rating.setter
    def star_rating(self, star_rating):
        """Sets the star_rating of this CreateHotelEstimateRequest.


        :param star_rating: The star_rating of this CreateHotelEstimateRequest.  # noqa: E501
        :type: int
        """

        self._star_rating = star_rating

    @property
    def number_of_nights(self):
        """Gets the number_of_nights of this CreateHotelEstimateRequest.  # noqa: E501


        :return: The number_of_nights of this CreateHotelEstimateRequest.  # noqa: E501
        :rtype: int
        """
        return self._number_of_nights

    @number_of_nights.setter
    def number_of_nights(self, number_of_nights):
        """Sets the number_of_nights of this CreateHotelEstimateRequest.


        :param number_of_nights: The number_of_nights of this CreateHotelEstimateRequest.  # noqa: E501
        :type: int
        """

        self._number_of_nights = number_of_nights

    @property
    def number_of_rooms(self):
        """Gets the number_of_rooms of this CreateHotelEstimateRequest.  # noqa: E501


        :return: The number_of_rooms of this CreateHotelEstimateRequest.  # noqa: E501
        :rtype: int
        """
        return self._number_of_rooms

    @number_of_rooms.setter
    def number_of_rooms(self, number_of_rooms):
        """Sets the number_of_rooms of this CreateHotelEstimateRequest.


        :param number_of_rooms: The number_of_rooms of this CreateHotelEstimateRequest.  # noqa: E501
        :type: int
        """

        self._number_of_rooms = number_of_rooms

    @property
    def project_id(self):
        """Gets the project_id of this CreateHotelEstimateRequest.  # noqa: E501


        :return: The project_id of this CreateHotelEstimateRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateHotelEstimateRequest.


        :param project_id: The project_id of this CreateHotelEstimateRequest.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def create_order(self):
        """Gets the create_order of this CreateHotelEstimateRequest.  # noqa: E501


        :return: The create_order of this CreateHotelEstimateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._create_order

    @create_order.setter
    def create_order(self, create_order):
        """Sets the create_order of this CreateHotelEstimateRequest.


        :param create_order: The create_order of this CreateHotelEstimateRequest.  # noqa: E501
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
                        lambda item: (
                            (item[0], item[1].to_dict())
                            if hasattr(item[1], "to_dict")
                            else item
                        ),
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
        if not isinstance(other, CreateHotelEstimateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateHotelEstimateRequest):
            return True

        return self.to_dict() != other.to_dict()
