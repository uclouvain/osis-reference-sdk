"""
    Reference Service

    A set of API endpoints that allow you to get reference data.  # noqa: E501

    The version of the OpenAPI document: 1.24
    Generated by: https://openapi-generator.tech
"""


import unittest

import osis_reference_sdk
from osis_reference_sdk.api.academic_years_api import AcademicYearsApi  # noqa: E501


class TestAcademicYearsApi(unittest.TestCase):
    """AcademicYearsApi unit test stubs"""

    def setUp(self):
        self.api = AcademicYearsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_academic_years(self):
        """Test case for get_academic_years

        """
        pass


if __name__ == '__main__':
    unittest.main()
