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
from MergeCRMClient.model.contact import Contact
from MergeCRMClient.model.debug_mode_log import DebugModeLog
from MergeCRMClient.model.error_validation_problem import ErrorValidationProblem
from MergeCRMClient.model.warning_validation_problem import WarningValidationProblem
globals()['Contact'] = Contact
globals()['DebugModeLog'] = DebugModeLog
globals()['ErrorValidationProblem'] = ErrorValidationProblem
globals()['WarningValidationProblem'] = WarningValidationProblem
from MergeCRMClient.model.crm_contact_response import CRMContactResponse
from MergeCRMClient.api_client import ApiClient


class TestCRMContactResponse(unittest.TestCase):
    """CRMContactResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCRMContactResponse(self):
        """Test CRMContactResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CRMContactResponse()  # noqa: E501

        """
        No test json responses were defined for CRMContactResponse
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (CRMContactResponse,), False)

        assert deserialized is not None

        assert deserialized.model is not None
        assert deserialized.warnings is not None
        assert deserialized.errors is not None


if __name__ == '__main__':
    unittest.main()
