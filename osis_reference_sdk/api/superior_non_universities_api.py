"""
    Reference Service

    A set of API endpoints that allow you to get reference data.  # noqa: E501

    The version of the OpenAPI document: 1.31
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from osis_reference_sdk.api_client import ApiClient, Endpoint as _Endpoint
from osis_reference_sdk.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from osis_reference_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_reference_sdk.model.error import Error
from osis_reference_sdk.model.paginated_superior_non_university import PaginatedSuperiorNonUniversity
from osis_reference_sdk.model.superior_non_university_detail import SuperiorNonUniversityDetail


class SuperiorNonUniversitiesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.superior_non_universities_list_endpoint = _Endpoint(
            settings={
                'response_type': (PaginatedSuperiorNonUniversity,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/superior_non_universities',
                'operation_id': 'superior_non_universities_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'search',
                    'name',
                    'zipcode',
                    'city',
                    'active',
                    'community',
                    'country_iso_code',
                    'accept_language',
                    'x_user_first_name',
                    'x_user_last_name',
                    'x_user_email',
                    'x_user_global_id',
                    'limit',
                    'offset',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'search':
                        (str,),
                    'name':
                        (str,),
                    'zipcode':
                        (str,),
                    'city':
                        (str,),
                    'active':
                        (bool,),
                    'community':
                        (str,),
                    'country_iso_code':
                        (str,),
                    'accept_language':
                        (AcceptedLanguageEnum,),
                    'x_user_first_name':
                        (str,),
                    'x_user_last_name':
                        (str,),
                    'x_user_email':
                        (str,),
                    'x_user_global_id':
                        (str,),
                    'limit':
                        (int,),
                    'offset':
                        (int,),
                },
                'attribute_map': {
                    'search': 'search',
                    'name': 'name',
                    'zipcode': 'zipcode',
                    'city': 'city',
                    'active': 'active',
                    'community': 'community',
                    'country_iso_code': 'country_iso_code',
                    'accept_language': 'Accept-Language',
                    'x_user_first_name': 'X-User-FirstName',
                    'x_user_last_name': 'X-User-LastName',
                    'x_user_email': 'X-User-Email',
                    'x_user_global_id': 'X-User-GlobalID',
                    'limit': 'limit',
                    'offset': 'offset',
                },
                'location_map': {
                    'search': 'query',
                    'name': 'query',
                    'zipcode': 'query',
                    'city': 'query',
                    'active': 'query',
                    'community': 'query',
                    'country_iso_code': 'query',
                    'accept_language': 'header',
                    'x_user_first_name': 'header',
                    'x_user_last_name': 'header',
                    'x_user_email': 'header',
                    'x_user_global_id': 'header',
                    'limit': 'query',
                    'offset': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.superior_non_university_read_endpoint = _Endpoint(
            settings={
                'response_type': (SuperiorNonUniversityDetail,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/superior_non_universities/{uuid}',
                'operation_id': 'superior_non_university_read',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'uuid',
                    'accept_language',
                    'x_user_first_name',
                    'x_user_last_name',
                    'x_user_email',
                    'x_user_global_id',
                ],
                'required': [
                    'uuid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'uuid':
                        (str,),
                    'accept_language':
                        (AcceptedLanguageEnum,),
                    'x_user_first_name':
                        (str,),
                    'x_user_last_name':
                        (str,),
                    'x_user_email':
                        (str,),
                    'x_user_global_id':
                        (str,),
                },
                'attribute_map': {
                    'uuid': 'uuid',
                    'accept_language': 'Accept-Language',
                    'x_user_first_name': 'X-User-FirstName',
                    'x_user_last_name': 'X-User-LastName',
                    'x_user_email': 'X-User-Email',
                    'x_user_global_id': 'X-User-GlobalID',
                },
                'location_map': {
                    'uuid': 'path',
                    'accept_language': 'header',
                    'x_user_first_name': 'header',
                    'x_user_last_name': 'header',
                    'x_user_email': 'header',
                    'x_user_global_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def superior_non_universities_list(
        self,
        **kwargs
    ):
        """superior_non_universities_list  # noqa: E501

        Return a list of superior non universities with optional filtering.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.superior_non_universities_list(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            search (str): [optional]
            name (str): [optional]
            zipcode (str): [optional]
            city (str): [optional]
            active (bool): [optional]
            community (str): [optional]
            country_iso_code (str): [optional]
            accept_language (AcceptedLanguageEnum): The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) . [optional]
            x_user_first_name (str): [optional]
            x_user_last_name (str): [optional]
            x_user_email (str): [optional]
            x_user_global_id (str): [optional]
            limit (int): Limit of paginated results. [optional]
            offset (int): Offset of paginated results. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            PaginatedSuperiorNonUniversity
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.superior_non_universities_list_endpoint.call_with_http_info(**kwargs)

    def superior_non_university_read(
        self,
        uuid,
        **kwargs
    ):
        """superior_non_university_read  # noqa: E501

        Return the detail of superior non university  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.superior_non_university_read(uuid, async_req=True)
        >>> result = thread.get()

        Args:
            uuid (str):

        Keyword Args:
            accept_language (AcceptedLanguageEnum): The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) . [optional]
            x_user_first_name (str): [optional]
            x_user_last_name (str): [optional]
            x_user_email (str): [optional]
            x_user_global_id (str): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            SuperiorNonUniversityDetail
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['uuid'] = \
            uuid
        return self.superior_non_university_read_endpoint.call_with_http_info(**kwargs)

