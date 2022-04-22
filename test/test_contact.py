"""
    Merge CRM API

    The unified API for building rich integrations with multiple CRM platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import MergeCRMClient
from MergeCRMClient.model.address import Address
from MergeCRMClient.model.email_address import EmailAddress
from MergeCRMClient.model.phone_number import PhoneNumber
globals()['Address'] = Address
globals()['EmailAddress'] = EmailAddress
globals()['PhoneNumber'] = PhoneNumber
from MergeCRMClient.model.contact import Contact


class TestContact(unittest.TestCase):
    """Contact unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testContact(self):
        """Test Contact"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Contact()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()