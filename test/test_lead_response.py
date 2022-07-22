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
from MergeCRMClient.model.debug_mode_log import DebugModeLog
from MergeCRMClient.model.error_validation_problem import ErrorValidationProblem
from MergeCRMClient.model.lead import Lead
from MergeCRMClient.model.warning_validation_problem import WarningValidationProblem
globals()['DebugModeLog'] = DebugModeLog
globals()['ErrorValidationProblem'] = ErrorValidationProblem
globals()['Lead'] = Lead
globals()['WarningValidationProblem'] = WarningValidationProblem
from MergeCRMClient.model.lead_response import LeadResponse
from MergeCRMClient.api_client import ApiClient


class TestLeadResponse(unittest.TestCase):
    """LeadResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLeadResponse(self):
        """Test LeadResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LeadResponse()  # noqa: E501

        """
        No test json responses were defined for LeadResponse
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (LeadResponse,), False)

        assert deserialized is not None

        assert deserialized.model is not None
        assert deserialized.warnings is not None
        assert deserialized.errors is not None


if __name__ == '__main__':
    unittest.main()
