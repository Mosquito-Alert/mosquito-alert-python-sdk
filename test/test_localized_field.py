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

from mosquito_alert.models.localized_field import LocalizedField

class TestLocalizedField(unittest.TestCase):
    """LocalizedField unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LocalizedField:
        """Test LocalizedField
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LocalizedField`
        """
        model = LocalizedField()
        if include_optional:
            return LocalizedField(
                bg = '',
                bn = '',
                ca = '',
                de = '',
                el = '',
                en = '',
                es = '',
                eu = '',
                fr = '',
                gl = '',
                hr = '',
                hu = '',
                it = '',
                lb = '',
                mk = '',
                nl = '',
                pt = '',
                ro = '',
                sl = '',
                sq = '',
                sr = '',
                sv = '',
                tr = '',
                zh_cn = ''
            )
        else:
            return LocalizedField(
                en = '',
        )
        """

    def testLocalizedField(self):
        """Test LocalizedField"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
