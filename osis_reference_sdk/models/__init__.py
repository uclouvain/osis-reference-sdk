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
from osis_reference_sdk.model.allocation_get import AllocationGet
from osis_reference_sdk.model.allocation_paging import AllocationPaging
from osis_reference_sdk.model.cohort_get import CohortGet
from osis_reference_sdk.model.cohort_paging import CohortPaging
from osis_reference_sdk.model.country import Country
from osis_reference_sdk.model.inline_response200 import InlineResponse200
from osis_reference_sdk.model.internship_get import InternshipGet
from osis_reference_sdk.model.internship_paging import InternshipPaging
from osis_reference_sdk.model.master_get import MasterGet
from osis_reference_sdk.model.master_paging import MasterPaging
from osis_reference_sdk.model.organization_get import OrganizationGet
from osis_reference_sdk.model.organization_paging import OrganizationPaging
from osis_reference_sdk.model.period_get import PeriodGet
from osis_reference_sdk.model.period_paging import PeriodPaging
from osis_reference_sdk.model.person import Person
from osis_reference_sdk.model.person_affectation_get import PersonAffectationGet
from osis_reference_sdk.model.person_affectation_paging import PersonAffectationPaging
from osis_reference_sdk.model.place_evaluation_get import PlaceEvaluationGet
from osis_reference_sdk.model.place_evaluation_item_get import PlaceEvaluationItemGet
from osis_reference_sdk.model.place_evaluation_item_paging import PlaceEvaluationItemPaging
from osis_reference_sdk.model.score_get import ScoreGet
from osis_reference_sdk.model.score_list_get import ScoreListGet
from osis_reference_sdk.model.score_paging import ScorePaging
from osis_reference_sdk.model.specialty_get import SpecialtyGet
from osis_reference_sdk.model.specialty_paging import SpecialtyPaging
from osis_reference_sdk.model.student import Student
from osis_reference_sdk.model.student_affectation_get import StudentAffectationGet
from osis_reference_sdk.model.student_affectation_paging import StudentAffectationPaging
from osis_reference_sdk.model.student_get import StudentGet
from osis_reference_sdk.model.student_paging import StudentPaging
