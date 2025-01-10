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
        "mechanism": "str",
        "country": "str",
        "state": "str",
        "issuance_type": "str",
        "latitude": "float",
        "longitude": "float",
        "project_partner": "str",
        "photos": "list[Photo]",
        "verifier": "str",
        "standard": "Standard",
        "sdgs": "list[Sdg]",
        "tagline": "str",
        "technology_type": "TechnologyType",
        "highlights": "list[Highlight]",
        "inventory": "list[Inventory]",
        "disclaimers": "list[Disclaimer]",
    }

    attribute_map = {
        "id": "id",
        "production": "production",
        "name": "name",
        "description": "description",
        "mechanism": "mechanism",
        "country": "country",
        "state": "state",
        "issuance_type": "issuance_type",
        "latitude": "latitude",
        "longitude": "longitude",
        "project_partner": "project_partner",
        "photos": "photos",
        "verifier": "verifier",
        "standard": "standard",
        "sdgs": "sdgs",
        "tagline": "tagline",
        "technology_type": "technology_type",
        "highlights": "highlights",
        "inventory": "inventory",
        "disclaimers": "disclaimers",
    }

    def __init__(
        self,
        id=None,
        production=None,
        name=None,
        description=None,
        mechanism=None,
        country=None,
        state=None,
        issuance_type=None,
        latitude=None,
        longitude=None,
        project_partner=None,
        photos=None,
        verifier=None,
        standard=None,
        sdgs=None,
        tagline=None,
        technology_type=None,
        highlights=None,
        inventory=None,
        disclaimers=None,
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
        self._mechanism = None
        self._country = None
        self._state = None
        self._issuance_type = None
        self._latitude = None
        self._longitude = None
        self._project_partner = None
        self._photos = None
        self._verifier = None
        self._standard = None
        self._sdgs = None
        self._tagline = None
        self._technology_type = None
        self._highlights = None
        self._inventory = None
        self._disclaimers = None
        self.discriminator = None

        self.id = id
        self.production = production
        self.name = name
        self.description = description
        if mechanism is not None:
            self.mechanism = mechanism
        self.country = country
        self.state = state
        if issuance_type is not None:
            self.issuance_type = issuance_type
        self.latitude = latitude
        self.longitude = longitude
        self.project_partner = project_partner
        self.photos = photos
        if verifier is not None:
            self.verifier = verifier
        self.standard = standard
        self.sdgs = sdgs
        if tagline is not None:
            self.tagline = tagline
        self.technology_type = technology_type
        self.highlights = highlights
        self.inventory = inventory
        if disclaimers is not None:
            self.disclaimers = disclaimers

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

        A boolean indicating if this project is a production or demo mode project.  # noqa: E501

        :return: The production of this Project.  # noqa: E501
        :rtype: bool
        """
        return self._production

    @production.setter
    def production(self, production):
        """Sets the production of this Project.

        A boolean indicating if this project is a production or demo mode project.  # noqa: E501

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
    def mechanism(self):
        """Gets the mechanism of this Project.  # noqa: E501

        The mechanism of the project. One of: removal, avoidance, avoidance_and_removal.  # noqa: E501

        :return: The mechanism of this Project.  # noqa: E501
        :rtype: str
        """
        return self._mechanism

    @mechanism.setter
    def mechanism(self, mechanism):
        """Sets the mechanism of this Project.

        The mechanism of the project. One of: removal, avoidance, avoidance_and_removal.  # noqa: E501

        :param mechanism: The mechanism of this Project.  # noqa: E501
        :type: str
        """

        self._mechanism = mechanism

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
    def state(self):
        """Gets the state of this Project.  # noqa: E501

        The state where this project is located.  # noqa: E501

        :return: The state of this Project.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Project.

        The state where this project is located.  # noqa: E501

        :param state: The state of this Project.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def issuance_type(self):
        """Gets the issuance_type of this Project.  # noqa: E501

        The issuance type of the project. One of: ex-ante, ex-post.  # noqa: E501

        :return: The issuance_type of this Project.  # noqa: E501
        :rtype: str
        """
        return self._issuance_type

    @issuance_type.setter
    def issuance_type(self, issuance_type):
        """Sets the issuance_type of this Project.

        The issuance type of the project. One of: ex-ante, ex-post.  # noqa: E501

        :param issuance_type: The issuance_type of this Project.  # noqa: E501
        :type: str
        """
        allowed_values = ["ex-ante", "ex-post"]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and issuance_type not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `issuance_type` ({0}), must be one of {1}".format(  # noqa: E501
                    issuance_type, allowed_values
                )
            )

        self._issuance_type = issuance_type

    @property
    def latitude(self):
        """Gets the latitude of this Project.  # noqa: E501

        The latitude at which this project is located.  # noqa: E501

        :return: The latitude of this Project.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this Project.

        The latitude at which this project is located.  # noqa: E501

        :param latitude: The latitude of this Project.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this Project.  # noqa: E501

        The longitude at which this project is located.  # noqa: E501

        :return: The longitude of this Project.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this Project.

        The longitude at which this project is located.  # noqa: E501

        :param longitude: The longitude of this Project.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def project_partner(self):
        """Gets the project_partner of this Project.  # noqa: E501

        The name of the project project partner.  # noqa: E501

        :return: The project_partner of this Project.  # noqa: E501
        :rtype: str
        """
        return self._project_partner

    @project_partner.setter
    def project_partner(self, project_partner):
        """Sets the project_partner of this Project.

        The name of the project project partner.  # noqa: E501

        :param project_partner: The project_partner of this Project.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and project_partner is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `project_partner`, must not be `None`"
            )  # noqa: E501

        self._project_partner = project_partner

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
    def verifier(self):
        """Gets the verifier of this Project.  # noqa: E501

        The name of the project verifier, when applicable. A verifier is the organization that verifies the calculations of the actual amount of greenhouse gas emissions that have been avoided or sequestered through implementation of the project.  # noqa: E501

        :return: The verifier of this Project.  # noqa: E501
        :rtype: str
        """
        return self._verifier

    @verifier.setter
    def verifier(self, verifier):
        """Sets the verifier of this Project.

        The name of the project verifier, when applicable. A verifier is the organization that verifies the calculations of the actual amount of greenhouse gas emissions that have been avoided or sequestered through implementation of the project.  # noqa: E501

        :param verifier: The verifier of this Project.  # noqa: E501
        :type: str
        """

        self._verifier = verifier

    @property
    def standard(self):
        """Gets the standard of this Project.  # noqa: E501

        An object returning the Standard associated with this project, when applicable. Standards provide guidance on GHG quantification, monitoring, and reporting. Standards can include protocols/methodologies and guidance documents.  # noqa: E501

        :return: The standard of this Project.  # noqa: E501
        :rtype: Standard
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        """Sets the standard of this Project.

        An object returning the Standard associated with this project, when applicable. Standards provide guidance on GHG quantification, monitoring, and reporting. Standards can include protocols/methodologies and guidance documents.  # noqa: E501

        :param standard: The standard of this Project.  # noqa: E501
        :type: Standard
        """

        self._standard = standard

    @property
    def sdgs(self):
        """Gets the sdgs of this Project.  # noqa: E501

        An array returning the UN Sustainable Development Goals associated with this project.  # noqa: E501

        :return: The sdgs of this Project.  # noqa: E501
        :rtype: list[Sdg]
        """
        return self._sdgs

    @sdgs.setter
    def sdgs(self, sdgs):
        """Sets the sdgs of this Project.

        An array returning the UN Sustainable Development Goals associated with this project.  # noqa: E501

        :param sdgs: The sdgs of this Project.  # noqa: E501
        :type: list[Sdg]
        """

        self._sdgs = sdgs

    @property
    def tagline(self):
        """Gets the tagline of this Project.  # noqa: E501

        A short description of the project.  # noqa: E501

        :return: The tagline of this Project.  # noqa: E501
        :rtype: str
        """
        return self._tagline

    @tagline.setter
    def tagline(self, tagline):
        """Sets the tagline of this Project.

        A short description of the project.  # noqa: E501

        :param tagline: The tagline of this Project.  # noqa: E501
        :type: str
        """

        self._tagline = tagline

    @property
    def technology_type(self):
        """Gets the technology_type of this Project.  # noqa: E501


        :return: The technology_type of this Project.  # noqa: E501
        :rtype: TechnologyType
        """
        return self._technology_type

    @technology_type.setter
    def technology_type(self, technology_type):
        """Sets the technology_type of this Project.


        :param technology_type: The technology_type of this Project.  # noqa: E501
        :type: TechnologyType
        """
        if (
            self.local_vars_configuration.client_side_validation
            and technology_type is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `technology_type`, must not be `None`"
            )  # noqa: E501

        self._technology_type = technology_type

    @property
    def highlights(self):
        """Gets the highlights of this Project.  # noqa: E501

        DEPRECATED. An array of objects containing the highlight's slug, title, and a URL for the corresponding icon. A highlight's title is a short string that spotlights a characteristic about the project. Highlights are deprecated and not populated for recent projects.  # noqa: E501

        :return: The highlights of this Project.  # noqa: E501
        :rtype: list[Highlight]
        """
        return self._highlights

    @highlights.setter
    def highlights(self, highlights):
        """Sets the highlights of this Project.

        DEPRECATED. An array of objects containing the highlight's slug, title, and a URL for the corresponding icon. A highlight's title is a short string that spotlights a characteristic about the project. Highlights are deprecated and not populated for recent projects.  # noqa: E501

        :param highlights: The highlights of this Project.  # noqa: E501
        :type: list[Highlight]
        """
        if (
            self.local_vars_configuration.client_side_validation and highlights is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `highlights`, must not be `None`"
            )  # noqa: E501

        self._highlights = highlights

    @property
    def inventory(self):
        """Gets the inventory of this Project.  # noqa: E501

        An array of objects containing available inventory for a project. Available inventory is grouped by a project's vintage year and returns amount and pricing available for a given vintage year.  # noqa: E501

        :return: The inventory of this Project.  # noqa: E501
        :rtype: list[Inventory]
        """
        return self._inventory

    @inventory.setter
    def inventory(self, inventory):
        """Sets the inventory of this Project.

        An array of objects containing available inventory for a project. Available inventory is grouped by a project's vintage year and returns amount and pricing available for a given vintage year.  # noqa: E501

        :param inventory: The inventory of this Project.  # noqa: E501
        :type: list[Inventory]
        """
        if (
            self.local_vars_configuration.client_side_validation and inventory is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `inventory`, must not be `None`"
            )  # noqa: E501

        self._inventory = inventory

    @property
    def disclaimers(self):
        """Gets the disclaimers of this Project.  # noqa: E501

        An array of objects containing disclaimers about the project. Information, warnings, and critical concerns may be present.  # noqa: E501

        :return: The disclaimers of this Project.  # noqa: E501
        :rtype: list[Disclaimer]
        """
        return self._disclaimers

    @disclaimers.setter
    def disclaimers(self, disclaimers):
        """Sets the disclaimers of this Project.

        An array of objects containing disclaimers about the project. Information, warnings, and critical concerns may be present.  # noqa: E501

        :param disclaimers: The disclaimers of this Project.  # noqa: E501
        :type: list[Disclaimer]
        """

        self._disclaimers = disclaimers

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
        if not isinstance(other, Project):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Project):
            return True

        return self.to_dict() != other.to_dict()
