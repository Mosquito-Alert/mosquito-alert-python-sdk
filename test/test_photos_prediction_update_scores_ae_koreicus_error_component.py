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

from mosquito_alert.models.photos_prediction_update_scores_ae_koreicus_error_component import PhotosPredictionUpdateScoresAeKoreicusErrorComponent

class TestPhotosPredictionUpdateScoresAeKoreicusErrorComponent(unittest.TestCase):
    """PhotosPredictionUpdateScoresAeKoreicusErrorComponent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PhotosPredictionUpdateScoresAeKoreicusErrorComponent:
        """Test PhotosPredictionUpdateScoresAeKoreicusErrorComponent
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PhotosPredictionUpdateScoresAeKoreicusErrorComponent`
        """
        model = PhotosPredictionUpdateScoresAeKoreicusErrorComponent()
        if include_optional:
            return PhotosPredictionUpdateScoresAeKoreicusErrorComponent(
                attr = 'scores.ae_koreicus',
                code = 'invalid',
                detail = ''
            )
        else:
            return PhotosPredictionUpdateScoresAeKoreicusErrorComponent(
                attr = 'scores.ae_koreicus',
                code = 'invalid',
                detail = '',
        )
        """

    def testPhotosPredictionUpdateScoresAeKoreicusErrorComponent(self):
        """Test PhotosPredictionUpdateScoresAeKoreicusErrorComponent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
