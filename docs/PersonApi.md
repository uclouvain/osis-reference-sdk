# osis_reference_sdk.PersonApi

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/admission*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_language_knowledge**](PersonApi.md#create_language_knowledge) | **POST** /languages_knowledge | 
[**list_language_knowledges**](PersonApi.md#list_language_knowledges) | **GET** /languages_knowledge | 
[**retrieve_coordonnees**](PersonApi.md#retrieve_coordonnees) | **GET** /coordonnees | 
[**retrieve_coordonnees_admission**](PersonApi.md#retrieve_coordonnees_admission) | **GET** /propositions/{uuid}/coordonnees | 
[**retrieve_high_school_diploma**](PersonApi.md#retrieve_high_school_diploma) | **GET** /secondary_studies | 
[**retrieve_high_school_diploma_admission**](PersonApi.md#retrieve_high_school_diploma_admission) | **GET** /propositions/{uuid}/secondary_studies | 
[**retrieve_person_identification**](PersonApi.md#retrieve_person_identification) | **GET** /person | 
[**retrieve_person_identification_admission**](PersonApi.md#retrieve_person_identification_admission) | **GET** /propositions/{uuid}/person | 
[**update_coordonnees**](PersonApi.md#update_coordonnees) | **PUT** /coordonnees | 
[**update_coordonnees_admission**](PersonApi.md#update_coordonnees_admission) | **PUT** /propositions/{uuid}/coordonnees | 
[**update_high_school_diploma**](PersonApi.md#update_high_school_diploma) | **PUT** /secondary_studies | 
[**update_high_school_diploma_admission**](PersonApi.md#update_high_school_diploma_admission) | **PUT** /propositions/{uuid}/secondary_studies | 
[**update_person_identification**](PersonApi.md#update_person_identification) | **PUT** /person | 
[**update_person_identification_admission**](PersonApi.md#update_person_identification_admission) | **PUT** /propositions/{uuid}/person | 


# **create_language_knowledge**
> [LanguageKnowledge] create_language_knowledge()



### Example

* Api Key Authentication (Token):
```python
import time
import osis_reference_sdk
from osis_reference_sdk.api import person_api
from osis_reference_sdk.model.error import Error
from osis_reference_sdk.model.language_knowledge import LanguageKnowledge
from osis_reference_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/admission
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_reference_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/admission"
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
    api_instance = person_api.PersonApi(api_client)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    language_knowledge = [
        LanguageKnowledge(
            language="language_example",
            listening_comprehension=LanguageKnowledgeGrade("A1"),
            speaking_ability=LanguageKnowledgeGrade("A1"),
            writing_ability=LanguageKnowledgeGrade("A1"),
        ),
    ] # [LanguageKnowledge] |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_language_knowledge(accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, language_knowledge=language_knowledge)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PersonApi->create_language_knowledge: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]
 **language_knowledge** | [**[LanguageKnowledge]**](LanguageKnowledge.md)|  | [optional]

### Return type

[**[LanguageKnowledge]**](LanguageKnowledge.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_language_knowledges**
> [LanguageKnowledge] list_language_knowledges()



### Example

* Api Key Authentication (Token):
```python
import time
import osis_reference_sdk
from osis_reference_sdk.api import person_api
from osis_reference_sdk.model.error import Error
from osis_reference_sdk.model.language_knowledge import LanguageKnowledge
from osis_reference_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/admission
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_reference_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/admission"
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
    api_instance = person_api.PersonApi(api_client)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_language_knowledges(accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PersonApi->list_language_knowledges: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**[LanguageKnowledge]**](LanguageKnowledge.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_coordonnees**
> Coordonnees retrieve_coordonnees()



### Example

* Api Key Authentication (Token):
```python
import time
import osis_reference_sdk
from osis_reference_sdk.api import person_api
from osis_reference_sdk.model.coordonnees import Coordonnees
from osis_reference_sdk.model.error import Error
from osis_reference_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/admission
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_reference_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/admission"
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
    api_instance = person_api.PersonApi(api_client)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.retrieve_coordonnees(accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PersonApi->retrieve_coordonnees: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**Coordonnees**](Coordonnees.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_coordonnees_admission**
> Coordonnees retrieve_coordonnees_admission(uuid)



### Example

* Api Key Authentication (Token):
```python
import time
import osis_reference_sdk
from osis_reference_sdk.api import person_api
from osis_reference_sdk.model.coordonnees import Coordonnees
from osis_reference_sdk.model.error import Error
from osis_reference_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/admission
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_reference_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/admission"
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
    api_instance = person_api.PersonApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_coordonnees_admission(uuid)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PersonApi->retrieve_coordonnees_admission: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.retrieve_coordonnees_admission(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PersonApi->retrieve_coordonnees_admission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**Coordonnees**](Coordonnees.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_high_school_diploma**
> HighSchoolDiploma retrieve_high_school_diploma()



### Example

* Api Key Authentication (Token):
```python
import time
import osis_reference_sdk
from osis_reference_sdk.api import person_api
from osis_reference_sdk.model.high_school_diploma import HighSchoolDiploma
from osis_reference_sdk.model.error import Error
from osis_reference_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/admission
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_reference_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/admission"
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
    api_instance = person_api.PersonApi(api_client)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.retrieve_high_school_diploma(accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PersonApi->retrieve_high_school_diploma: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**HighSchoolDiploma**](HighSchoolDiploma.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_high_school_diploma_admission**
> HighSchoolDiploma retrieve_high_school_diploma_admission(uuid)



### Example

* Api Key Authentication (Token):
```python
import time
import osis_reference_sdk
from osis_reference_sdk.api import person_api
from osis_reference_sdk.model.high_school_diploma import HighSchoolDiploma
from osis_reference_sdk.model.error import Error
from osis_reference_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/admission
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_reference_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/admission"
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
    api_instance = person_api.PersonApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_high_school_diploma_admission(uuid)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PersonApi->retrieve_high_school_diploma_admission: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.retrieve_high_school_diploma_admission(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PersonApi->retrieve_high_school_diploma_admission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**HighSchoolDiploma**](HighSchoolDiploma.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_person_identification**
> PersonIdentification retrieve_person_identification()



### Example

* Api Key Authentication (Token):
```python
import time
import osis_reference_sdk
from osis_reference_sdk.api import person_api
from osis_reference_sdk.model.person_identification import PersonIdentification
from osis_reference_sdk.model.error import Error
from osis_reference_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/admission
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_reference_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/admission"
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
    api_instance = person_api.PersonApi(api_client)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.retrieve_person_identification(accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PersonApi->retrieve_person_identification: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**PersonIdentification**](PersonIdentification.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_person_identification_admission**
> PersonIdentification retrieve_person_identification_admission(uuid)



### Example

* Api Key Authentication (Token):
```python
import time
import osis_reference_sdk
from osis_reference_sdk.api import person_api
from osis_reference_sdk.model.person_identification import PersonIdentification
from osis_reference_sdk.model.error import Error
from osis_reference_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/admission
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_reference_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/admission"
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
    api_instance = person_api.PersonApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_person_identification_admission(uuid)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PersonApi->retrieve_person_identification_admission: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.retrieve_person_identification_admission(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PersonApi->retrieve_person_identification_admission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**PersonIdentification**](PersonIdentification.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_coordonnees**
> Coordonnees update_coordonnees()



### Example

* Api Key Authentication (Token):
```python
import time
import osis_reference_sdk
from osis_reference_sdk.api import person_api
from osis_reference_sdk.model.coordonnees import Coordonnees
from osis_reference_sdk.model.error import Error
from osis_reference_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/admission
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_reference_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/admission"
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
    api_instance = person_api.PersonApi(api_client)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    coordonnees = Coordonnees(
        contact=CoordonneesContact(
            location="location_example",
            postal_code="postal_code_example",
            city="city_example",
            country="country_example",
            street="street_example",
            street_number="street_number_example",
            postal_box="postal_box_example",
            place="place_example",
        ),
        residential=CoordonneesContact(
            location="location_example",
            postal_code="postal_code_example",
            city="city_example",
            country="country_example",
            street="street_example",
            street_number="street_number_example",
            postal_box="postal_box_example",
            place="place_example",
        ),
        phone_mobile="phone_mobile_example",
    ) # Coordonnees |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_coordonnees(accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, coordonnees=coordonnees)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PersonApi->update_coordonnees: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]
 **coordonnees** | [**Coordonnees**](Coordonnees.md)|  | [optional]

### Return type

[**Coordonnees**](Coordonnees.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_coordonnees_admission**
> Coordonnees update_coordonnees_admission(uuid)



### Example

* Api Key Authentication (Token):
```python
import time
import osis_reference_sdk
from osis_reference_sdk.api import person_api
from osis_reference_sdk.model.coordonnees import Coordonnees
from osis_reference_sdk.model.error import Error
from osis_reference_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/admission
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_reference_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/admission"
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
    api_instance = person_api.PersonApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    coordonnees = Coordonnees(
        contact=CoordonneesContact(
            location="location_example",
            postal_code="postal_code_example",
            city="city_example",
            country="country_example",
            street="street_example",
            street_number="street_number_example",
            postal_box="postal_box_example",
            place="place_example",
        ),
        residential=CoordonneesContact(
            location="location_example",
            postal_code="postal_code_example",
            city="city_example",
            country="country_example",
            street="street_example",
            street_number="street_number_example",
            postal_box="postal_box_example",
            place="place_example",
        ),
        phone_mobile="phone_mobile_example",
    ) # Coordonnees |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_coordonnees_admission(uuid)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PersonApi->update_coordonnees_admission: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_coordonnees_admission(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, coordonnees=coordonnees)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PersonApi->update_coordonnees_admission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]
 **coordonnees** | [**Coordonnees**](Coordonnees.md)|  | [optional]

### Return type

[**Coordonnees**](Coordonnees.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_high_school_diploma**
> HighSchoolDiploma update_high_school_diploma()



### Example

* Api Key Authentication (Token):
```python
import time
import osis_reference_sdk
from osis_reference_sdk.api import person_api
from osis_reference_sdk.model.high_school_diploma import HighSchoolDiploma
from osis_reference_sdk.model.error import Error
from osis_reference_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/admission
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_reference_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/admission"
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
    api_instance = person_api.PersonApi(api_client)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    high_school_diploma = HighSchoolDiploma(
        belgian_diploma=HighSchoolDiplomaBelgianDiploma(
            academic_graduation_year=1,
            result=DiplomaResults("NOT_KNOWN_YET_RESULT"),
            community=BelgianCommunitiesOfEducation("FRENCH_SPEAKING"),
            educational_type=EducationalType(""),
            educational_other="educational_other_example",
            course_repeat=True,
            course_orientation=True,
            institute="institute_example",
            other_institute="other_institute_example",
            schedule=HighSchoolDiplomaBelgianDiplomaSchedule(
                latin=0,
                greek=0,
                chemistry=0,
                physic=0,
                biology=0,
                german=0,
                dutch=0,
                english=0,
                french=0,
                modern_languages_other_label="modern_languages_other_label_example",
                modern_languages_other_hours=0,
                mathematics=0,
                it=0,
                social_sciences=0,
                economic_sciences=0,
                other_label="other_label_example",
                other_hours=0,
            ),
        ),
        foreign_diploma=HighSchoolDiplomaForeignDiploma(
            academic_graduation_year=1,
            result=DiplomaResults("NOT_KNOWN_YET_RESULT"),
            foreign_diploma_type=ForeignDiplomaTypes("NATIONAL_BACHELOR"),
            linguistic_regime="linguistic_regime_example",
            other_linguistic_regime="other_linguistic_regime_example",
            country="country_example",
            equivalence=Equivalence("YES"),
        ),
    ) # HighSchoolDiploma |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_high_school_diploma(accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, high_school_diploma=high_school_diploma)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PersonApi->update_high_school_diploma: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]
 **high_school_diploma** | [**HighSchoolDiploma**](HighSchoolDiploma.md)|  | [optional]

### Return type

[**HighSchoolDiploma**](HighSchoolDiploma.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_high_school_diploma_admission**
> HighSchoolDiploma update_high_school_diploma_admission(uuid)



### Example

* Api Key Authentication (Token):
```python
import time
import osis_reference_sdk
from osis_reference_sdk.api import person_api
from osis_reference_sdk.model.high_school_diploma import HighSchoolDiploma
from osis_reference_sdk.model.error import Error
from osis_reference_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/admission
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_reference_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/admission"
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
    api_instance = person_api.PersonApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    high_school_diploma = HighSchoolDiploma(
        belgian_diploma=HighSchoolDiplomaBelgianDiploma(
            academic_graduation_year=1,
            result=DiplomaResults("NOT_KNOWN_YET_RESULT"),
            community=BelgianCommunitiesOfEducation("FRENCH_SPEAKING"),
            educational_type=EducationalType(""),
            educational_other="educational_other_example",
            course_repeat=True,
            course_orientation=True,
            institute="institute_example",
            other_institute="other_institute_example",
            schedule=HighSchoolDiplomaBelgianDiplomaSchedule(
                latin=0,
                greek=0,
                chemistry=0,
                physic=0,
                biology=0,
                german=0,
                dutch=0,
                english=0,
                french=0,
                modern_languages_other_label="modern_languages_other_label_example",
                modern_languages_other_hours=0,
                mathematics=0,
                it=0,
                social_sciences=0,
                economic_sciences=0,
                other_label="other_label_example",
                other_hours=0,
            ),
        ),
        foreign_diploma=HighSchoolDiplomaForeignDiploma(
            academic_graduation_year=1,
            result=DiplomaResults("NOT_KNOWN_YET_RESULT"),
            foreign_diploma_type=ForeignDiplomaTypes("NATIONAL_BACHELOR"),
            linguistic_regime="linguistic_regime_example",
            other_linguistic_regime="other_linguistic_regime_example",
            country="country_example",
            equivalence=Equivalence("YES"),
        ),
    ) # HighSchoolDiploma |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_high_school_diploma_admission(uuid)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PersonApi->update_high_school_diploma_admission: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_high_school_diploma_admission(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, high_school_diploma=high_school_diploma)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PersonApi->update_high_school_diploma_admission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]
 **high_school_diploma** | [**HighSchoolDiploma**](HighSchoolDiploma.md)|  | [optional]

### Return type

[**HighSchoolDiploma**](HighSchoolDiploma.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_person_identification**
> PersonIdentification update_person_identification()



### Example

* Api Key Authentication (Token):
```python
import time
import osis_reference_sdk
from osis_reference_sdk.api import person_api
from osis_reference_sdk.model.person_identification import PersonIdentification
from osis_reference_sdk.model.error import Error
from osis_reference_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/admission
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_reference_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/admission"
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
    api_instance = person_api.PersonApi(api_client)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    person_identification = PersonIdentification(
        first_name="first_name_example",
        middle_name="middle_name_example",
        last_name="last_name_example",
        first_name_in_use="first_name_in_use_example",
        birth_date=dateutil_parser('1970-01-01').date(),
        birth_year=1000,
        birth_country="birth_country_example",
        birth_place="birth_place_example",
        country_of_citizenship="country_of_citizenship_example",
        language="",
        sex="",
        gender="",
        id_photo=[
            "id_photo_example",
        ],
        id_card=[
            "id_card_example",
        ],
        passport=[
            "passport_example",
        ],
        national_number="national_number_example",
        id_card_number="id_card_number_example",
        passport_number="passport_number_example",
        passport_expiration_date=dateutil_parser('1970-01-01').date(),
        last_registration_year=1,
    ) # PersonIdentification |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_person_identification(accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, person_identification=person_identification)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PersonApi->update_person_identification: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]
 **person_identification** | [**PersonIdentification**](PersonIdentification.md)|  | [optional]

### Return type

[**PersonIdentification**](PersonIdentification.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_person_identification_admission**
> PersonIdentification update_person_identification_admission(uuid)



### Example

* Api Key Authentication (Token):
```python
import time
import osis_reference_sdk
from osis_reference_sdk.api import person_api
from osis_reference_sdk.model.person_identification import PersonIdentification
from osis_reference_sdk.model.error import Error
from osis_reference_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/admission
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_reference_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/admission"
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
    api_instance = person_api.PersonApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    person_identification = PersonIdentification(
        first_name="first_name_example",
        middle_name="middle_name_example",
        last_name="last_name_example",
        first_name_in_use="first_name_in_use_example",
        birth_date=dateutil_parser('1970-01-01').date(),
        birth_year=1000,
        birth_country="birth_country_example",
        birth_place="birth_place_example",
        country_of_citizenship="country_of_citizenship_example",
        language="",
        sex="",
        gender="",
        id_photo=[
            "id_photo_example",
        ],
        id_card=[
            "id_card_example",
        ],
        passport=[
            "passport_example",
        ],
        national_number="national_number_example",
        id_card_number="id_card_number_example",
        passport_number="passport_number_example",
        passport_expiration_date=dateutil_parser('1970-01-01').date(),
        last_registration_year=1,
    ) # PersonIdentification |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_person_identification_admission(uuid)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PersonApi->update_person_identification_admission: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_person_identification_admission(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, person_identification=person_identification)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PersonApi->update_person_identification_admission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]
 **person_identification** | [**PersonIdentification**](PersonIdentification.md)|  | [optional]

### Return type

[**PersonIdentification**](PersonIdentification.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

