# osis-reference-sdk
A set of API endpoints that allow you to get reference data.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.22
- Package version: 1.22
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import osis_reference_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import osis_reference_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import osis_reference_sdk
from pprint import pprint
from osis_reference_sdk.api import academic_calendars_api
from osis_reference_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_reference_sdk.model.error import Error
from osis_reference_sdk.model.paginated_academic_calendars import PaginatedAcademicCalendars
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
    api_instance = academic_calendars_api.AcademicCalendarsApi(api_client)
    data_year = 1 # int |  (optional)
reference = "reference_example" # str |  (optional)
accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
x_user_first_name = "X-User-FirstName_example" # str |  (optional)
x_user_last_name = "X-User-LastName_example" # str |  (optional)
x_user_email = "X-User-Email_example" # str |  (optional)
x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
limit = 25 # int | Limit of paginated results (optional)
offset = 25 # int | Offset of paginated results (optional)

    try:
        api_response = api_instance.academic_calendars_list(data_year=data_year, reference=reference, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, limit=limit, offset=offset)
        pprint(api_response)
    except osis_reference_sdk.ApiException as e:
        print("Exception when calling AcademicCalendarsApi->academic_calendars_list: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/reference*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AcademicCalendarsApi* | [**academic_calendars_list**](docs/AcademicCalendarsApi.md#academic_calendars_list) | **GET** /academic_calendars/ | 
*AcademicYearsApi* | [**get_academic_years**](docs/AcademicYearsApi.md#get_academic_years) | **GET** /academic_years | 
*CitiesApi* | [**cities_list**](docs/CitiesApi.md#cities_list) | **GET** /cities/ | 
*CountriesApi* | [**countries_list**](docs/CountriesApi.md#countries_list) | **GET** /countries/ | 
*CountriesApi* | [**countries_read**](docs/CountriesApi.md#countries_read) | **GET** /countries/{uuid} | 
*DiplomasApi* | [**diploma_read**](docs/DiplomasApi.md#diploma_read) | **GET** /diplomas/{uuid} | 
*DiplomasApi* | [**diplomas_list**](docs/DiplomasApi.md#diplomas_list) | **GET** /diplomas/ | 
*HighSchoolsApi* | [**high_school_read**](docs/HighSchoolsApi.md#high_school_read) | **GET** /high_schools/{uuid} | 
*HighSchoolsApi* | [**high_schools_list**](docs/HighSchoolsApi.md#high_schools_list) | **GET** /high_schools/ | 
*LanguagesApi* | [**languages_list**](docs/LanguagesApi.md#languages_list) | **GET** /languages | 
*StudyDomainsApi* | [**study_domains_list**](docs/StudyDomainsApi.md#study_domains_list) | **GET** /study-domains | 


## Documentation For Models

 - [AcademicCalendar](docs/AcademicCalendar.md)
 - [AcademicYear](docs/AcademicYear.md)
 - [AcceptedLanguageEnum](docs/AcceptedLanguageEnum.md)
 - [City](docs/City.md)
 - [Country](docs/Country.md)
 - [CycleEnum](docs/CycleEnum.md)
 - [Diploma](docs/Diploma.md)
 - [DiplomaDetail](docs/DiplomaDetail.md)
 - [DiplomaDetailAllOf](docs/DiplomaDetailAllOf.md)
 - [DurationTypeEnum](docs/DurationTypeEnum.md)
 - [Error](docs/Error.md)
 - [HighSchool](docs/HighSchool.md)
 - [HighSchoolDetail](docs/HighSchoolDetail.md)
 - [HighSchoolDetailAllOf](docs/HighSchoolDetailAllOf.md)
 - [Language](docs/Language.md)
 - [PaginatedAcademicCalendars](docs/PaginatedAcademicCalendars.md)
 - [PaginatedAcademicCalendarsAllOf](docs/PaginatedAcademicCalendarsAllOf.md)
 - [PaginatedAcademicYears](docs/PaginatedAcademicYears.md)
 - [PaginatedAcademicYearsAllOf](docs/PaginatedAcademicYearsAllOf.md)
 - [PaginatedCity](docs/PaginatedCity.md)
 - [PaginatedCityAllOf](docs/PaginatedCityAllOf.md)
 - [PaginatedCountry](docs/PaginatedCountry.md)
 - [PaginatedCountryAllOf](docs/PaginatedCountryAllOf.md)
 - [PaginatedDiploma](docs/PaginatedDiploma.md)
 - [PaginatedDiplomaAllOf](docs/PaginatedDiplomaAllOf.md)
 - [PaginatedHighSchool](docs/PaginatedHighSchool.md)
 - [PaginatedHighSchoolAllOf](docs/PaginatedHighSchoolAllOf.md)
 - [PaginatedLanguage](docs/PaginatedLanguage.md)
 - [PaginatedLanguageAllOf](docs/PaginatedLanguageAllOf.md)
 - [PaginatedStudyDomain](docs/PaginatedStudyDomain.md)
 - [PaginatedStudyDomainAllOf](docs/PaginatedStudyDomainAllOf.md)
 - [Paging](docs/Paging.md)
 - [StudyDomain](docs/StudyDomain.md)
 - [StudyTypeEnum](docs/StudyTypeEnum.md)


## Documentation For Authorization


## Token

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in osis_reference_sdk.apis and osis_reference_sdk.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from osis_reference_sdk.api.default_api import DefaultApi`
- `from osis_reference_sdk.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import osis_reference_sdk
from osis_reference_sdk.apis import *
from osis_reference_sdk.models import *
```

