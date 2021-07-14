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

from patch_api.exceptions import ApiTypeError, ApiValueError


class OrdersApi(object):
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
        "timestamp",
    ]

    def __init__(self, api_client=None):
        self.api_client = api_client

    def cancel_order(self, id={}, **kwargs):  # noqa: E501
        """Cancel an order  # noqa: E501

        Cancelling an order removes the associated offset allocation from an order. You will not be charged for cancelled orders. Only orders in the `draft` or `placed` state can be cancelled.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_order(id, async_req=True)
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
        :return: OrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.cancel_order_with_http_info(id, **kwargs)  # noqa: E501

    def cancel_order_with_http_info(self, id, **kwargs):  # noqa: E501
        """Cancel an order  # noqa: E501

        Cancelling an order removes the associated offset allocation from an order. You will not be charged for cancelled orders. Only orders in the `draft` or `placed` state can be cancelled.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_order_with_http_info(id, async_req=True)
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
        :return: tuple(OrderResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["id"]  # noqa: E501
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
        all_params.append("timestamp")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_order" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in local_var_params or local_var_params["id"] is None:
            raise ApiValueError(
                "Missing the required parameter `id` when calling `cancel_order`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "id" in local_var_params:
            path_params["id"] = local_var_params["id"]  # noqa: E501

        query_params = []
        for key in kwargs:
            query_params.append([key, kwargs.get(key)])

        header_params = {}

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
            "/v1/orders/{id}/cancel",
            "PATCH",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="OrderResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def create_order(self, create_order_request={}, **kwargs):  # noqa: E501
        """Creates an order  # noqa: E501

        Creates an order in the `placed` state. To create a `draft` order, create an estimate first.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_order(create_order_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CreateOrderRequest create_order_request: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: OrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.create_order_with_http_info(
            create_order_request, **kwargs
        )  # noqa: E501

    def create_order_with_http_info(self, create_order_request, **kwargs):  # noqa: E501
        """Creates an order  # noqa: E501

        Creates an order in the `placed` state. To create a `draft` order, create an estimate first.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_order_with_http_info(create_order_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CreateOrderRequest create_order_request: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(OrderResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["create_order_request"]  # noqa: E501
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
        all_params.append("timestamp")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_order" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'create_order_request' is set
        if (
            "create_order_request" not in local_var_params
            or local_var_params["create_order_request"] is None
        ):
            raise ApiValueError(
                "Missing the required parameter `create_order_request` when calling `create_order`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        for key in kwargs:
            query_params.append([key, kwargs.get(key)])

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "create_order_request" in local_var_params:
            body_params = local_var_params["create_order_request"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearer_auth"]  # noqa: E501

        return self.api_client.call_api(
            "/v1/orders",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="OrderResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def place_order(self, id={}, **kwargs):  # noqa: E501
        """Place an order  # noqa: E501

        Placing an order confirms an order's allocation of offsets. Only orders that are in the `draft` state can be placed   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.place_order(id, async_req=True)
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
        :return: OrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.place_order_with_http_info(id, **kwargs)  # noqa: E501

    def place_order_with_http_info(self, id, **kwargs):  # noqa: E501
        """Place an order  # noqa: E501

        Placing an order confirms an order's allocation of offsets. Only orders that are in the `draft` state can be placed   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.place_order_with_http_info(id, async_req=True)
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
        :return: tuple(OrderResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["id"]  # noqa: E501
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
        all_params.append("timestamp")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method place_order" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in local_var_params or local_var_params["id"] is None:
            raise ApiValueError(
                "Missing the required parameter `id` when calling `place_order`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "id" in local_var_params:
            path_params["id"] = local_var_params["id"]  # noqa: E501

        query_params = []
        for key in kwargs:
            query_params.append([key, kwargs.get(key)])

        header_params = {}

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
            "/v1/orders/{id}/place",
            "PATCH",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="OrderResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def retrieve_order(self, id={}, **kwargs):  # noqa: E501
        """Retrieves an order  # noqa: E501

        Retrieves a given order and its allocation offsets or negative emissions. You can only retrieve orders associated with the organization you are querying for.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_order(id, async_req=True)
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
        :return: OrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.retrieve_order_with_http_info(id, **kwargs)  # noqa: E501

    def retrieve_order_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieves an order  # noqa: E501

        Retrieves a given order and its allocation offsets or negative emissions. You can only retrieve orders associated with the organization you are querying for.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_order_with_http_info(id, async_req=True)
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
        :return: tuple(OrderResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["id"]  # noqa: E501
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
        all_params.append("timestamp")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_order" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in local_var_params or local_var_params["id"] is None:
            raise ApiValueError(
                "Missing the required parameter `id` when calling `retrieve_order`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "id" in local_var_params:
            path_params["id"] = local_var_params["id"]  # noqa: E501

        query_params = []
        for key in kwargs:
            query_params.append([key, kwargs.get(key)])

        header_params = {}

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
            "/v1/orders/{id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="OrderResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def retrieve_orders(self, **kwargs):  # noqa: E501
        """Retrieves a list of orders  # noqa: E501

        Retrieves a list of orders and its allocation offsets or negative emissions. You can only retrieve orders associated with the organization you are querying for.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_orders(async_req=True)
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
        :return: OrderListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.retrieve_orders_with_http_info(**kwargs)  # noqa: E501

    def retrieve_orders_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves a list of orders  # noqa: E501

        Retrieves a list of orders and its allocation offsets or negative emissions. You can only retrieve orders associated with the organization you are querying for.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_orders_with_http_info(async_req=True)
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
        :return: tuple(OrderListResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["page"]  # noqa: E501
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
        all_params.append("timestamp")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_orders" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        for key in kwargs:
            query_params.append([key, kwargs.get(key)])
        if "page" in local_var_params:
            query_params.append(("page", local_var_params["page"]))  # noqa: E501

        header_params = {}

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
            "/v1/orders",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="OrderListResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
