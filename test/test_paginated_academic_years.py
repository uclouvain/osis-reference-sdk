"""
    Reference Service

    A set of API endpoints that allow you to get reference data.  # noqa: E501

    The version of the OpenAPI document: 1.25
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_reference_sdk
from osis_reference_sdk.model.academic_year import AcademicYear
from osis_reference_sdk.model.paginated_academic_years_all_of import PaginatedAcademicYearsAllOf
from osis_reference_sdk.model.paging import Paging
globals()['AcademicYear'] = AcademicYear
globals()['PaginatedAcademicYearsAllOf'] = PaginatedAcademicYearsAllOf
globals()['Paging'] = Paging
from osis_reference_sdk.model.paginated_academic_years import PaginatedAcademicYears


class TestPaginatedAcademicYears(unittest.TestCase):
    """PaginatedAcademicYears unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaginatedAcademicYears(self):
        """Test PaginatedAcademicYears"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaginatedAcademicYears()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
