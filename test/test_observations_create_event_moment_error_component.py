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

from mosquito_alert.models.observations_create_event_moment_error_component import ObservationsCreateEventMomentErrorComponent

class TestObservationsCreateEventMomentErrorComponent(unittest.TestCase):
    """ObservationsCreateEventMomentErrorComponent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ObservationsCreateEventMomentErrorComponent:
        """Test ObservationsCreateEventMomentErrorComponent
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ObservationsCreateEventMomentErrorComponent`
        """
        model = ObservationsCreateEventMomentErrorComponent()
        if include_optional:
            return ObservationsCreateEventMomentErrorComponent(
                attr = 'event_moment',
                code = 'invalid_choice',
                detail = ''
            )
        else:
            return ObservationsCreateEventMomentErrorComponent(
                attr = 'event_moment',
                code = 'invalid_choice',
                detail = '',
        )
        """

    def testObservationsCreateEventMomentErrorComponent(self):
        """Test ObservationsCreateEventMomentErrorComponent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
