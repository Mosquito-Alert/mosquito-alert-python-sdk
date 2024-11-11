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

from mosquito_alert_api.models.paginated_observation_list import PaginatedObservationList

class TestPaginatedObservationList(unittest.TestCase):
    """PaginatedObservationList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedObservationList:
        """Test PaginatedObservationList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedObservationList`
        """
        model = PaginatedObservationList()
        if include_optional:
            return PaginatedObservationList(
                count = 123,
                next = '',
                previous = '',
                results = [
                    mosquito_alert_api.models.observation.Observation(
                        uuid = '', 
                        short_id = '', 
                        user_uuid = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created_at_local = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        sent_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        received_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        location = mosquito_alert_api.models.report_location.ReportLocation(
                            type = 'current', 
                            point = mosquito_alert_api.models.report_location_point.ReportLocation_point(
                                latitude = 1.337, 
                                longitude = 1.337, ), 
                            timezone = 'Africa/Abidjan', 
                            country_id = 56, 
                            nuts_2 = '', 
                            nuts_3 = '', ), 
                        note = '', 
                        tags = [
                            ''
                            ], 
                        published = True, 
                        photos = [
                            mosquito_alert_api.models.report_photo.ReportPhoto(
                                uuid = '', 
                                url = '', )
                            ], 
                        event_environment = 'indoors', 
                        event_moment = 'now', 
                        user_perceived_mosquito_specie = 'albopictus', 
                        user_perceived_mosquito_thorax = 'albopictus', 
                        user_perceived_mosquito_abdomen = 'albopictus', 
                        user_perceived_mosquito_legs = 'albopictus', )
                    ]
            )
        else:
            return PaginatedObservationList(
        )
        """

    def testPaginatedObservationList(self):
        """Test PaginatedObservationList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
