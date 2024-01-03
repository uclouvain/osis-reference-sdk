# osis_reference_sdk.OrganizationsApi

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/reference*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organizations_history_list**](OrganizationsApi.md#organizations_history_list) | **GET** /organization/{uuid}/history | 
[**organizations_list**](OrganizationsApi.md#organizations_list) | **GET** /organization | 
[**organizations_search_duplicate**](OrganizationsApi.md#organizations_search_duplicate) | **GET** /organization/search_duplicate | 


# **organizations_history_list**
> PaginatedOrganizationHistory organizations_history_list(uuid, date)



Return a list of organizations on their current version with optional filtering.

### Example

* Api Key Authentication (Token):

```python
import time
import osis_reference_sdk
from osis_reference_sdk.api import organizations_api
from osis_reference_sdk.model.paginated_organization_history import PaginatedOrganizationHistory
from osis_reference_sdk.model.error import Error
from osis_reference_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/reference
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_reference_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/reference"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_reference_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = organizations_api.OrganizationsApi(api_client)
    uuid = "uuid_example" # str | 
    date = "date_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.organizations_history_list(uuid, date)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling OrganizationsApi->organizations_history_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.organizations_history_list(uuid, date, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling OrganizationsApi->organizations_history_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **date** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**PaginatedOrganizationHistory**](PaginatedOrganizationHistory.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_list**
> PaginatedOrganization organizations_list()



Return a list of organizations on their current version with optional filtering.

### Example

* Api Key Authentication (Token):

```python
import time
import osis_reference_sdk
from osis_reference_sdk.api import organizations_api
from osis_reference_sdk.model.paginated_organization import PaginatedOrganization
from osis_reference_sdk.model.error import Error
from osis_reference_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/reference
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_reference_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/reference"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_reference_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = organizations_api.OrganizationsApi(api_client)
    changed = "changed_example" # str |  (optional)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    limit = 25 # int | Limit of paginated results (optional)
    offset = 25 # int | Offset of paginated results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.organizations_list(changed=changed, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, limit=limit, offset=offset)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling OrganizationsApi->organizations_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **changed** | **str**|  | [optional]
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]
 **limit** | **int**| Limit of paginated results | [optional]
 **offset** | **int**| Offset of paginated results | [optional]

### Return type

[**PaginatedOrganization**](PaginatedOrganization.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_search_duplicate**
> OrganizationDuplicateScoreList organizations_search_duplicate(name, city, street, street_number, zipcode, country_iso_code)



Return a list of organizations which have a similarity with querstring args provided.

### Example

* Api Key Authentication (Token):

```python
import time
import osis_reference_sdk
from osis_reference_sdk.api import organizations_api
from osis_reference_sdk.model.organization_duplicate_score_list import OrganizationDuplicateScoreList
from osis_reference_sdk.model.error import Error
from osis_reference_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/reference
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_reference_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/reference"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_reference_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = organizations_api.OrganizationsApi(api_client)
    name = "name_example" # str | 
    city = "city_example" # str | 
    street = "street_example" # str | 
    street_number = "street_number_example" # str | 
    zipcode = "zipcode_example" # str | 
    country_iso_code = "BE" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.organizations_search_duplicate(name, city, street, street_number, zipcode, country_iso_code)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling OrganizationsApi->organizations_search_duplicate: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.organizations_search_duplicate(name, city, street, street_number, zipcode, country_iso_code, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling OrganizationsApi->organizations_search_duplicate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |
 **city** | **str**|  |
 **street** | **str**|  |
 **street_number** | **str**|  |
 **zipcode** | **str**|  |
 **country_iso_code** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**OrganizationDuplicateScoreList**](OrganizationDuplicateScoreList.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

