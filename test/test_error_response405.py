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

from mosquito_alert.models.error_response405 import ErrorResponse405

class TestErrorResponse405(unittest.TestCase):
    """ErrorResponse405 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ErrorResponse405:
        """Test ErrorResponse405
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ErrorResponse405`
        """
        model = ErrorResponse405()
        if include_optional:
            return ErrorResponse405(
                type = 'client_error',
                errors = [
                    mosquito_alert.models.error405.Error405(
                        code = 'method_not_allowed', 
                        detail = '', 
                        attr = '', )
                    ]
            )
        else:
            return ErrorResponse405(
                type = 'client_error',
                errors = [
                    mosquito_alert.models.error405.Error405(
                        code = 'method_not_allowed', 
                        detail = '', 
                        attr = '', )
                    ],
        )
        """

    def testErrorResponse405(self):
        """Test ErrorResponse405"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
