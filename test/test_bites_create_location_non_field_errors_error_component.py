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

from mosquito_alert.models.bites_create_location_non_field_errors_error_component import BitesCreateLocationNonFieldErrorsErrorComponent

class TestBitesCreateLocationNonFieldErrorsErrorComponent(unittest.TestCase):
    """BitesCreateLocationNonFieldErrorsErrorComponent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BitesCreateLocationNonFieldErrorsErrorComponent:
        """Test BitesCreateLocationNonFieldErrorsErrorComponent
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BitesCreateLocationNonFieldErrorsErrorComponent`
        """
        model = BitesCreateLocationNonFieldErrorsErrorComponent()
        if include_optional:
            return BitesCreateLocationNonFieldErrorsErrorComponent(
                attr = 'location.non_field_errors',
                code = 'invalid',
                detail = ''
            )
        else:
            return BitesCreateLocationNonFieldErrorsErrorComponent(
                attr = 'location.non_field_errors',
                code = 'invalid',
                detail = '',
        )
        """

    def testBitesCreateLocationNonFieldErrorsErrorComponent(self):
        """Test BitesCreateLocationNonFieldErrorsErrorComponent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
