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

from mosquito_alert.models.paginated_identification_task_list import PaginatedIdentificationTaskList

class TestPaginatedIdentificationTaskList(unittest.TestCase):
    """PaginatedIdentificationTaskList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedIdentificationTaskList:
        """Test PaginatedIdentificationTaskList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedIdentificationTaskList`
        """
        model = PaginatedIdentificationTaskList()
        if include_optional:
            return PaginatedIdentificationTaskList(
                count = 123,
                next = 'http://api.example.org/accounts/?page=4',
                previous = 'http://api.example.org/accounts/?page=2',
                results = [
                    mosquito_alert.models.identification_task.IdentificationTask(
                        observation = null, 
                        public_photo = mosquito_alert.models.simple_photo.SimplePhoto(
                            uuid = '', 
                            url = '', ), 
                        assignees_ids = [
                            56
                            ], 
                        status = 'open', 
                        is_flagged = True, 
                        is_safe = True, 
                        public_note = '', 
                        num_assignations = 0, 
                        num_annotations = 0, 
                        revision = null, 
                        result = null, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return PaginatedIdentificationTaskList(
        )
        """

    def testPaginatedIdentificationTaskList(self):
        """Test PaginatedIdentificationTaskList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
