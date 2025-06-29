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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from mosquito_alert.models.annotation_classification import AnnotationClassification
from mosquito_alert.models.annotation_feedback import AnnotationFeedback
from mosquito_alert.models.observation_flags import ObservationFlags
from mosquito_alert.models.simple_annotator_user import SimpleAnnotatorUser
from mosquito_alert.models.simple_photo import SimplePhoto
from typing import Optional, Set
from typing_extensions import Self

class Annotation(BaseModel):
    """
    Annotation
    """ # noqa: E501
    id: StrictInt
    observation_uuid: StrictStr = Field(description="UUID randomly generated on phone to identify each unique report version. Must be exactly 36 characters (32 hex digits plus 4 hyphens).")
    user: SimpleAnnotatorUser
    best_photo: Optional[SimplePhoto]
    classification: Optional[AnnotationClassification]
    feedback: Optional[AnnotationFeedback] = None
    type: StrictStr
    is_flagged: StrictBool
    is_decisive: StrictBool
    observation_flags: Optional[ObservationFlags] = None
    tags: Optional[List[StrictStr]] = None
    created_at: datetime
    updated_at: datetime
    __properties: ClassVar[List[str]] = ["id", "observation_uuid", "user", "best_photo", "classification", "feedback", "type", "is_flagged", "is_decisive", "observation_flags", "tags", "created_at", "updated_at"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['short', 'long']):
            raise ValueError("must be one of enum values ('short', 'long')")
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
        """Create an instance of Annotation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "observation_uuid",
            "user",
            "best_photo",
            "type",
            "is_flagged",
            "is_decisive",
            "created_at",
            "updated_at",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of best_photo
        if self.best_photo:
            _dict['best_photo'] = self.best_photo.to_dict()
        # override the default output from pydantic by calling `to_dict()` of classification
        if self.classification:
            _dict['classification'] = self.classification.to_dict()
        # override the default output from pydantic by calling `to_dict()` of feedback
        if self.feedback:
            _dict['feedback'] = self.feedback.to_dict()
        # override the default output from pydantic by calling `to_dict()` of observation_flags
        if self.observation_flags:
            _dict['observation_flags'] = self.observation_flags.to_dict()
        # set to None if best_photo (nullable) is None
        # and model_fields_set contains the field
        if self.best_photo is None and "best_photo" in self.model_fields_set:
            _dict['best_photo'] = None

        # set to None if classification (nullable) is None
        # and model_fields_set contains the field
        if self.classification is None and "classification" in self.model_fields_set:
            _dict['classification'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Annotation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "observation_uuid": obj.get("observation_uuid"),
            "user": SimpleAnnotatorUser.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "best_photo": SimplePhoto.from_dict(obj["best_photo"]) if obj.get("best_photo") is not None else None,
            "classification": AnnotationClassification.from_dict(obj["classification"]) if obj.get("classification") is not None else None,
            "feedback": AnnotationFeedback.from_dict(obj["feedback"]) if obj.get("feedback") is not None else None,
            "type": obj.get("type"),
            "is_flagged": obj.get("is_flagged") if obj.get("is_flagged") is not None else False,
            "is_decisive": obj.get("is_decisive") if obj.get("is_decisive") is not None else False,
            "observation_flags": ObservationFlags.from_dict(obj["observation_flags"]) if obj.get("observation_flags") is not None else None,
            "tags": obj.get("tags"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


