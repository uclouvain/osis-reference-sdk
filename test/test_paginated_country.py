"""
    Reference Service

    A set of API endpoints that allow you to get reference data.  # noqa: E501

    The version of the OpenAPI document: 1.25
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_reference_sdk
from osis_reference_sdk.model.country import Country
from osis_reference_sdk.model.paginated_country_all_of import PaginatedCountryAllOf
from osis_reference_sdk.model.paging import Paging
globals()['Country'] = Country
globals()['PaginatedCountryAllOf'] = PaginatedCountryAllOf
globals()['Paging'] = Paging
from osis_reference_sdk.model.paginated_country import PaginatedCountry


class TestPaginatedCountry(unittest.TestCase):
    """PaginatedCountry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaginatedCountry(self):
        """Test PaginatedCountry"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaginatedCountry()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
