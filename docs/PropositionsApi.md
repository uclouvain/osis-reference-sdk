# osis_reference_sdk.PropositionsApi

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/admission*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_member**](PropositionsApi.md#add_member) | **PUT** /propositions/{uuid}/supervision | 
[**approve_proposition**](PropositionsApi.md#approve_proposition) | **POST** /propositions/{uuid}/approve | 
[**create_proposition**](PropositionsApi.md#create_proposition) | **POST** /propositions | 
[**create_signatures**](PropositionsApi.md#create_signatures) | **POST** /propositions/{uuid}/request_signatures | 
[**destroy_proposition**](PropositionsApi.md#destroy_proposition) | **DELETE** /propositions/{uuid} | 
[**list_propositions**](PropositionsApi.md#list_propositions) | **GET** /propositions | 
[**reject_proposition**](PropositionsApi.md#reject_proposition) | **PUT** /propositions/{uuid}/approve | 
[**remove_member**](PropositionsApi.md#remove_member) | **POST** /propositions/{uuid}/supervision | 
[**retrieve_cotutelle**](PropositionsApi.md#retrieve_cotutelle) | **GET** /propositions/{uuid}/cotutelle | 
[**retrieve_proposition**](PropositionsApi.md#retrieve_proposition) | **GET** /propositions/{uuid} | 
[**retrieve_supervision**](PropositionsApi.md#retrieve_supervision) | **GET** /propositions/{uuid}/supervision | 
[**retrieve_verify_proposition**](PropositionsApi.md#retrieve_verify_proposition) | **GET** /propositions/{uuid}/verify | 
[**update_cotutelle**](PropositionsApi.md#update_cotutelle) | **PUT** /propositions/{uuid}/cotutelle | 
[**update_proposition**](PropositionsApi.md#update_proposition) | **PUT** /propositions/{uuid} | 


# **add_member**
> PropositionIdentityDTO add_member(uuid)



Add a supervision group member for a proposition

### Example

* Api Key Authentication (Token):
```python
import time
import osis_reference_sdk
from osis_reference_sdk.api import propositions_api
from osis_reference_sdk.model.supervision_actor import SupervisionActor
from osis_reference_sdk.model.proposition_identity_dto import PropositionIdentityDTO
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
    api_instance = propositions_api.PropositionsApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    supervision_actor = SupervisionActor(
        type=ActorType("PROMOTER"),
        member="member_example",
    ) # SupervisionActor |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_member(uuid)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PropositionsApi->add_member: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.add_member(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, supervision_actor=supervision_actor)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PropositionsApi->add_member: %s\n" % e)
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
 **supervision_actor** | [**SupervisionActor**](SupervisionActor.md)|  | [optional]

### Return type

[**PropositionIdentityDTO**](PropositionIdentityDTO.md)

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

# **approve_proposition**
> PropositionIdentityDTO approve_proposition(uuid)



Approve the proposition.

### Example

* Api Key Authentication (Token):
```python
import time
import osis_reference_sdk
from osis_reference_sdk.api import propositions_api
from osis_reference_sdk.model.proposition_identity_dto import PropositionIdentityDTO
from osis_reference_sdk.model.error import Error
from osis_reference_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_reference_sdk.model.approuver_proposition_command import ApprouverPropositionCommand
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
    api_instance = propositions_api.PropositionsApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    approuver_proposition_command = ApprouverPropositionCommand(
        matricule="matricule_example",
        commentaire_interne="commentaire_interne_example",
        commentaire_externe="commentaire_externe_example",
    ) # ApprouverPropositionCommand |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.approve_proposition(uuid)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PropositionsApi->approve_proposition: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.approve_proposition(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, approuver_proposition_command=approuver_proposition_command)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PropositionsApi->approve_proposition: %s\n" % e)
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
 **approuver_proposition_command** | [**ApprouverPropositionCommand**](ApprouverPropositionCommand.md)|  | [optional]

### Return type

[**PropositionIdentityDTO**](PropositionIdentityDTO.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_proposition**
> PropositionIdentityDTO create_proposition()



### Example

* Api Key Authentication (Token):
```python
import time
import osis_reference_sdk
from osis_reference_sdk.api import propositions_api
from osis_reference_sdk.model.proposition_identity_dto import PropositionIdentityDTO
from osis_reference_sdk.model.error import Error
from osis_reference_sdk.model.initier_proposition_command import InitierPropositionCommand
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
    api_instance = propositions_api.PropositionsApi(api_client)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    initier_proposition_command = InitierPropositionCommand(
        type_admission=AdmissionType("ADMISSION"),
        sigle_formation="sigle_formation_example",
        annee_formation=1,
        matricule_candidat="matricule_candidat_example",
        justification="justification_example",
        commission_proximite=ChoixCommissionProximite(""),
        type_financement="type_financement_example",
        type_contrat_travail="type_contrat_travail_example",
        eft=1,
        bourse_recherche="bourse_recherche_example",
        duree_prevue=1,
        temps_consacre=1,
        titre_projet="titre_projet_example",
        resume_projet="resume_projet_example",
        institut_these="institut_these_example",
        lieu_these="lieu_these_example",
        autre_lieu_these="autre_lieu_these_example",
        documents_projet=[
            "documents_projet_example",
        ],
        graphe_gantt=[
            "graphe_gantt_example",
        ],
        proposition_programme_doctoral=[
            "proposition_programme_doctoral_example",
        ],
        projet_formation_complementaire=[
            "projet_formation_complementaire_example",
        ],
        lettres_recommandation=[
            "lettres_recommandation_example",
        ],
        langue_redaction_these=ChoixLangueRedactionThese("FRENCH"),
        doctorat_deja_realise=ChoixDoctoratDejaRealise("YES"),
        institution="institution_example",
        date_soutenance=dateutil_parser('1970-01-01').date(),
        raison_non_soutenue="raison_non_soutenue_example",
    ) # InitierPropositionCommand |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_proposition(accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, initier_proposition_command=initier_proposition_command)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PropositionsApi->create_proposition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]
 **initier_proposition_command** | [**InitierPropositionCommand**](InitierPropositionCommand.md)|  | [optional]

### Return type

[**PropositionIdentityDTO**](PropositionIdentityDTO.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_signatures**
> PropositionIdentityDTO create_signatures(uuid)



Ask for all promoters and members to sign the proposition.

### Example

* Api Key Authentication (Token):
```python
import time
import osis_reference_sdk
from osis_reference_sdk.api import propositions_api
from osis_reference_sdk.model.proposition_identity_dto import PropositionIdentityDTO
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
    api_instance = propositions_api.PropositionsApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    proposition_identity_dto = PropositionIdentityDTO(
    ) # PropositionIdentityDTO |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_signatures(uuid)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PropositionsApi->create_signatures: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_signatures(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, proposition_identity_dto=proposition_identity_dto)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PropositionsApi->create_signatures: %s\n" % e)
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
 **proposition_identity_dto** | [**PropositionIdentityDTO**](PropositionIdentityDTO.md)|  | [optional]

### Return type

[**PropositionIdentityDTO**](PropositionIdentityDTO.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_proposition**
> PropositionIdentityDTO destroy_proposition(uuid)



Soft-Delete a proposition

### Example

* Api Key Authentication (Token):
```python
import time
import osis_reference_sdk
from osis_reference_sdk.api import propositions_api
from osis_reference_sdk.model.proposition_identity_dto import PropositionIdentityDTO
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
    api_instance = propositions_api.PropositionsApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.destroy_proposition(uuid)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PropositionsApi->destroy_proposition: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.destroy_proposition(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PropositionsApi->destroy_proposition: %s\n" % e)
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

[**PropositionIdentityDTO**](PropositionIdentityDTO.md)

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

# **list_propositions**
> PropositionSearch list_propositions()



### Example

* Api Key Authentication (Token):
```python
import time
import osis_reference_sdk
from osis_reference_sdk.api import propositions_api
from osis_reference_sdk.model.proposition_search import PropositionSearch
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
    api_instance = propositions_api.PropositionsApi(api_client)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_propositions(accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PropositionsApi->list_propositions: %s\n" % e)
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

[**PropositionSearch**](PropositionSearch.md)

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

# **reject_proposition**
> PropositionIdentityDTO reject_proposition(uuid)



Reject the proposition.

### Example

* Api Key Authentication (Token):
```python
import time
import osis_reference_sdk
from osis_reference_sdk.api import propositions_api
from osis_reference_sdk.model.refuser_proposition_command import RefuserPropositionCommand
from osis_reference_sdk.model.proposition_identity_dto import PropositionIdentityDTO
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
    api_instance = propositions_api.PropositionsApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    refuser_proposition_command = RefuserPropositionCommand(
        matricule="matricule_example",
        commentaire_interne="commentaire_interne_example",
        commentaire_externe="commentaire_externe_example",
        motif_refus="motif_refus_example",
    ) # RefuserPropositionCommand |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.reject_proposition(uuid)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PropositionsApi->reject_proposition: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.reject_proposition(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, refuser_proposition_command=refuser_proposition_command)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PropositionsApi->reject_proposition: %s\n" % e)
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
 **refuser_proposition_command** | [**RefuserPropositionCommand**](RefuserPropositionCommand.md)|  | [optional]

### Return type

[**PropositionIdentityDTO**](PropositionIdentityDTO.md)

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

# **remove_member**
> PropositionIdentityDTO remove_member(uuid)



Remove a supervision group member for a proposition

### Example

* Api Key Authentication (Token):
```python
import time
import osis_reference_sdk
from osis_reference_sdk.api import propositions_api
from osis_reference_sdk.model.supervision_actor import SupervisionActor
from osis_reference_sdk.model.proposition_identity_dto import PropositionIdentityDTO
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
    api_instance = propositions_api.PropositionsApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    supervision_actor = SupervisionActor(
        type=ActorType("PROMOTER"),
        member="member_example",
    ) # SupervisionActor |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.remove_member(uuid)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PropositionsApi->remove_member: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.remove_member(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, supervision_actor=supervision_actor)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PropositionsApi->remove_member: %s\n" % e)
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
 **supervision_actor** | [**SupervisionActor**](SupervisionActor.md)|  | [optional]

### Return type

[**PropositionIdentityDTO**](PropositionIdentityDTO.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_cotutelle**
> CotutelleDTO retrieve_cotutelle(uuid)



Get the cotutelle of a proposition

### Example

* Api Key Authentication (Token):
```python
import time
import osis_reference_sdk
from osis_reference_sdk.api import propositions_api
from osis_reference_sdk.model.cotutelle_dto import CotutelleDTO
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
    api_instance = propositions_api.PropositionsApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_cotutelle(uuid)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PropositionsApi->retrieve_cotutelle: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.retrieve_cotutelle(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PropositionsApi->retrieve_cotutelle: %s\n" % e)
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

[**CotutelleDTO**](CotutelleDTO.md)

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

# **retrieve_proposition**
> PropositionDTO retrieve_proposition(uuid)



Get a single proposition

### Example

* Api Key Authentication (Token):
```python
import time
import osis_reference_sdk
from osis_reference_sdk.api import propositions_api
from osis_reference_sdk.model.proposition_dto import PropositionDTO
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
    api_instance = propositions_api.PropositionsApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_proposition(uuid)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PropositionsApi->retrieve_proposition: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.retrieve_proposition(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PropositionsApi->retrieve_proposition: %s\n" % e)
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

[**PropositionDTO**](PropositionDTO.md)

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

# **retrieve_supervision**
> SupervisionDTO retrieve_supervision(uuid)



Get the supervision group of a proposition

### Example

* Api Key Authentication (Token):
```python
import time
import osis_reference_sdk
from osis_reference_sdk.api import propositions_api
from osis_reference_sdk.model.error import Error
from osis_reference_sdk.model.supervision_dto import SupervisionDTO
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
    api_instance = propositions_api.PropositionsApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_supervision(uuid)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PropositionsApi->retrieve_supervision: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.retrieve_supervision(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PropositionsApi->retrieve_supervision: %s\n" % e)
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

[**SupervisionDTO**](SupervisionDTO.md)

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

# **retrieve_verify_proposition**
> [InlineResponse200] retrieve_verify_proposition(uuid)



Check the proposition to be OK with all validators.

### Example

* Api Key Authentication (Token):
```python
import time
import osis_reference_sdk
from osis_reference_sdk.api import propositions_api
from osis_reference_sdk.model.inline_response200 import InlineResponse200
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
    api_instance = propositions_api.PropositionsApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_verify_proposition(uuid)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PropositionsApi->retrieve_verify_proposition: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.retrieve_verify_proposition(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PropositionsApi->retrieve_verify_proposition: %s\n" % e)
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

[**[InlineResponse200]**](InlineResponse200.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Proposition verification errors |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cotutelle**
> PropositionIdentityDTO update_cotutelle(uuid)



Set the cotutelle of a proposition

### Example

* Api Key Authentication (Token):
```python
import time
import osis_reference_sdk
from osis_reference_sdk.api import propositions_api
from osis_reference_sdk.model.definir_cotutelle_command import DefinirCotutelleCommand
from osis_reference_sdk.model.proposition_identity_dto import PropositionIdentityDTO
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
    api_instance = propositions_api.PropositionsApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    definir_cotutelle_command = DefinirCotutelleCommand(
        motivation="motivation_example",
        institution="institution_example",
        demande_ouverture=[
            "demande_ouverture_example",
        ],
        convention=[
            "convention_example",
        ],
        autres_documents=[
            "autres_documents_example",
        ],
    ) # DefinirCotutelleCommand |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_cotutelle(uuid)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PropositionsApi->update_cotutelle: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_cotutelle(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, definir_cotutelle_command=definir_cotutelle_command)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PropositionsApi->update_cotutelle: %s\n" % e)
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
 **definir_cotutelle_command** | [**DefinirCotutelleCommand**](DefinirCotutelleCommand.md)|  | [optional]

### Return type

[**PropositionIdentityDTO**](PropositionIdentityDTO.md)

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

# **update_proposition**
> PropositionIdentityDTO update_proposition(uuid)



Edit a proposition

### Example

* Api Key Authentication (Token):
```python
import time
import osis_reference_sdk
from osis_reference_sdk.api import propositions_api
from osis_reference_sdk.model.completer_proposition_command import CompleterPropositionCommand
from osis_reference_sdk.model.proposition_identity_dto import PropositionIdentityDTO
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
    api_instance = propositions_api.PropositionsApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    completer_proposition_command = CompleterPropositionCommand(
        uuid="uuid_example",
        type_admission=AdmissionType("ADMISSION"),
        justification="justification_example",
        commission_proximite=ChoixCommissionProximite(""),
        type_financement="type_financement_example",
        type_contrat_travail="type_contrat_travail_example",
        eft=1,
        bourse_recherche="bourse_recherche_example",
        duree_prevue=1,
        temps_consacre=1,
        titre_projet="titre_projet_example",
        resume_projet="resume_projet_example",
        documents_projet=[
            "documents_projet_example",
        ],
        graphe_gantt=[
            "graphe_gantt_example",
        ],
        proposition_programme_doctoral=[
            "proposition_programme_doctoral_example",
        ],
        projet_formation_complementaire=[
            "projet_formation_complementaire_example",
        ],
        lettres_recommandation=[
            "lettres_recommandation_example",
        ],
        langue_redaction_these=ChoixLangueRedactionThese("FRENCH"),
        institut_these="institut_these_example",
        lieu_these="lieu_these_example",
        autre_lieu_these="autre_lieu_these_example",
        doctorat_deja_realise=ChoixDoctoratDejaRealise("YES"),
        institution="institution_example",
        date_soutenance=dateutil_parser('1970-01-01').date(),
        raison_non_soutenue="raison_non_soutenue_example",
    ) # CompleterPropositionCommand |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_proposition(uuid)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PropositionsApi->update_proposition: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_proposition(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, completer_proposition_command=completer_proposition_command)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling PropositionsApi->update_proposition: %s\n" % e)
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
 **completer_proposition_command** | [**CompleterPropositionCommand**](CompleterPropositionCommand.md)|  | [optional]

### Return type

[**PropositionIdentityDTO**](PropositionIdentityDTO.md)

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

