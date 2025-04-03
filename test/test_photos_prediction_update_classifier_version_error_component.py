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

from mosquito_alert.models.photos_prediction_update_classifier_version_error_component import PhotosPredictionUpdateClassifierVersionErrorComponent

class TestPhotosPredictionUpdateClassifierVersionErrorComponent(unittest.TestCase):
    """PhotosPredictionUpdateClassifierVersionErrorComponent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PhotosPredictionUpdateClassifierVersionErrorComponent:
        """Test PhotosPredictionUpdateClassifierVersionErrorComponent
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PhotosPredictionUpdateClassifierVersionErrorComponent`
        """
        model = PhotosPredictionUpdateClassifierVersionErrorComponent()
        if include_optional:
            return PhotosPredictionUpdateClassifierVersionErrorComponent(
                attr = 'classifier_version',
                code = 'invalid_choice',
                detail = ''
            )
        else:
            return PhotosPredictionUpdateClassifierVersionErrorComponent(
                attr = 'classifier_version',
                code = 'invalid_choice',
                detail = '',
        )
        """

    def testPhotosPredictionUpdateClassifierVersionErrorComponent(self):
        """Test PhotosPredictionUpdateClassifierVersionErrorComponent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
