"""
    Reference Service

    A set of API endpoints that allow you to get reference data.  # noqa: E501

    The version of the OpenAPI document: 1.19
    Generated by: https://openapi-generator.tech
"""


import unittest

import osis_reference_sdk
from osis_reference_sdk.api.countries_api import CountriesApi  # noqa: E501


class TestCountriesApi(unittest.TestCase):
    """CountriesApi unit test stubs"""

    def setUp(self):
        self.api = CountriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_countries_list(self):
        """Test case for countries_list

        """
        pass

    def test_countries_read(self):
        """Test case for countries_read

        """
        pass


if __name__ == '__main__':
    unittest.main()
