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

from mosquito_alert.models.simple_photo_request import SimplePhotoRequest

class TestSimplePhotoRequest(unittest.TestCase):
    """SimplePhotoRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SimplePhotoRequest:
        """Test SimplePhotoRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SimplePhotoRequest`
        """
        model = SimplePhotoRequest()
        if include_optional:
            return SimplePhotoRequest(
                file = bytes(b'blah')
            )
        else:
            return SimplePhotoRequest(
                file = bytes(b'blah'),
        )
        """

    def testSimplePhotoRequest(self):
        """Test SimplePhotoRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
