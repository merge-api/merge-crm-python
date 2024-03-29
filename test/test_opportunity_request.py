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
from MergeCRMClient.model.opportunity_request import OpportunityRequest
from MergeCRMClient.api_client import ApiClient


class TestOpportunityRequest(unittest.TestCase):
    """OpportunityRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOpportunityRequest(self):
        """Test OpportunityRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = OpportunityRequest()  # noqa: E501

        """
        No test json responses were defined for OpportunityRequest
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (OpportunityRequest,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
