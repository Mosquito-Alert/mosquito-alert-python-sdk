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

from mosquito_alert.models.bites_list_mine_location_nuts3_error_component import BitesListMineLocationNuts3ErrorComponent

class TestBitesListMineLocationNuts3ErrorComponent(unittest.TestCase):
    """BitesListMineLocationNuts3ErrorComponent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BitesListMineLocationNuts3ErrorComponent:
        """Test BitesListMineLocationNuts3ErrorComponent
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BitesListMineLocationNuts3ErrorComponent`
        """
        model = BitesListMineLocationNuts3ErrorComponent()
        if include_optional:
            return BitesListMineLocationNuts3ErrorComponent(
                attr = 'location_nuts_3',
                code = 'null_characters_not_allowed',
                detail = ''
            )
        else:
            return BitesListMineLocationNuts3ErrorComponent(
                attr = 'location_nuts_3',
                code = 'null_characters_not_allowed',
                detail = '',
        )
        """

    def testBitesListMineLocationNuts3ErrorComponent(self):
        """Test BitesListMineLocationNuts3ErrorComponent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
