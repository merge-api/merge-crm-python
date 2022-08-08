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
from MergeCRMClient.model.validation_problem_source import ValidationProblemSource
from MergeCRMClient.api_client import ApiClient


class TestValidationProblemSource(unittest.TestCase):
    """ValidationProblemSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testValidationProblemSource(self):
        """Test ValidationProblemSource"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ValidationProblemSource()  # noqa: E501

        """
        No test json responses were defined for ValidationProblemSource
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (ValidationProblemSource,), False)

        assert deserialized is not None

        assert deserialized.pointer is not None


if __name__ == '__main__':
    unittest.main()
