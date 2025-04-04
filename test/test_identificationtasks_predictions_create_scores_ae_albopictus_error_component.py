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

from mosquito_alert.models.identificationtasks_predictions_create_scores_ae_albopictus_error_component import IdentificationtasksPredictionsCreateScoresAeAlbopictusErrorComponent

class TestIdentificationtasksPredictionsCreateScoresAeAlbopictusErrorComponent(unittest.TestCase):
    """IdentificationtasksPredictionsCreateScoresAeAlbopictusErrorComponent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdentificationtasksPredictionsCreateScoresAeAlbopictusErrorComponent:
        """Test IdentificationtasksPredictionsCreateScoresAeAlbopictusErrorComponent
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdentificationtasksPredictionsCreateScoresAeAlbopictusErrorComponent`
        """
        model = IdentificationtasksPredictionsCreateScoresAeAlbopictusErrorComponent()
        if include_optional:
            return IdentificationtasksPredictionsCreateScoresAeAlbopictusErrorComponent(
                attr = 'scores.ae_albopictus',
                code = 'invalid',
                detail = ''
            )
        else:
            return IdentificationtasksPredictionsCreateScoresAeAlbopictusErrorComponent(
                attr = 'scores.ae_albopictus',
                code = 'invalid',
                detail = '',
        )
        """

    def testIdentificationtasksPredictionsCreateScoresAeAlbopictusErrorComponent(self):
        """Test IdentificationtasksPredictionsCreateScoresAeAlbopictusErrorComponent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
