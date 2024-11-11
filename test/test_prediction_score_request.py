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

from mosquito_alert_api.models.prediction_score_request import PredictionScoreRequest

class TestPredictionScoreRequest(unittest.TestCase):
    """PredictionScoreRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PredictionScoreRequest:
        """Test PredictionScoreRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PredictionScoreRequest`
        """
        model = PredictionScoreRequest()
        if include_optional:
            return PredictionScoreRequest(
                ae_albopictus = 0.0,
                ae_aegypti = 0.0,
                ae_japonicus = 0.0,
                ae_koreicus = 0.0,
                culex = 0.0,
                anopheles = 0.0,
                culiseta = 0.0,
                other_species = 0.0,
                not_sure = 0.0
            )
        else:
            return PredictionScoreRequest(
                ae_albopictus = 0.0,
                ae_aegypti = 0.0,
                ae_japonicus = 0.0,
                ae_koreicus = 0.0,
                culex = 0.0,
                anopheles = 0.0,
                culiseta = 0.0,
                other_species = 0.0,
                not_sure = 0.0,
        )
        """

    def testPredictionScoreRequest(self):
        """Test PredictionScoreRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()