# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from osis_reference_sdk.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from osis_reference_sdk.model.academic_calendar import AcademicCalendar
from osis_reference_sdk.model.academic_year import AcademicYear
from osis_reference_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_reference_sdk.model.city import City
from osis_reference_sdk.model.country import Country
from osis_reference_sdk.model.error import Error
from osis_reference_sdk.model.language import Language
from osis_reference_sdk.model.paginated_academic_calendars import PaginatedAcademicCalendars
from osis_reference_sdk.model.paginated_academic_calendars_all_of import PaginatedAcademicCalendarsAllOf
from osis_reference_sdk.model.paginated_academic_years import PaginatedAcademicYears
from osis_reference_sdk.model.paginated_academic_years_all_of import PaginatedAcademicYearsAllOf
from osis_reference_sdk.model.paginated_city import PaginatedCity
from osis_reference_sdk.model.paginated_city_all_of import PaginatedCityAllOf
from osis_reference_sdk.model.paginated_country import PaginatedCountry
from osis_reference_sdk.model.paginated_country_all_of import PaginatedCountryAllOf
from osis_reference_sdk.model.paginated_language import PaginatedLanguage
from osis_reference_sdk.model.paginated_language_all_of import PaginatedLanguageAllOf
from osis_reference_sdk.model.paginated_study_domain import PaginatedStudyDomain
from osis_reference_sdk.model.paginated_study_domain_all_of import PaginatedStudyDomainAllOf
from osis_reference_sdk.model.paging import Paging
from osis_reference_sdk.model.study_domain import StudyDomain
