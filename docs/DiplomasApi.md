# osis_reference_sdk.DiplomasApi

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/reference*

Method | HTTP request | Description
------------- | ------------- | -------------
[**diploma_read**](DiplomasApi.md#diploma_read) | **GET** /diplomas/{uuid} | 
[**diplomas_list**](DiplomasApi.md#diplomas_list) | **GET** /diplomas/ | 


# **diploma_read**
> DiplomaDetail diploma_read(uuid)



Return the detail of a diploma

### Example

* Api Key Authentication (Token):

```python
import time
import osis_reference_sdk
from osis_reference_sdk.api import diplomas_api
from osis_reference_sdk.model.error import Error
from osis_reference_sdk.model.diploma_detail import DiplomaDetail
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
    api_instance = diplomas_api.DiplomasApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.diploma_read(uuid)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling DiplomasApi->diploma_read: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.diploma_read(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling DiplomasApi->diploma_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**DiplomaDetail**](DiplomaDetail.md)

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

# **diplomas_list**
> PaginatedDiploma diplomas_list()



Return a list of diplomas with optional filtering.

### Example

* Api Key Authentication (Token):

```python
import time
import osis_reference_sdk
from osis_reference_sdk.api import diplomas_api
from osis_reference_sdk.model.error import Error
from osis_reference_sdk.model.paginated_diploma import PaginatedDiploma
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
    api_instance = diplomas_api.DiplomasApi(api_client)
    search = "search_example" # str |  (optional)
    active = True # bool |  (optional)
    study_type = "study_type_example" # str |  (optional)
    duration_type = "duration_type_example" # str |  (optional)
    cycle = "cycle_example" # str |  (optional)
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
        api_response = api_instance.diplomas_list(search=search, active=active, study_type=study_type, duration_type=duration_type, cycle=cycle, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, limit=limit, offset=offset)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling DiplomasApi->diplomas_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**|  | [optional]
 **active** | **bool**|  | [optional]
 **study_type** | **str**|  | [optional]
 **duration_type** | **str**|  | [optional]
 **cycle** | **str**|  | [optional]
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]
 **limit** | **int**| Limit of paginated results | [optional]
 **offset** | **int**| Offset of paginated results | [optional]

### Return type

[**PaginatedDiploma**](PaginatedDiploma.md)

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

