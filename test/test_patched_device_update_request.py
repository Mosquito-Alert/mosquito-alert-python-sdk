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

from mosquito_alert.models.patched_device_update_request import PatchedDeviceUpdateRequest

class TestPatchedDeviceUpdateRequest(unittest.TestCase):
    """PatchedDeviceUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedDeviceUpdateRequest:
        """Test PatchedDeviceUpdateRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedDeviceUpdateRequest`
        """
        model = PatchedDeviceUpdateRequest()
        if include_optional:
            return PatchedDeviceUpdateRequest(
                name = '',
                fcm_token = '0',
                os = mosquito_alert.models.device_os_request.DeviceOsRequest(
                    name = '', 
                    version = '', 
                    locale = '', ),
                mobile_app = mosquito_alert.models.mobile_app_request.MobileAppRequest(
                    package_name = '0', 
                    package_version = '0', )
            )
        else:
            return PatchedDeviceUpdateRequest(
        )
        """

    def testPatchedDeviceUpdateRequest(self):
        """Test PatchedDeviceUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
