"""
    Reference Service

    A set of API endpoints that allow you to get reference data.  # noqa: E501

    The version of the OpenAPI document: 1.23
    Generated by: https://openapi-generator.tech
"""


import unittest

import osis_reference_sdk
from osis_reference_sdk.api.study_domains_api import StudyDomainsApi  # noqa: E501


class TestStudyDomainsApi(unittest.TestCase):
    """StudyDomainsApi unit test stubs"""

    def setUp(self):
        self.api = StudyDomainsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_study_domains_list(self):
        """Test case for study_domains_list

        """
        pass


if __name__ == '__main__':
    unittest.main()
