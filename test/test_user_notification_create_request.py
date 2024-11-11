# coding: utf-8

"""
    Mosquito Alert API

    Introducing API v1 for Mosquito Alert platform, a project desgined to facilitate citizen science initiatives and enable collaboration among scientists, public health officials, and environmental managers in the investigation and control of disease-carrying mosquitoes.

    The version of the OpenAPI document: v1
    Contact: it@mosquitoalert.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from mosquito_alert_api.models.user_notification_create_request import UserNotificationCreateRequest

class TestUserNotificationCreateRequest(unittest.TestCase):
    """UserNotificationCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserNotificationCreateRequest:
        """Test UserNotificationCreateRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserNotificationCreateRequest`
        """
        model = UserNotificationCreateRequest()
        if include_optional:
            return UserNotificationCreateRequest(
                receiver_type = 'user',
                title_en = '0',
                body_en = '0',
                user_uuid = ''
            )
        else:
            return UserNotificationCreateRequest(
                receiver_type = 'user',
                title_en = '0',
                body_en = '0',
                user_uuid = '',
        )
        """

    def testUserNotificationCreateRequest(self):
        """Test UserNotificationCreateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
