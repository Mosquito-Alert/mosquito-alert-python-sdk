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

from mosquito_alert.models.breeding_sites_list_error import BreedingSitesListError

class TestBreedingSitesListError(unittest.TestCase):
    """BreedingSitesListError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BreedingSitesListError:
        """Test BreedingSitesListError
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BreedingSitesListError`
        """
        model = BreedingSitesListError()
        if include_optional:
            return BreedingSitesListError(
                attr = 'order_by',
                code = 'invalid_choice',
                detail = ''
            )
        else:
            return BreedingSitesListError(
                attr = 'order_by',
                code = 'invalid_choice',
                detail = '',
        )
        """

    def testBreedingSitesListError(self):
        """Test BreedingSitesListError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
