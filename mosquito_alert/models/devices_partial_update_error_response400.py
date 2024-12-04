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
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from mosquito_alert.models.devices_partial_update_validation_error import DevicesPartialUpdateValidationError
from mosquito_alert.models.parse_error_response import ParseErrorResponse
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

DEVICESPARTIALUPDATEERRORRESPONSE400_ONE_OF_SCHEMAS = ["DevicesPartialUpdateValidationError", "ParseErrorResponse"]

class DevicesPartialUpdateErrorResponse400(BaseModel):
    """
    DevicesPartialUpdateErrorResponse400
    """
    # data type: DevicesPartialUpdateValidationError
    oneof_schema_1_validator: Optional[DevicesPartialUpdateValidationError] = None
    # data type: ParseErrorResponse
    oneof_schema_2_validator: Optional[ParseErrorResponse] = None
    actual_instance: Optional[Union[DevicesPartialUpdateValidationError, ParseErrorResponse]] = None
    one_of_schemas: Set[str] = { "DevicesPartialUpdateValidationError", "ParseErrorResponse" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    discriminator_value_class_map: Dict[str, str] = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = DevicesPartialUpdateErrorResponse400.model_construct()
        error_messages = []
        match = 0
        # validate data type: DevicesPartialUpdateValidationError
        if not isinstance(v, DevicesPartialUpdateValidationError):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DevicesPartialUpdateValidationError`")
        else:
            match += 1
        # validate data type: ParseErrorResponse
        if not isinstance(v, ParseErrorResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ParseErrorResponse`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in DevicesPartialUpdateErrorResponse400 with oneOf schemas: DevicesPartialUpdateValidationError, ParseErrorResponse. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in DevicesPartialUpdateErrorResponse400 with oneOf schemas: DevicesPartialUpdateValidationError, ParseErrorResponse. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into DevicesPartialUpdateValidationError
        try:
            instance.actual_instance = DevicesPartialUpdateValidationError.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ParseErrorResponse
        try:
            instance.actual_instance = ParseErrorResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into DevicesPartialUpdateErrorResponse400 with oneOf schemas: DevicesPartialUpdateValidationError, ParseErrorResponse. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into DevicesPartialUpdateErrorResponse400 with oneOf schemas: DevicesPartialUpdateValidationError, ParseErrorResponse. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], DevicesPartialUpdateValidationError, ParseErrorResponse]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


