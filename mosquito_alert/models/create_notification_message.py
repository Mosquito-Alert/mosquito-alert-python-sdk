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
from typing import Any, ClassVar, Dict, List
from mosquito_alert.models.localized_message_body import LocalizedMessageBody
from mosquito_alert.models.localized_message_title import LocalizedMessageTitle
from typing import Optional, Set
from typing_extensions import Self

class CreateNotificationMessage(BaseModel):
    """
    CreateNotificationMessage
    """ # noqa: E501
    title: LocalizedMessageTitle = Field(description="Provide the message's title in all supported languages")
    body: LocalizedMessageBody = Field(description="Provide the message's body in all supported languages")
    __properties: ClassVar[List[str]] = ["title", "body"]

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
        """Create an instance of CreateNotificationMessage from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of title
        if self.title:
            _dict['title'] = self.title.to_dict()
        # override the default output from pydantic by calling `to_dict()` of body
        if self.body:
            _dict['body'] = self.body.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateNotificationMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": LocalizedMessageTitle.from_dict(obj["title"]) if obj.get("title") is not None else None,
            "body": LocalizedMessageBody.from_dict(obj["body"]) if obj.get("body") is not None else None
        })
        return _obj


