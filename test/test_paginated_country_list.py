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

from mosquito_alert.models.paginated_country_list import PaginatedCountryList

class TestPaginatedCountryList(unittest.TestCase):
    """PaginatedCountryList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedCountryList:
        """Test PaginatedCountryList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedCountryList`
        """
        model = PaginatedCountryList()
        if include_optional:
            return PaginatedCountryList(
                count = 123,
                next = 'http://api.example.org/accounts/?page=4',
                previous = 'http://api.example.org/accounts/?page=2',
                results = [
                    mosquito_alert.models.country.Country(
                        id = 56, 
                        name_en = '', 
                        iso3_code = '', )
                    ]
            )
        else:
            return PaginatedCountryList(
        )
        """

    def testPaginatedCountryList(self):
        """Test PaginatedCountryList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
