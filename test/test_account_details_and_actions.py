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
from MergeCRMClient.model.account_details_and_actions_integration import AccountDetailsAndActionsIntegration
globals()['AccountDetailsAndActionsIntegration'] = AccountDetailsAndActionsIntegration
from MergeCRMClient.model.account_details_and_actions import AccountDetailsAndActions
from MergeCRMClient.api_client import ApiClient


class TestAccountDetailsAndActions(unittest.TestCase):
    """AccountDetailsAndActions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAccountDetailsAndActions(self):
        """Test AccountDetailsAndActions"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AccountDetailsAndActions()  # noqa: E501

        raw_json = """
            {"id": "e59b1821-f85c-4e28-a6b3-1804156f3563", "category": "hris", "status": "COMPLETE", "status_detail": null, "end_user_origin_id": "3ac95cde-6c7f-4eef-afec-be710b42308d", "end_user_organization_name": "Foo Bar, LLC", "end_user_email_address": "hradmin@foobar.dev", "webhook_listener_url": "https://api.merge.dev/api/integrations/webhook-listener/7fc3mee0UW8ecV4", "integration": {"name": "SAP SuccessFactors", "categories": ["hris", "ats"], "image": "https://cdn.merge.dev/SuccessFactors_Logo.png", "square_image": "https://cdn.merge.dev/SuccessFactors_Square_Logo.jpg", "color": "#F6A704", "slug": "sap-successfactors", "passthrough_available": true, "available_model_operations": [{"model_name": "Candidate", "available_operations": ["FETCH", "CREATE"], "required_post_parameters": ["remote_user_id"], "supported_fields": ["first_name", "last_name", "company", "title"]}]}}
        """

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (AccountDetailsAndActions,), False)

        assert deserialized is not None

        assert deserialized.id is not None
        assert deserialized.status is not None
        assert deserialized.end_user_organization_name is not None
        assert deserialized.end_user_email_address is not None
        assert deserialized.webhook_listener_url is not None


if __name__ == '__main__':
    unittest.main()
