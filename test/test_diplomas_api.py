"""
    Reference Service

    A set of API endpoints that allow you to get reference data.  # noqa: E501

    The version of the OpenAPI document: 1.23
    Generated by: https://openapi-generator.tech
"""


import unittest

import osis_reference_sdk
from osis_reference_sdk.api.diplomas_api import DiplomasApi  # noqa: E501


class TestDiplomasApi(unittest.TestCase):
    """DiplomasApi unit test stubs"""

    def setUp(self):
        self.api = DiplomasApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_diploma_read(self):
        """Test case for diploma_read

        """
        pass

    def test_diplomas_list(self):
        """Test case for diplomas_list

        """
        pass


if __name__ == '__main__':
    unittest.main()
