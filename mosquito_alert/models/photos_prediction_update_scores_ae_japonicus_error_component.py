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

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class PhotosPredictionUpdateScoresAeJaponicusErrorComponent(BaseModel):
    """
    PhotosPredictionUpdateScoresAeJaponicusErrorComponent
    """ # noqa: E501
    attr: StrictStr
    code: StrictStr
    detail: StrictStr
    __properties: ClassVar[List[str]] = ["attr", "code", "detail"]

    @field_validator('attr')
    def attr_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['scores.ae_japonicus']):
            raise ValueError("must be one of enum values ('scores.ae_japonicus')")
        return value

    @field_validator('code')
    def code_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['invalid', 'max_string_length', 'max_value', 'min_value', 'null', 'required']):
            raise ValueError("must be one of enum values ('invalid', 'max_string_length', 'max_value', 'min_value', 'null', 'required')")
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
        """Create an instance of PhotosPredictionUpdateScoresAeJaponicusErrorComponent from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PhotosPredictionUpdateScoresAeJaponicusErrorComponent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "attr": obj.get("attr"),
            "code": obj.get("code"),
            "detail": obj.get("detail")
        })
        return _obj


