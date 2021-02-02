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


class Project(object):
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
        "id": "str",
        "production": "bool",
        "name": "str",
        "description": "str",
        "type": "str",
        "country": "str",
        "developer": "str",
        "photos": "list[Photo]",
        "average_price_per_tonne_cents_usd": "int",
        "remaining_mass_g": "int",
        "standard": "Standard",
    }

    attribute_map = {
        "id": "id",
        "production": "production",
        "name": "name",
        "description": "description",
        "type": "type",
        "country": "country",
        "developer": "developer",
        "photos": "photos",
        "average_price_per_tonne_cents_usd": "average_price_per_tonne_cents_usd",
        "remaining_mass_g": "remaining_mass_g",
        "standard": "standard",
    }

    def __init__(
        self,
        id=None,
        production=None,
        name=None,
        description=None,
        type=None,
        country=None,
        developer=None,
        photos=None,
        average_price_per_tonne_cents_usd=None,
        remaining_mass_g=None,
        standard=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """Project - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._production = None
        self._name = None
        self._description = None
        self._type = None
        self._country = None
        self._developer = None
        self._photos = None
        self._average_price_per_tonne_cents_usd = None
        self._remaining_mass_g = None
        self._standard = None
        self.discriminator = None

        self.id = id
        self.production = production
        self.name = name
        self.description = description
        if type is not None:
            self.type = type
        self.country = country
        self.developer = developer
        self.photos = photos
        self.average_price_per_tonne_cents_usd = average_price_per_tonne_cents_usd
        self.remaining_mass_g = remaining_mass_g
        self.standard = standard

    @property
    def id(self):
        """Gets the id of this Project.  # noqa: E501

        A unique uid for the record. UIDs will be prepended by pro_prod or pro_test depending on the mode it was created in.  # noqa: E501

        :return: The id of this Project.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Project.

        A unique uid for the record. UIDs will be prepended by pro_prod or pro_test depending on the mode it was created in.  # noqa: E501

        :param id: The id of this Project.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and id is None
        ):  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def production(self):
        """Gets the production of this Project.  # noqa: E501

        A boolean indicating if this project is a production or test mode project.  # noqa: E501

        :return: The production of this Project.  # noqa: E501
        :rtype: bool
        """
        return self._production

    @production.setter
    def production(self, production):
        """Sets the production of this Project.

        A boolean indicating if this project is a production or test mode project.  # noqa: E501

        :param production: The production of this Project.  # noqa: E501
        :type: bool
        """
        if (
            self.local_vars_configuration.client_side_validation and production is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `production`, must not be `None`"
            )  # noqa: E501

        self._production = production

    @property
    def name(self):
        """Gets the name of this Project.  # noqa: E501

        The name of the project.  # noqa: E501

        :return: The name of this Project.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Project.

        The name of the project.  # noqa: E501

        :param name: The name of this Project.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and name is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `name`, must not be `None`"
            )  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Project.  # noqa: E501

        The description of the project.  # noqa: E501

        :return: The description of this Project.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Project.

        The description of the project.  # noqa: E501

        :param description: The description of this Project.  # noqa: E501
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
    def type(self):
        """Gets the type of this Project.  # noqa: E501

        The type of carbon removal project, currently available project types are Biomass, Dac, Forestry, Mineralization, Ocean, Soil.  # noqa: E501

        :return: The type of this Project.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Project.

        The type of carbon removal project, currently available project types are Biomass, Dac, Forestry, Mineralization, Ocean, Soil.  # noqa: E501

        :param type: The type of this Project.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "biomass",
            "dac",
            "forestry",
            "mineralization",
            "ocean",
            "soil",
        ]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and type not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}".format(  # noqa: E501
                    type, allowed_values
                )
            )

        self._type = type

    @property
    def country(self):
        """Gets the country of this Project.  # noqa: E501

        The country of origin of the project.  # noqa: E501

        :return: The country of this Project.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Project.

        The country of origin of the project.  # noqa: E501

        :param country: The country of this Project.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and country is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `country`, must not be `None`"
            )  # noqa: E501

        self._country = country

    @property
    def developer(self):
        """Gets the developer of this Project.  # noqa: E501

        The name of the project developer.  # noqa: E501

        :return: The developer of this Project.  # noqa: E501
        :rtype: str
        """
        return self._developer

    @developer.setter
    def developer(self, developer):
        """Sets the developer of this Project.

        The name of the project developer.  # noqa: E501

        :param developer: The developer of this Project.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and developer is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `developer`, must not be `None`"
            )  # noqa: E501

        self._developer = developer

    @property
    def photos(self):
        """Gets the photos of this Project.  # noqa: E501

        An array of URLs for photos of the project.  # noqa: E501

        :return: The photos of this Project.  # noqa: E501
        :rtype: list[Photo]
        """
        return self._photos

    @photos.setter
    def photos(self, photos):
        """Sets the photos of this Project.

        An array of URLs for photos of the project.  # noqa: E501

        :param photos: The photos of this Project.  # noqa: E501
        :type: list[Photo]
        """

        self._photos = photos

    @property
    def average_price_per_tonne_cents_usd(self):
        """Gets the average_price_per_tonne_cents_usd of this Project.  # noqa: E501

        The average price per tonne in USD cents for carbon offsets supplied by this project.  # noqa: E501

        :return: The average_price_per_tonne_cents_usd of this Project.  # noqa: E501
        :rtype: int
        """
        return self._average_price_per_tonne_cents_usd

    @average_price_per_tonne_cents_usd.setter
    def average_price_per_tonne_cents_usd(self, average_price_per_tonne_cents_usd):
        """Sets the average_price_per_tonne_cents_usd of this Project.

        The average price per tonne in USD cents for carbon offsets supplied by this project.  # noqa: E501

        :param average_price_per_tonne_cents_usd: The average_price_per_tonne_cents_usd of this Project.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and average_price_per_tonne_cents_usd is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `average_price_per_tonne_cents_usd`, must not be `None`"
            )  # noqa: E501

        self._average_price_per_tonne_cents_usd = average_price_per_tonne_cents_usd

    @property
    def remaining_mass_g(self):
        """Gets the remaining_mass_g of this Project.  # noqa: E501

        The remaining mass in grams available for purchase for this project.  # noqa: E501

        :return: The remaining_mass_g of this Project.  # noqa: E501
        :rtype: int
        """
        return self._remaining_mass_g

    @remaining_mass_g.setter
    def remaining_mass_g(self, remaining_mass_g):
        """Sets the remaining_mass_g of this Project.

        The remaining mass in grams available for purchase for this project.  # noqa: E501

        :param remaining_mass_g: The remaining_mass_g of this Project.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and remaining_mass_g is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `remaining_mass_g`, must not be `None`"
            )  # noqa: E501

        self._remaining_mass_g = remaining_mass_g

    @property
    def standard(self):
        """Gets the standard of this Project.  # noqa: E501

        An object returning the Standard associated with this project.  # noqa: E501

        :return: The standard of this Project.  # noqa: E501
        :rtype: Standard
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        """Sets the standard of this Project.

        An object returning the Standard associated with this project.  # noqa: E501

        :param standard: The standard of this Project.  # noqa: E501
        :type: Standard
        """

        self._standard = standard

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
        if not isinstance(other, Project):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Project):
            return True

        return self.to_dict() != other.to_dict()
