# coding: utf-8

"""
    Patch API V1

    The core API used to integrate with Patch's service  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: engineering@usepatch.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from patch_api.exceptions import ApiTypeError, ApiValueError


class ProjectsApi(object):
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
        "origin_aiport",
        "destination_aiport",
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
    ]

    def __init__(self, api_client=None):
        self.api_client = api_client

    def retrieve_project(self, id={}, **kwargs):  # noqa: E501
        """Retrieves a project  # noqa: E501

        Retrieves a project available on Patch's platform.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_project(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: (required)
        :param str accept_language:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ProjectResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.retrieve_project_with_http_info(id, **kwargs)  # noqa: E501

    def retrieve_project_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieves a project  # noqa: E501

        Retrieves a project available on Patch's platform.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_project_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: (required)
        :param str accept_language:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ProjectResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["id", "accept_language"]  # noqa: E501
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

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_project" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in local_var_params or local_var_params["id"] is None:
            raise ApiValueError(
                "Missing the required parameter `id` when calling `retrieve_project`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "id" in local_var_params:
            path_params["id"] = local_var_params["id"]  # noqa: E501

        query_params = []

        # do not add duplicate keys to query_params list
        existing_keys = []
        for param in query_params:
            existing_keys.append(param[0])

        for key in kwargs:
            if key not in existing_keys:
                query_params.append([key, kwargs.get(key)])

        header_params = {}
        if "accept_language" in local_var_params:
            header_params["Accept-Language"] = local_var_params[
                "accept_language"
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
            "/v1/projects/{id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ProjectResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def retrieve_projects(self, **kwargs):  # noqa: E501
        """Retrieves a list of projects  # noqa: E501

        Retrieves a list of projects available for purchase on Patch's platform.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_projects(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int page:
        :param str country:
        :param str type:
        :param int minimum_available_mass:
        :param str accept_language:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ProjectListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.retrieve_projects_with_http_info(**kwargs)  # noqa: E501

    def retrieve_projects_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves a list of projects  # noqa: E501

        Retrieves a list of projects available for purchase on Patch's platform.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_projects_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int page:
        :param str country:
        :param str type:
        :param int minimum_available_mass:
        :param str accept_language:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ProjectListResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            "page",
            "country",
            "type",
            "minimum_available_mass",
            "accept_language",
        ]  # noqa: E501
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

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_projects" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if "page" in local_var_params:
            query_params.append(("page", local_var_params["page"]))  # noqa: E501
        if "country" in local_var_params:
            query_params.append(("country", local_var_params["country"]))  # noqa: E501
        if "type" in local_var_params:
            query_params.append(("type", local_var_params["type"]))  # noqa: E501
        if "minimum_available_mass" in local_var_params:
            query_params.append(
                ("minimum_available_mass", local_var_params["minimum_available_mass"])
            )  # noqa: E501

        # do not add duplicate keys to query_params list
        existing_keys = []
        for param in query_params:
            existing_keys.append(param[0])

        for key in kwargs:
            if key not in existing_keys:
                query_params.append([key, kwargs.get(key)])

        header_params = {}
        if "accept_language" in local_var_params:
            header_params["Accept-Language"] = local_var_params[
                "accept_language"
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
            "/v1/projects",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ProjectListResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
