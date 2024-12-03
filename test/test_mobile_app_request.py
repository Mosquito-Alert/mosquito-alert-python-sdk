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

from mosquito_alert.models.mobile_app_request import MobileAppRequest

class TestMobileAppRequest(unittest.TestCase):
    """MobileAppRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MobileAppRequest:
        """Test MobileAppRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MobileAppRequest`
        """
        model = MobileAppRequest()
        if include_optional:
            return MobileAppRequest(
                package_name = '0',
                package_version = '0'
            )
        else:
            return MobileAppRequest(
                package_name = '0',
                package_version = '0',
        )
        """

    def testMobileAppRequest(self):
        """Test MobileAppRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()