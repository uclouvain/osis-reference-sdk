
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.academic_calendars_api import AcademicCalendarsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from osis_reference_sdk.api.academic_calendars_api import AcademicCalendarsApi
from osis_reference_sdk.api.academic_years_api import AcademicYearsApi
from osis_reference_sdk.api.cities_api import CitiesApi
from osis_reference_sdk.api.countries_api import CountriesApi
from osis_reference_sdk.api.languages_api import LanguagesApi
from osis_reference_sdk.api.study_domains_api import StudyDomainsApi
