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

from mosquito_alert.models.bite import Bite

class TestBite(unittest.TestCase):
    """Bite unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Bite:
        """Test Bite
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Bite`
        """
        model = Bite()
        if include_optional:
            return Bite(
                uuid = '',
                short_id = '',
                user_uuid = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_at_local = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                sent_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                received_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                location = mosquito_alert.models.location.Location(
                    source = 'auto', 
                    point = mosquito_alert.models.location_point.Location_point(
                        latitude = 1.337, 
                        longitude = 1.337, ), 
                    timezone = 'Africa/Abidjan', 
                    display_name = '', 
                    country_id = 56, 
                    adm_boundaries = [
                        mosquito_alert.models.adm_boundary.AdmBoundary(
                            name = '', 
                            code = '', 
                            source = '', 
                            level = 0, )
                        ], ),
                note = '',
                tags = [
                    ''
                    ],
                published = True,
                event_environment = 'indoors',
                event_moment = 'now',
                counts = mosquito_alert.models.bite_counts.BiteCounts(
                    total = 56, 
                    head = 56, 
                    left_arm = 56, 
                    right_arm = 56, 
                    chest = 56, 
                    left_leg = 56, 
                    right_leg = 56, )
            )
        else:
            return Bite(
                uuid = '',
                short_id = '',
                user_uuid = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_at_local = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                sent_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                received_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                location = mosquito_alert.models.location.Location(
                    source = 'auto', 
                    point = mosquito_alert.models.location_point.Location_point(
                        latitude = 1.337, 
                        longitude = 1.337, ), 
                    timezone = 'Africa/Abidjan', 
                    display_name = '', 
                    country_id = 56, 
                    adm_boundaries = [
                        mosquito_alert.models.adm_boundary.AdmBoundary(
                            name = '', 
                            code = '', 
                            source = '', 
                            level = 0, )
                        ], ),
                published = True,
                counts = mosquito_alert.models.bite_counts.BiteCounts(
                    total = 56, 
                    head = 56, 
                    left_arm = 56, 
                    right_arm = 56, 
                    chest = 56, 
                    left_leg = 56, 
                    right_leg = 56, ),
        )
        """

    def testBite(self):
        """Test Bite"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
