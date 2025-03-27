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
from mosquito_alert.models.bites_list_country_id_error_component import BitesListCountryIdErrorComponent
from mosquito_alert.models.bites_list_created_at_error_component import BitesListCreatedAtErrorComponent
from mosquito_alert.models.bites_list_order_by_error_component import BitesListOrderByErrorComponent
from mosquito_alert.models.bites_list_received_at_error_component import BitesListReceivedAtErrorComponent
from mosquito_alert.models.bites_list_short_id_error_component import BitesListShortIdErrorComponent
from mosquito_alert.models.bites_list_updated_at_error_component import BitesListUpdatedAtErrorComponent
from mosquito_alert.models.bites_list_user_uuid_error_component import BitesListUserUuidErrorComponent
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

BITESLISTERROR_ONE_OF_SCHEMAS = ["BitesListCountryIdErrorComponent", "BitesListCreatedAtErrorComponent", "BitesListOrderByErrorComponent", "BitesListReceivedAtErrorComponent", "BitesListShortIdErrorComponent", "BitesListUpdatedAtErrorComponent", "BitesListUserUuidErrorComponent"]

class BitesListError(BaseModel):
    """
    BitesListError
    """
    # data type: BitesListShortIdErrorComponent
    oneof_schema_1_validator: Optional[BitesListShortIdErrorComponent] = None
    # data type: BitesListCreatedAtErrorComponent
    oneof_schema_2_validator: Optional[BitesListCreatedAtErrorComponent] = None
    # data type: BitesListReceivedAtErrorComponent
    oneof_schema_3_validator: Optional[BitesListReceivedAtErrorComponent] = None
    # data type: BitesListUpdatedAtErrorComponent
    oneof_schema_4_validator: Optional[BitesListUpdatedAtErrorComponent] = None
    # data type: BitesListCountryIdErrorComponent
    oneof_schema_5_validator: Optional[BitesListCountryIdErrorComponent] = None
    # data type: BitesListUserUuidErrorComponent
    oneof_schema_6_validator: Optional[BitesListUserUuidErrorComponent] = None
    # data type: BitesListOrderByErrorComponent
    oneof_schema_7_validator: Optional[BitesListOrderByErrorComponent] = None
    actual_instance: Optional[Union[BitesListCountryIdErrorComponent, BitesListCreatedAtErrorComponent, BitesListOrderByErrorComponent, BitesListReceivedAtErrorComponent, BitesListShortIdErrorComponent, BitesListUpdatedAtErrorComponent, BitesListUserUuidErrorComponent]] = None
    one_of_schemas: Set[str] = { "BitesListCountryIdErrorComponent", "BitesListCreatedAtErrorComponent", "BitesListOrderByErrorComponent", "BitesListReceivedAtErrorComponent", "BitesListShortIdErrorComponent", "BitesListUpdatedAtErrorComponent", "BitesListUserUuidErrorComponent" }

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
        instance = BitesListError.model_construct()
        error_messages = []
        match = 0
        # validate data type: BitesListShortIdErrorComponent
        if not isinstance(v, BitesListShortIdErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BitesListShortIdErrorComponent`")
        else:
            match += 1
        # validate data type: BitesListCreatedAtErrorComponent
        if not isinstance(v, BitesListCreatedAtErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BitesListCreatedAtErrorComponent`")
        else:
            match += 1
        # validate data type: BitesListReceivedAtErrorComponent
        if not isinstance(v, BitesListReceivedAtErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BitesListReceivedAtErrorComponent`")
        else:
            match += 1
        # validate data type: BitesListUpdatedAtErrorComponent
        if not isinstance(v, BitesListUpdatedAtErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BitesListUpdatedAtErrorComponent`")
        else:
            match += 1
        # validate data type: BitesListCountryIdErrorComponent
        if not isinstance(v, BitesListCountryIdErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BitesListCountryIdErrorComponent`")
        else:
            match += 1
        # validate data type: BitesListUserUuidErrorComponent
        if not isinstance(v, BitesListUserUuidErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BitesListUserUuidErrorComponent`")
        else:
            match += 1
        # validate data type: BitesListOrderByErrorComponent
        if not isinstance(v, BitesListOrderByErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BitesListOrderByErrorComponent`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in BitesListError with oneOf schemas: BitesListCountryIdErrorComponent, BitesListCreatedAtErrorComponent, BitesListOrderByErrorComponent, BitesListReceivedAtErrorComponent, BitesListShortIdErrorComponent, BitesListUpdatedAtErrorComponent, BitesListUserUuidErrorComponent. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in BitesListError with oneOf schemas: BitesListCountryIdErrorComponent, BitesListCreatedAtErrorComponent, BitesListOrderByErrorComponent, BitesListReceivedAtErrorComponent, BitesListShortIdErrorComponent, BitesListUpdatedAtErrorComponent, BitesListUserUuidErrorComponent. Details: " + ", ".join(error_messages))
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

        # deserialize data into BitesListShortIdErrorComponent
        try:
            instance.actual_instance = BitesListShortIdErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BitesListCreatedAtErrorComponent
        try:
            instance.actual_instance = BitesListCreatedAtErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BitesListReceivedAtErrorComponent
        try:
            instance.actual_instance = BitesListReceivedAtErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BitesListUpdatedAtErrorComponent
        try:
            instance.actual_instance = BitesListUpdatedAtErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BitesListCountryIdErrorComponent
        try:
            instance.actual_instance = BitesListCountryIdErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BitesListUserUuidErrorComponent
        try:
            instance.actual_instance = BitesListUserUuidErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BitesListOrderByErrorComponent
        try:
            instance.actual_instance = BitesListOrderByErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into BitesListError with oneOf schemas: BitesListCountryIdErrorComponent, BitesListCreatedAtErrorComponent, BitesListOrderByErrorComponent, BitesListReceivedAtErrorComponent, BitesListShortIdErrorComponent, BitesListUpdatedAtErrorComponent, BitesListUserUuidErrorComponent. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into BitesListError with oneOf schemas: BitesListCountryIdErrorComponent, BitesListCreatedAtErrorComponent, BitesListOrderByErrorComponent, BitesListReceivedAtErrorComponent, BitesListShortIdErrorComponent, BitesListUpdatedAtErrorComponent, BitesListUserUuidErrorComponent. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], BitesListCountryIdErrorComponent, BitesListCreatedAtErrorComponent, BitesListOrderByErrorComponent, BitesListReceivedAtErrorComponent, BitesListShortIdErrorComponent, BitesListUpdatedAtErrorComponent, BitesListUserUuidErrorComponent]]:
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


