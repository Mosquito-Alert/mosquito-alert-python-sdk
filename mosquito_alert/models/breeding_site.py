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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from mosquito_alert.models.location import Location
from mosquito_alert.models.simple_photo import SimplePhoto
from typing import Optional, Set
from typing_extensions import Self

class BreedingSite(BaseModel):
    """
    BreedingSite
    """ # noqa: E501
    uuid: StrictStr
    short_id: StrictStr
    user_uuid: StrictStr
    created_at: datetime
    created_at_local: datetime = Field(description="The date and time when the record was created, displayed in the local timezone specified for this entry.")
    sent_at: datetime
    received_at: datetime
    updated_at: datetime = Field(description="Date and time when the report was last modified")
    location: Location
    note: Optional[StrictStr] = Field(default=None, description="Note user attached to report.")
    tags: Optional[List[StrictStr]] = None
    published: StrictBool
    photos: List[SimplePhoto]
    site_type: Optional[StrictStr] = Field(default=None, description="Breeding site type.")
    has_water: Optional[StrictBool] = Field(default=None, description="Either if the user perceived water in the breeding site.")
    in_public_area: Optional[StrictBool] = Field(default=None, description="Either if the breeding site is found in a public area.")
    has_near_mosquitoes: Optional[StrictBool] = Field(default=None, description="Either if the user perceived mosquitoes near the breeding site (less than 10 meters).")
    has_larvae: Optional[StrictBool] = Field(default=None, description="Either if the user perceived larvaes the breeding site.")
    __properties: ClassVar[List[str]] = ["uuid", "short_id", "user_uuid", "created_at", "created_at_local", "sent_at", "received_at", "updated_at", "location", "note", "tags", "published", "photos", "site_type", "has_water", "in_public_area", "has_near_mosquitoes", "has_larvae"]

    @field_validator('site_type')
    def site_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['basin', 'bucket', 'fountain', 'small_container', 'storm_drain', 'well', 'other', '']):
            raise ValueError("must be one of enum values ('basin', 'bucket', 'fountain', 'small_container', 'storm_drain', 'well', 'other', '')")
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
        """Create an instance of BreedingSite from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "uuid",
            "short_id",
            "user_uuid",
            "created_at_local",
            "received_at",
            "updated_at",
            "published",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in photos (list)
        _items = []
        if self.photos:
            for _item_photos in self.photos:
                if _item_photos:
                    _items.append(_item_photos.to_dict())
            _dict['photos'] = _items
        # set to None if note (nullable) is None
        # and model_fields_set contains the field
        if self.note is None and "note" in self.model_fields_set:
            _dict['note'] = None

        # set to None if has_water (nullable) is None
        # and model_fields_set contains the field
        if self.has_water is None and "has_water" in self.model_fields_set:
            _dict['has_water'] = None

        # set to None if in_public_area (nullable) is None
        # and model_fields_set contains the field
        if self.in_public_area is None and "in_public_area" in self.model_fields_set:
            _dict['in_public_area'] = None

        # set to None if has_near_mosquitoes (nullable) is None
        # and model_fields_set contains the field
        if self.has_near_mosquitoes is None and "has_near_mosquitoes" in self.model_fields_set:
            _dict['has_near_mosquitoes'] = None

        # set to None if has_larvae (nullable) is None
        # and model_fields_set contains the field
        if self.has_larvae is None and "has_larvae" in self.model_fields_set:
            _dict['has_larvae'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BreedingSite from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uuid": obj.get("uuid"),
            "short_id": obj.get("short_id"),
            "user_uuid": obj.get("user_uuid"),
            "created_at": obj.get("created_at"),
            "created_at_local": obj.get("created_at_local"),
            "sent_at": obj.get("sent_at"),
            "received_at": obj.get("received_at"),
            "updated_at": obj.get("updated_at"),
            "location": Location.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "note": obj.get("note"),
            "tags": obj.get("tags"),
            "published": obj.get("published"),
            "photos": [SimplePhoto.from_dict(_item) for _item in obj["photos"]] if obj.get("photos") is not None else None,
            "site_type": obj.get("site_type"),
            "has_water": obj.get("has_water"),
            "in_public_area": obj.get("in_public_area"),
            "has_near_mosquitoes": obj.get("has_near_mosquitoes"),
            "has_larvae": obj.get("has_larvae")
        })
        return _obj


