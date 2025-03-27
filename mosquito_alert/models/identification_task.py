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
from typing_extensions import Annotated
from mosquito_alert.models.identification_task_result import IdentificationTaskResult
from mosquito_alert.models.identification_task_revision import IdentificationTaskRevision
from mosquito_alert.models.simple_photo import SimplePhoto
from typing import Optional, Set
from typing_extensions import Self

class IdentificationTask(BaseModel):
    """
    IdentificationTask
    """ # noqa: E501
    uuid: StrictStr
    observation_uuid: StrictStr
    public_photo: SimplePhoto
    assignees_ids: List[StrictInt]
    status: Optional[StrictStr] = None
    is_flagged: StrictBool
    is_safe: StrictBool = Field(description="Indicates if the content is safe for publication.")
    public_note: Optional[StrictStr]
    num_assignations: Annotated[int, Field(strict=True, ge=0)]
    num_annotations: Annotated[int, Field(strict=True, ge=0)]
    revision: Optional[IdentificationTaskRevision]
    result: IdentificationTaskResult
    created_at: datetime
    updated_at: datetime
    __properties: ClassVar[List[str]] = ["uuid", "observation_uuid", "public_photo", "assignees_ids", "status", "is_flagged", "is_safe", "public_note", "num_assignations", "num_annotations", "revision", "result", "created_at", "updated_at"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['open', 'conflict', 'review', 'done', 'archived']):
            raise ValueError("must be one of enum values ('open', 'conflict', 'review', 'done', 'archived')")
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
        """Create an instance of IdentificationTask from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "uuid",
            "assignees_ids",
            "is_flagged",
            "is_safe",
            "public_note",
            "num_assignations",
            "num_annotations",
            "revision",
            "result",
            "created_at",
            "updated_at",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of public_photo
        if self.public_photo:
            _dict['public_photo'] = self.public_photo.to_dict()
        # override the default output from pydantic by calling `to_dict()` of revision
        if self.revision:
            _dict['revision'] = self.revision.to_dict()
        # override the default output from pydantic by calling `to_dict()` of result
        if self.result:
            _dict['result'] = self.result.to_dict()
        # set to None if public_note (nullable) is None
        # and model_fields_set contains the field
        if self.public_note is None and "public_note" in self.model_fields_set:
            _dict['public_note'] = None

        # set to None if revision (nullable) is None
        # and model_fields_set contains the field
        if self.revision is None and "revision" in self.model_fields_set:
            _dict['revision'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IdentificationTask from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uuid": obj.get("uuid"),
            "observation_uuid": obj.get("observation_uuid"),
            "public_photo": SimplePhoto.from_dict(obj["public_photo"]) if obj.get("public_photo") is not None else None,
            "assignees_ids": obj.get("assignees_ids"),
            "status": obj.get("status"),
            "is_flagged": obj.get("is_flagged"),
            "is_safe": obj.get("is_safe"),
            "public_note": obj.get("public_note"),
            "num_assignations": obj.get("num_assignations"),
            "num_annotations": obj.get("num_annotations"),
            "revision": IdentificationTaskRevision.from_dict(obj["revision"]) if obj.get("revision") is not None else None,
            "result": IdentificationTaskResult.from_dict(obj["result"]) if obj.get("result") is not None else None,
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


