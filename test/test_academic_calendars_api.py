"""
    Reference Service

    A set of API endpoints that allow you to get reference data.  # noqa: E501

    The version of the OpenAPI document: 1.23
    Generated by: https://openapi-generator.tech
"""


import unittest

import osis_reference_sdk
from osis_reference_sdk.api.academic_calendars_api import AcademicCalendarsApi  # noqa: E501


class TestAcademicCalendarsApi(unittest.TestCase):
    """AcademicCalendarsApi unit test stubs"""

    def setUp(self):
        self.api = AcademicCalendarsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_academic_calendars_list(self):
        """Test case for academic_calendars_list

        """
        pass


if __name__ == '__main__':
    unittest.main()
