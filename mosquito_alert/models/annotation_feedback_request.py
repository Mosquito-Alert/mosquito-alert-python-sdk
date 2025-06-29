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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class AnnotationFeedbackRequest(BaseModel):
    """
    AnnotationFeedbackRequest
    """ # noqa: E501
    public_note: Optional[StrictStr] = Field(default=None, description="Notes to display on public map")
    internal_note: Optional[StrictStr] = Field(default=None, description="Internal notes for yourself or other experts")
    user_note: Optional[StrictStr] = Field(default=None, description="Message that user will receive when viewing report on phone")
    __properties: ClassVar[List[str]] = ["public_note", "internal_note", "user_note"]

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
        """Create an instance of AnnotationFeedbackRequest from a JSON string"""
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
        # set to None if public_note (nullable) is None
        # and model_fields_set contains the field
        if self.public_note is None and "public_note" in self.model_fields_set:
            _dict['public_note'] = None

        # set to None if internal_note (nullable) is None
        # and model_fields_set contains the field
        if self.internal_note is None and "internal_note" in self.model_fields_set:
            _dict['internal_note'] = None

        # set to None if user_note (nullable) is None
        # and model_fields_set contains the field
        if self.user_note is None and "user_note" in self.model_fields_set:
            _dict['user_note'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AnnotationFeedbackRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "public_note": obj.get("public_note"),
            "internal_note": obj.get("internal_note"),
            "user_note": obj.get("user_note")
        })
        return _obj


