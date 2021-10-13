# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from osis_reference_sdk.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from osis_reference_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_reference_sdk.model.array_of_city import ArrayOfCity
from osis_reference_sdk.model.array_of_country import ArrayOfCountry
from osis_reference_sdk.model.array_of_languages import ArrayOfLanguages
from osis_reference_sdk.model.array_of_study_domain import ArrayOfStudyDomain
from osis_reference_sdk.model.city import City
from osis_reference_sdk.model.country import Country
from osis_reference_sdk.model.error import Error
from osis_reference_sdk.model.language import Language
from osis_reference_sdk.model.study_domain import StudyDomain
