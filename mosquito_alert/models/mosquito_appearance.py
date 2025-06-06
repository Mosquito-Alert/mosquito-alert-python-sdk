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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class MosquitoAppearance(BaseModel):
    """
    MosquitoAppearance
    """ # noqa: E501
    specie: Optional[StrictStr] = Field(default=None, description="The mosquito specie perceived by the user.")
    thorax: Optional[StrictStr] = Field(default=None, description="The species of mosquito that the thorax resembles, according to the user.")
    abdomen: Optional[StrictStr] = Field(default=None, description="The species of mosquito that the abdomen resembles, according to the user.")
    legs: Optional[StrictStr] = Field(default=None, description="The species of mosquito that the leg resembles, according to the user.")
    __properties: ClassVar[List[str]] = ["specie", "thorax", "abdomen", "legs"]

    @field_validator('specie')
    def specie_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['albopictus', 'aegypti', 'japonicus', 'koreicus', 'culex', 'other', '']):
            raise ValueError("must be one of enum values ('albopictus', 'aegypti', 'japonicus', 'koreicus', 'culex', 'other', '')")
        return value

    @field_validator('thorax')
    def thorax_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['albopictus', 'aegypti', 'japonicus', 'koreicus', 'culex', 'other', '']):
            raise ValueError("must be one of enum values ('albopictus', 'aegypti', 'japonicus', 'koreicus', 'culex', 'other', '')")
        return value

    @field_validator('abdomen')
    def abdomen_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['albopictus', 'aegypti', 'japonicus', 'koreicus', 'culex', 'other', '']):
            raise ValueError("must be one of enum values ('albopictus', 'aegypti', 'japonicus', 'koreicus', 'culex', 'other', '')")
        return value

    @field_validator('legs')
    def legs_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['albopictus', 'aegypti', 'japonicus', 'koreicus', 'culex', 'other', '']):
            raise ValueError("must be one of enum values ('albopictus', 'aegypti', 'japonicus', 'koreicus', 'culex', 'other', '')")
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
        """Create an instance of MosquitoAppearance from a JSON string"""
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
        # set to None if specie (nullable) is None
        # and model_fields_set contains the field
        if self.specie is None and "specie" in self.model_fields_set:
            _dict['specie'] = None

        # set to None if thorax (nullable) is None
        # and model_fields_set contains the field
        if self.thorax is None and "thorax" in self.model_fields_set:
            _dict['thorax'] = None

        # set to None if abdomen (nullable) is None
        # and model_fields_set contains the field
        if self.abdomen is None and "abdomen" in self.model_fields_set:
            _dict['abdomen'] = None

        # set to None if legs (nullable) is None
        # and model_fields_set contains the field
        if self.legs is None and "legs" in self.model_fields_set:
            _dict['legs'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MosquitoAppearance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "specie": obj.get("specie"),
            "thorax": obj.get("thorax"),
            "abdomen": obj.get("abdomen"),
            "legs": obj.get("legs")
        })
        return _obj


