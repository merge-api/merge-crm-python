"""
    Merge CRM API

    The unified API for building rich integrations with multiple CRM platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest
from unittest.mock import MagicMock

import MergeCRMClient
from MergeCRMClient.model.user import User
globals()['User'] = User
from MergeCRMClient.model.paginated_user_list import PaginatedUserList
from MergeCRMClient.api_client import ApiClient


class TestPaginatedUserList(unittest.TestCase):
    """PaginatedUserList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaginatedUserList(self):
        """Test PaginatedUserList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaginatedUserList()  # noqa: E501

        """
        No test json responses were defined for PaginatedUserList
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (PaginatedUserList,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
