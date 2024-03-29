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
from MergeCRMClient.model.account_details_and_actions import AccountDetailsAndActions
globals()['AccountDetailsAndActions'] = AccountDetailsAndActions
from MergeCRMClient.model.paginated_account_details_and_actions_list import PaginatedAccountDetailsAndActionsList
from MergeCRMClient.api_client import ApiClient


class TestPaginatedAccountDetailsAndActionsList(unittest.TestCase):
    """PaginatedAccountDetailsAndActionsList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaginatedAccountDetailsAndActionsList(self):
        """Test PaginatedAccountDetailsAndActionsList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaginatedAccountDetailsAndActionsList()  # noqa: E501

        """
        No test json responses were defined for PaginatedAccountDetailsAndActionsList
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (PaginatedAccountDetailsAndActionsList,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
