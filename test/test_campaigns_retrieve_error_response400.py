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

from mosquito_alert.models.campaigns_retrieve_error_response400 import CampaignsRetrieveErrorResponse400

class TestCampaignsRetrieveErrorResponse400(unittest.TestCase):
    """CampaignsRetrieveErrorResponse400 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CampaignsRetrieveErrorResponse400:
        """Test CampaignsRetrieveErrorResponse400
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CampaignsRetrieveErrorResponse400`
        """
        model = CampaignsRetrieveErrorResponse400()
        if include_optional:
            return CampaignsRetrieveErrorResponse400(
                type = 'client_error',
                errors = [
                    mosquito_alert.models.parse_error.ParseError(
                        code = 'parse_error', 
                        detail = '', 
                        attr = '', )
                    ]
            )
        else:
            return CampaignsRetrieveErrorResponse400(
                type = 'client_error',
                errors = [
                    mosquito_alert.models.parse_error.ParseError(
                        code = 'parse_error', 
                        detail = '', 
                        attr = '', )
                    ],
        )
        """

    def testCampaignsRetrieveErrorResponse400(self):
        """Test CampaignsRetrieveErrorResponse400"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
