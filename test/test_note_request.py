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
from MergeCRMClient.model.note_request import NoteRequest
from MergeCRMClient.api_client import ApiClient


class TestNoteRequest(unittest.TestCase):
    """NoteRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNoteRequest(self):
        """Test NoteRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NoteRequest()  # noqa: E501

        """
        No test json responses were defined for NoteRequest
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (NoteRequest,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
