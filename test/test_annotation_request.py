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

from mosquito_alert.models.annotation_request import AnnotationRequest

class TestAnnotationRequest(unittest.TestCase):
    """AnnotationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AnnotationRequest:
        """Test AnnotationRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AnnotationRequest`
        """
        model = AnnotationRequest()
        if include_optional:
            return AnnotationRequest(
                best_photo_uuid = '',
                classification = mosquito_alert.models.annotation_classification_request.AnnotationClassificationRequest(
                    taxon_id = 56, 
                    confidence_label = 'definitely', ),
                characteristics = mosquito_alert.models.annotation_characteristics_request.AnnotationCharacteristicsRequest(
                    sex = 'male', 
                    is_blood_fed = True, 
                    is_gravid = True, ),
                feedback = mosquito_alert.models.annotation_feedback_request.AnnotationFeedbackRequest(
                    public_note = '', 
                    internal_note = '', 
                    user_note = '', ),
                is_flagged = True,
                is_decisive = True,
                observation_flags = mosquito_alert.models.observation_flags_request.ObservationFlagsRequest(
                    is_favourite = True, 
                    is_visible = True, ),
                tags = [
                    '0'
                    ]
            )
        else:
            return AnnotationRequest(
                classification = mosquito_alert.models.annotation_classification_request.AnnotationClassificationRequest(
                    taxon_id = 56, 
                    confidence_label = 'definitely', ),
        )
        """

    def testAnnotationRequest(self):
        """Test AnnotationRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
