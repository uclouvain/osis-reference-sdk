"""
    Reference Service

    A set of API endpoints that allow you to get reference data.  # noqa: E501

    The version of the OpenAPI document: 1.19
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_reference_sdk
from osis_reference_sdk.model.academic_calendar import AcademicCalendar
from osis_reference_sdk.model.paginated_academic_calendars_all_of import PaginatedAcademicCalendarsAllOf
from osis_reference_sdk.model.paging import Paging
globals()['AcademicCalendar'] = AcademicCalendar
globals()['PaginatedAcademicCalendarsAllOf'] = PaginatedAcademicCalendarsAllOf
globals()['Paging'] = Paging
from osis_reference_sdk.model.paginated_academic_calendars import PaginatedAcademicCalendars


class TestPaginatedAcademicCalendars(unittest.TestCase):
    """PaginatedAcademicCalendars unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaginatedAcademicCalendars(self):
        """Test PaginatedAcademicCalendars"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaginatedAcademicCalendars()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
