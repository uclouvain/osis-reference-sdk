"""
    Reference Service

    A set of API endpoints that allow you to get reference data.  # noqa: E501

    The version of the OpenAPI document: 1.27
    Generated by: https://openapi-generator.tech
"""


import unittest

import osis_reference_sdk
from osis_reference_sdk.api.high_schools_api import HighSchoolsApi  # noqa: E501


class TestHighSchoolsApi(unittest.TestCase):
    """HighSchoolsApi unit test stubs"""

    def setUp(self):
        self.api = HighSchoolsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_high_school_read(self):
        """Test case for high_school_read

        """
        pass

    def test_high_schools_list(self):
        """Test case for high_schools_list

        """
        pass


if __name__ == '__main__':
    unittest.main()
