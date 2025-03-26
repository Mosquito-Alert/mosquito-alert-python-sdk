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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mosquito_alert.models.location_request import LocationRequest
from typing import Optional, Set
from typing_extensions import Self

class BiteRequest(BaseModel):
    """
    BiteRequest
    """ # noqa: E501
    created_at: datetime
    sent_at: datetime
    location: LocationRequest
    note: Optional[StrictStr] = Field(default=None, description="Note user attached to report.")
    tags: Optional[List[Annotated[str, Field(min_length=1, strict=True)]]] = None
    event_environment: Optional[StrictStr] = Field(default=None, description="The environment where the event took place.")
    event_moment: Optional[StrictStr] = Field(default=None, description="The moment of the day when the event took place.")
    head_bite_count: Optional[StrictInt] = Field(default=0, description="Number of bites reported in the head.")
    left_arm_bite_count: Optional[StrictInt] = Field(default=0, description="Number of bites reported in the left arm.")
    right_arm_bite_count: Optional[StrictInt] = Field(default=0, description="Number of bites reported in the right arm.")
    chest_bite_count: Optional[StrictInt] = Field(default=0, description="Number of bites reported in the chest.")
    left_leg_bite_count: Optional[StrictInt] = Field(default=0, description="Number of bites reported in the left leg.")
    right_leg_bite_count: Optional[StrictInt] = Field(default=0, description="Number of bites reported in the right leg.")
    __properties: ClassVar[List[str]] = ["created_at", "sent_at", "location", "note", "tags", "event_environment", "event_moment", "head_bite_count", "left_arm_bite_count", "right_arm_bite_count", "chest_bite_count", "left_leg_bite_count", "right_leg_bite_count"]

    @field_validator('event_environment')
    def event_environment_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['indoors', 'outdoors', 'vehicle', '']):
            raise ValueError("must be one of enum values ('indoors', 'outdoors', 'vehicle', '')")
        return value

    @field_validator('event_moment')
    def event_moment_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['now', 'last_morning', 'last_midday', 'last_afternoon', 'last_night', '']):
            raise ValueError("must be one of enum values ('now', 'last_morning', 'last_midday', 'last_afternoon', 'last_night', '')")
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
        """Create an instance of BiteRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # set to None if note (nullable) is None
        # and model_fields_set contains the field
        if self.note is None and "note" in self.model_fields_set:
            _dict['note'] = None

        # set to None if event_environment (nullable) is None
        # and model_fields_set contains the field
        if self.event_environment is None and "event_environment" in self.model_fields_set:
            _dict['event_environment'] = None

        # set to None if event_moment (nullable) is None
        # and model_fields_set contains the field
        if self.event_moment is None and "event_moment" in self.model_fields_set:
            _dict['event_moment'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BiteRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "sent_at": obj.get("sent_at"),
            "location": LocationRequest.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "note": obj.get("note"),
            "tags": obj.get("tags"),
            "event_environment": obj.get("event_environment"),
            "event_moment": obj.get("event_moment"),
            "head_bite_count": obj.get("head_bite_count") if obj.get("head_bite_count") is not None else 0,
            "left_arm_bite_count": obj.get("left_arm_bite_count") if obj.get("left_arm_bite_count") is not None else 0,
            "right_arm_bite_count": obj.get("right_arm_bite_count") if obj.get("right_arm_bite_count") is not None else 0,
            "chest_bite_count": obj.get("chest_bite_count") if obj.get("chest_bite_count") is not None else 0,
            "left_leg_bite_count": obj.get("left_leg_bite_count") if obj.get("left_leg_bite_count") is not None else 0,
            "right_leg_bite_count": obj.get("right_leg_bite_count") if obj.get("right_leg_bite_count") is not None else 0
        })
        return _obj


