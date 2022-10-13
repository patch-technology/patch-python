# coding: utf-8

"""
    Patch API V2

    The core API used to integrate with Patch's service  # noqa: E501

    The version of the OpenAPI document: 2
    Contact: engineering@usepatch.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from patch_api.exceptions import ApiTypeError, ApiValueError


class TechnologyTypesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    ALLOWED_QUERY_PARAMS = [
        "mass_g",
        "total_price_cents_usd",
        "project_id",
        "page",
        "distance_m",
        "transportation_method",
        "package_mass_g",
        "create_order",
        "model",
        "make",
        "year",
        "transaction_value_btc_sats",
        "transaction_value_eth_gwei",
        "gas_used",
        "average_daily_balance_btc_sats",
        "average_daily_balance_eth_gwei",
        "timestamp",
        "origin_airport",
        "destination_airport",
        "aircraft_code",
        "cabin_class",
        "passenger_count",
        "state",
        "country_code",
        "city",
        "region",
        "star_rating",
        "number_of_nights",
        "number_of_rooms",
        "vintage_year",
        "total_price",
        "currency",
        "amount",
        "unit",
        "issued_to",
        "cargo_type",
        "container_size_code",
        "destination_country_code",
        "destination_locode",
        "destination_postal_code",
        "emissions_scope",
        "freight_mass_g",
        "freight_volume_cubic_m",
        "fuel_type",
        "number_of_containers",
        "origin_country_code",
        "origin_locode",
        "origin_postal_code",
        "truck_weight_t",
        "vessel_imo",
    ]

    def __init__(self, api_client=None):
        self.api_client = api_client

    def retrieve_technology_types(self, **kwargs):  # noqa: E501
        """Retrieves the list of technology_types  # noqa: E501

        Retrieves a list of all technology_types.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_technology_types(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int patch_version:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TechnologyTypeListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.retrieve_technology_types_with_http_info(**kwargs)  # noqa: E501

    def retrieve_technology_types_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves the list of technology_types  # noqa: E501

        Retrieves a list of all technology_types.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_technology_types_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int patch_version:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TechnologyTypeListResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["patch_version"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")
        all_params.append("mass_g")
        all_params.append("total_price_cents_usd")
        all_params.append("project_id")
        all_params.append("metadata")
        all_params.append("distance_m")
        all_params.append("transportation_method")
        all_params.append("package_mass_g")
        all_params.append("create_order")
        all_params.append("make")
        all_params.append("model")
        all_params.append("year")
        all_params.append("transaction_value_btc_sats")
        all_params.append("transaction_value_eth_gwei")
        all_params.append("gas_used")
        all_params.append("transaction_value_btc_sats")
        all_params.append("average_daily_balance_btc_sats")
        all_params.append("average_daily_balance_eth_gwei")
        all_params.append("timestamp")
        all_params.append("origin_airport")
        all_params.append("destination_airport")
        all_params.append("aircraft_code")
        all_params.append("cabin_class")
        all_params.append("passenger_count")
        all_params.append("state")
        all_params.append("country_code")
        all_params.append("city")
        all_params.append("region")
        all_params.append("star_rating")
        all_params.append("number_of_nights")
        all_params.append("number_of_rooms")
        all_params.append("vintage_year")
        all_params.append("total_price")
        all_params.append("currency")
        all_params.append("amount")
        all_params.append("unit")
        all_params.append("issued_to")
        all_params.append("cargo_type")
        all_params.append("container_size_code")
        all_params.append("destination_country_code")
        all_params.append("destination_locode")
        all_params.append("destination_postal_code")
        all_params.append("emissions_scope")
        all_params.append("freight_mass_g")
        all_params.append("freight_volume_cubic_m")
        all_params.append("fuel_type")
        all_params.append("number_of_containers")
        all_params.append("origin_country_code")
        all_params.append("origin_locode")
        all_params.append("origin_postal_code")
        all_params.append("truck_weight_t")
        all_params.append("vessel_imo")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_technology_types" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        # do not add duplicate keys to query_params list
        existing_keys = []
        for param in query_params:
            existing_keys.append(param[0])

        for key in kwargs:
            if key not in existing_keys:
                query_params.append([key, kwargs.get(key)])

        header_params = {}
        if "patch_version" in local_var_params:
            header_params["Patch-Version"] = local_var_params[
                "patch_version"
            ]  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearer_auth"]  # noqa: E501

        return self.api_client.call_api(
            "/v1/projects/technology_types",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="TechnologyTypeListResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
