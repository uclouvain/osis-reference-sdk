"""
    Reference Service

    A set of API endpoints that allow you to get reference data.  # noqa: E501

    The version of the OpenAPI document: 1.27
    Generated by: https://openapi-generator.tech
"""


import unittest

import osis_reference_sdk
from osis_reference_sdk.api.cities_api import CitiesApi  # noqa: E501


class TestCitiesApi(unittest.TestCase):
    """CitiesApi unit test stubs"""

    def setUp(self):
        self.api = CitiesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cities_list(self):
        """Test case for cities_list

        """
        pass


if __name__ == '__main__':
    unittest.main()
