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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class LocalizedFieldRequest(BaseModel):
    """
    A custom serializer field that supports localization for a dynamic field name. Allows calling with arguments such as 'title', 'message', max_length, help_text, etc.
    """ # noqa: E501
    bg: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, description="Български")
    bn: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, description="বাংলা")
    ca: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, description="Català")
    de: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, description="Deutsch")
    el: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, description="Ελληνικά")
    en: Annotated[str, Field(min_length=1, strict=True, max_length=255)] = Field(description="English")
    es: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, description="Español")
    eu: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, description="Euskara")
    fr: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, description="Français")
    gl: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, description="Galego")
    hr: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, description="Hrvatski")
    hu: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, description="Magyar")
    it: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, description="Italiano")
    lb: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, description="Lëtzebuergesch")
    mk: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, description="Македонски")
    nl: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, description="Nederlands")
    pt: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, description="Português")
    ro: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, description="Română")
    sl: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, description="Slovenščina")
    sq: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, description="Shqip")
    sr: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, description="Српски")
    sv: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, description="Svenska")
    tr: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, description="Türkçe")
    zh_cn: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, description="中文（中国）", alias="zh-CN")
    __properties: ClassVar[List[str]] = ["bg", "bn", "ca", "de", "el", "en", "es", "eu", "fr", "gl", "hr", "hu", "it", "lb", "mk", "nl", "pt", "ro", "sl", "sq", "sr", "sv", "tr", "zh-CN"]

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
        """Create an instance of LocalizedFieldRequest from a JSON string"""
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
        """Create an instance of LocalizedFieldRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bg": obj.get("bg"),
            "bn": obj.get("bn"),
            "ca": obj.get("ca"),
            "de": obj.get("de"),
            "el": obj.get("el"),
            "en": obj.get("en"),
            "es": obj.get("es"),
            "eu": obj.get("eu"),
            "fr": obj.get("fr"),
            "gl": obj.get("gl"),
            "hr": obj.get("hr"),
            "hu": obj.get("hu"),
            "it": obj.get("it"),
            "lb": obj.get("lb"),
            "mk": obj.get("mk"),
            "nl": obj.get("nl"),
            "pt": obj.get("pt"),
            "ro": obj.get("ro"),
            "sl": obj.get("sl"),
            "sq": obj.get("sq"),
            "sr": obj.get("sr"),
            "sv": obj.get("sv"),
            "tr": obj.get("tr"),
            "zh-CN": obj.get("zh-CN")
        })
        return _obj


