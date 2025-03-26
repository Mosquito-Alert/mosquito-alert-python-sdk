# coding: utf-8

"""
    Mosquito Alert API

    Introducing API v1 for Mosquito Alert platform, a project desgined to facilitate citizen science initiatives and enable collaboration among scientists, public health officials, and environmental managers in the investigation and control of disease-carrying mosquitoes.

    The version of the OpenAPI document: v1
    Contact: it@mosquitoalert.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from mosquito_alert.models.bounding_box_request import BoundingBoxRequest
from mosquito_alert.models.prediction_score_request import PredictionScoreRequest
from typing import Optional, Set
from typing_extensions import Self

class CreatePhotoPredictionRequest(BaseModel):
    """
    CreatePhotoPredictionRequest
    """ # noqa: E501
    photo_uuid: StrictStr
    bbox: BoundingBoxRequest
    insect_confidence: Union[Annotated[float, Field(le=1.0, strict=True, ge=0.0)], Annotated[int, Field(le=1, strict=True, ge=0)]] = Field(description="Insect confidence")
    predicted_class: StrictStr
    threshold_deviation: Union[Annotated[float, Field(le=1.0, strict=True, ge=-1.0)], Annotated[int, Field(le=1, strict=True, ge=-1)]]
    is_final_prediction: Optional[StrictBool] = Field(default=None, description="Indicates if this prediction can close the identification task.")
    scores: PredictionScoreRequest
    classifier_version: StrictStr
    __properties: ClassVar[List[str]] = ["photo_uuid", "bbox", "insect_confidence", "predicted_class", "threshold_deviation", "is_final_prediction", "scores", "classifier_version"]

    @field_validator('predicted_class')
    def predicted_class_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['ae_albopictus', 'ae_aegypti', 'ae_japonicus', 'ae_koreicus', 'culex', 'anopheles', 'culiseta', 'other_species', 'not_sure']):
            raise ValueError("must be one of enum values ('ae_albopictus', 'ae_aegypti', 'ae_japonicus', 'ae_koreicus', 'culex', 'anopheles', 'culiseta', 'other_species', 'not_sure')")
        return value

    @field_validator('classifier_version')
    def classifier_version_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['v2023.1', 'v2024.1', 'v2025.1']):
            raise ValueError("must be one of enum values ('v2023.1', 'v2024.1', 'v2025.1')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CreatePhotoPredictionRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of bbox
        if self.bbox:
            _dict['bbox'] = self.bbox.to_dict()
        # override the default output from pydantic by calling `to_dict()` of scores
        if self.scores:
            _dict['scores'] = self.scores.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreatePhotoPredictionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "photo_uuid": obj.get("photo_uuid"),
            "bbox": BoundingBoxRequest.from_dict(obj["bbox"]) if obj.get("bbox") is not None else None,
            "insect_confidence": obj.get("insect_confidence"),
            "predicted_class": obj.get("predicted_class"),
            "threshold_deviation": obj.get("threshold_deviation"),
            "is_final_prediction": obj.get("is_final_prediction"),
            "scores": PredictionScoreRequest.from_dict(obj["scores"]) if obj.get("scores") is not None else None,
            "classifier_version": obj.get("classifier_version")
        })
        return _obj


