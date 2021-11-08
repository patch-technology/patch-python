# coding: utf-8

"""
    Patch API V1

    The core API used to integrate with Patch's service  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: developers@usepatch.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from patch_api.exceptions import (
    ApiTypeError,
    ApiValueError
)


class PreferencesApi(object):
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
            "passenger_count"
    ]

    def __init__(self, api_client=None):
        self.api_client = api_client

    def create_preference(self, create_preference_request={}, **kwargs):  # noqa: E501
        """creates a project preference  # noqa: E501

        Creates a project preference for the given organization. If you have a `preference` in place, all of your orders will be directed to the project the preference points to.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_preference(create_preference_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CreatePreferenceRequest create_preference_request: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PreferenceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_preference_with_http_info(create_preference_request, **kwargs)  # noqa: E501

    def create_preference_with_http_info(self, create_preference_request, **kwargs):  # noqa: E501
        """creates a project preference  # noqa: E501

        Creates a project preference for the given organization. If you have a `preference` in place, all of your orders will be directed to the project the preference points to.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_preference_with_http_info(create_preference_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CreatePreferenceRequest create_preference_request: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PreferenceResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['create_preference_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('mass_g')
        all_params.append('total_price_cents_usd')
        all_params.append('project_id')
        all_params.append('metadata')
        all_params.append('distance_m')
        all_params.append('transportation_method')
        all_params.append('package_mass_g')
        all_params.append('create_order')
        all_params.append('make')
        all_params.append('model')
        all_params.append('year')
        all_params.append('transaction_value_btc_sats')
        all_params.append('transaction_value_eth_gwei')
        all_params.append('gas_used')
        all_params.append('transaction_value_btc_sats')
        all_params.append('average_daily_balance_btc_sats')
        all_params.append('average_daily_balance_eth_gwei')
        all_params.append('timestamp')
        all_params.append('origin_airport')
        all_params.append('destination_airport')
        all_params.append('aircraft_code')
        all_params.append('cabin_class')
        all_params.append('passenger_count')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_preference" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'create_preference_request' is set
        if ('create_preference_request' not in local_var_params or
                local_var_params['create_preference_request'] is None):
            raise ApiValueError("Missing the required parameter `create_preference_request` when calling `create_preference`")  # noqa: E501

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

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_preference_request' in local_var_params:
            body_params = local_var_params['create_preference_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer_auth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/preferences', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PreferenceResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_preference(self, id={}, **kwargs):  # noqa: E501
        """Deletes an organization's preference for a project  # noqa: E501

        Deletes the given `preference`. Once a preference is deleted, it cannot be undone. If you want to restore your previous preference, create a new one.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_preference(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PreferenceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_preference_with_http_info(id, **kwargs)  # noqa: E501

    def delete_preference_with_http_info(self, id, **kwargs):  # noqa: E501
        """Deletes an organization's preference for a project  # noqa: E501

        Deletes the given `preference`. Once a preference is deleted, it cannot be undone. If you want to restore your previous preference, create a new one.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_preference_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PreferenceResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('mass_g')
        all_params.append('total_price_cents_usd')
        all_params.append('project_id')
        all_params.append('metadata')
        all_params.append('distance_m')
        all_params.append('transportation_method')
        all_params.append('package_mass_g')
        all_params.append('create_order')
        all_params.append('make')
        all_params.append('model')
        all_params.append('year')
        all_params.append('transaction_value_btc_sats')
        all_params.append('transaction_value_eth_gwei')
        all_params.append('gas_used')
        all_params.append('transaction_value_btc_sats')
        all_params.append('average_daily_balance_btc_sats')
        all_params.append('average_daily_balance_eth_gwei')
        all_params.append('timestamp')
        all_params.append('origin_airport')
        all_params.append('destination_airport')
        all_params.append('aircraft_code')
        all_params.append('cabin_class')
        all_params.append('passenger_count')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_preference" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ApiValueError("Missing the required parameter `id` when calling `delete_preference`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        # do not add duplicate keys to query_params list
        existing_keys = []
        for param in query_params:
            existing_keys.append(param[0])

        for key in kwargs:
            if key not in existing_keys:
                query_params.append([key, kwargs.get(key)])

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer_auth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/preferences/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PreferenceResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_preference(self, id={}, **kwargs):  # noqa: E501
        """Retrieve the preference  # noqa: E501

        Retrieve the preference and project of an organization. You can only retrieve preferences associated with your organization.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_preference(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PreferenceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.retrieve_preference_with_http_info(id, **kwargs)  # noqa: E501

    def retrieve_preference_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieve the preference  # noqa: E501

        Retrieve the preference and project of an organization. You can only retrieve preferences associated with your organization.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_preference_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PreferenceResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('mass_g')
        all_params.append('total_price_cents_usd')
        all_params.append('project_id')
        all_params.append('metadata')
        all_params.append('distance_m')
        all_params.append('transportation_method')
        all_params.append('package_mass_g')
        all_params.append('create_order')
        all_params.append('make')
        all_params.append('model')
        all_params.append('year')
        all_params.append('transaction_value_btc_sats')
        all_params.append('transaction_value_eth_gwei')
        all_params.append('gas_used')
        all_params.append('transaction_value_btc_sats')
        all_params.append('average_daily_balance_btc_sats')
        all_params.append('average_daily_balance_eth_gwei')
        all_params.append('timestamp')
        all_params.append('origin_airport')
        all_params.append('destination_airport')
        all_params.append('aircraft_code')
        all_params.append('cabin_class')
        all_params.append('passenger_count')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_preference" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ApiValueError("Missing the required parameter `id` when calling `retrieve_preference`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        # do not add duplicate keys to query_params list
        existing_keys = []
        for param in query_params:
            existing_keys.append(param[0])

        for key in kwargs:
            if key not in existing_keys:
                query_params.append([key, kwargs.get(key)])

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer_auth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/preferences/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PreferenceResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_preferences(self, **kwargs):  # noqa: E501
        """Retrieves a list of preferences  # noqa: E501

        Retrieves a list of preferences and associated projects of an organization. You can only retrieve preferences associated with your organization.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_preferences(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int page:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PreferenceListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.retrieve_preferences_with_http_info(**kwargs)  # noqa: E501

    def retrieve_preferences_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves a list of preferences  # noqa: E501

        Retrieves a list of preferences and associated projects of an organization. You can only retrieve preferences associated with your organization.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_preferences_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int page:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PreferenceListResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('mass_g')
        all_params.append('total_price_cents_usd')
        all_params.append('project_id')
        all_params.append('metadata')
        all_params.append('distance_m')
        all_params.append('transportation_method')
        all_params.append('package_mass_g')
        all_params.append('create_order')
        all_params.append('make')
        all_params.append('model')
        all_params.append('year')
        all_params.append('transaction_value_btc_sats')
        all_params.append('transaction_value_eth_gwei')
        all_params.append('gas_used')
        all_params.append('transaction_value_btc_sats')
        all_params.append('average_daily_balance_btc_sats')
        all_params.append('average_daily_balance_eth_gwei')
        all_params.append('timestamp')
        all_params.append('origin_airport')
        all_params.append('destination_airport')
        all_params.append('aircraft_code')
        all_params.append('cabin_class')
        all_params.append('passenger_count')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_preferences" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))  # noqa: E501

        # do not add duplicate keys to query_params list
        existing_keys = []
        for param in query_params:
            existing_keys.append(param[0])

        for key in kwargs:
            if key not in existing_keys:
                query_params.append([key, kwargs.get(key)])

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer_auth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/preferences', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PreferenceListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
