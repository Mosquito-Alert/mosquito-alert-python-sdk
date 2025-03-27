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
from mosquito_alert.models.breedingsites_list_country_id_error_component import BreedingsitesListCountryIdErrorComponent
from mosquito_alert.models.breedingsites_list_created_at_error_component import BreedingsitesListCreatedAtErrorComponent
from mosquito_alert.models.breedingsites_list_order_by_error_component import BreedingsitesListOrderByErrorComponent
from mosquito_alert.models.breedingsites_list_received_at_error_component import BreedingsitesListReceivedAtErrorComponent
from mosquito_alert.models.breedingsites_list_short_id_error_component import BreedingsitesListShortIdErrorComponent
from mosquito_alert.models.breedingsites_list_updated_at_error_component import BreedingsitesListUpdatedAtErrorComponent
from mosquito_alert.models.breedingsites_list_user_uuid_error_component import BreedingsitesListUserUuidErrorComponent
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

BREEDINGSITESLISTERROR_ONE_OF_SCHEMAS = ["BreedingsitesListCountryIdErrorComponent", "BreedingsitesListCreatedAtErrorComponent", "BreedingsitesListOrderByErrorComponent", "BreedingsitesListReceivedAtErrorComponent", "BreedingsitesListShortIdErrorComponent", "BreedingsitesListUpdatedAtErrorComponent", "BreedingsitesListUserUuidErrorComponent"]

class BreedingsitesListError(BaseModel):
    """
    BreedingsitesListError
    """
    # data type: BreedingsitesListShortIdErrorComponent
    oneof_schema_1_validator: Optional[BreedingsitesListShortIdErrorComponent] = None
    # data type: BreedingsitesListCreatedAtErrorComponent
    oneof_schema_2_validator: Optional[BreedingsitesListCreatedAtErrorComponent] = None
    # data type: BreedingsitesListReceivedAtErrorComponent
    oneof_schema_3_validator: Optional[BreedingsitesListReceivedAtErrorComponent] = None
    # data type: BreedingsitesListUpdatedAtErrorComponent
    oneof_schema_4_validator: Optional[BreedingsitesListUpdatedAtErrorComponent] = None
    # data type: BreedingsitesListCountryIdErrorComponent
    oneof_schema_5_validator: Optional[BreedingsitesListCountryIdErrorComponent] = None
    # data type: BreedingsitesListUserUuidErrorComponent
    oneof_schema_6_validator: Optional[BreedingsitesListUserUuidErrorComponent] = None
    # data type: BreedingsitesListOrderByErrorComponent
    oneof_schema_7_validator: Optional[BreedingsitesListOrderByErrorComponent] = None
    actual_instance: Optional[Union[BreedingsitesListCountryIdErrorComponent, BreedingsitesListCreatedAtErrorComponent, BreedingsitesListOrderByErrorComponent, BreedingsitesListReceivedAtErrorComponent, BreedingsitesListShortIdErrorComponent, BreedingsitesListUpdatedAtErrorComponent, BreedingsitesListUserUuidErrorComponent]] = None
    one_of_schemas: Set[str] = { "BreedingsitesListCountryIdErrorComponent", "BreedingsitesListCreatedAtErrorComponent", "BreedingsitesListOrderByErrorComponent", "BreedingsitesListReceivedAtErrorComponent", "BreedingsitesListShortIdErrorComponent", "BreedingsitesListUpdatedAtErrorComponent", "BreedingsitesListUserUuidErrorComponent" }

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
        instance = BreedingsitesListError.model_construct()
        error_messages = []
        match = 0
        # validate data type: BreedingsitesListShortIdErrorComponent
        if not isinstance(v, BreedingsitesListShortIdErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreedingsitesListShortIdErrorComponent`")
        else:
            match += 1
        # validate data type: BreedingsitesListCreatedAtErrorComponent
        if not isinstance(v, BreedingsitesListCreatedAtErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreedingsitesListCreatedAtErrorComponent`")
        else:
            match += 1
        # validate data type: BreedingsitesListReceivedAtErrorComponent
        if not isinstance(v, BreedingsitesListReceivedAtErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreedingsitesListReceivedAtErrorComponent`")
        else:
            match += 1
        # validate data type: BreedingsitesListUpdatedAtErrorComponent
        if not isinstance(v, BreedingsitesListUpdatedAtErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreedingsitesListUpdatedAtErrorComponent`")
        else:
            match += 1
        # validate data type: BreedingsitesListCountryIdErrorComponent
        if not isinstance(v, BreedingsitesListCountryIdErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreedingsitesListCountryIdErrorComponent`")
        else:
            match += 1
        # validate data type: BreedingsitesListUserUuidErrorComponent
        if not isinstance(v, BreedingsitesListUserUuidErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreedingsitesListUserUuidErrorComponent`")
        else:
            match += 1
        # validate data type: BreedingsitesListOrderByErrorComponent
        if not isinstance(v, BreedingsitesListOrderByErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreedingsitesListOrderByErrorComponent`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in BreedingsitesListError with oneOf schemas: BreedingsitesListCountryIdErrorComponent, BreedingsitesListCreatedAtErrorComponent, BreedingsitesListOrderByErrorComponent, BreedingsitesListReceivedAtErrorComponent, BreedingsitesListShortIdErrorComponent, BreedingsitesListUpdatedAtErrorComponent, BreedingsitesListUserUuidErrorComponent. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in BreedingsitesListError with oneOf schemas: BreedingsitesListCountryIdErrorComponent, BreedingsitesListCreatedAtErrorComponent, BreedingsitesListOrderByErrorComponent, BreedingsitesListReceivedAtErrorComponent, BreedingsitesListShortIdErrorComponent, BreedingsitesListUpdatedAtErrorComponent, BreedingsitesListUserUuidErrorComponent. Details: " + ", ".join(error_messages))
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

        # deserialize data into BreedingsitesListShortIdErrorComponent
        try:
            instance.actual_instance = BreedingsitesListShortIdErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BreedingsitesListCreatedAtErrorComponent
        try:
            instance.actual_instance = BreedingsitesListCreatedAtErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BreedingsitesListReceivedAtErrorComponent
        try:
            instance.actual_instance = BreedingsitesListReceivedAtErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BreedingsitesListUpdatedAtErrorComponent
        try:
            instance.actual_instance = BreedingsitesListUpdatedAtErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BreedingsitesListCountryIdErrorComponent
        try:
            instance.actual_instance = BreedingsitesListCountryIdErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BreedingsitesListUserUuidErrorComponent
        try:
            instance.actual_instance = BreedingsitesListUserUuidErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BreedingsitesListOrderByErrorComponent
        try:
            instance.actual_instance = BreedingsitesListOrderByErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into BreedingsitesListError with oneOf schemas: BreedingsitesListCountryIdErrorComponent, BreedingsitesListCreatedAtErrorComponent, BreedingsitesListOrderByErrorComponent, BreedingsitesListReceivedAtErrorComponent, BreedingsitesListShortIdErrorComponent, BreedingsitesListUpdatedAtErrorComponent, BreedingsitesListUserUuidErrorComponent. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into BreedingsitesListError with oneOf schemas: BreedingsitesListCountryIdErrorComponent, BreedingsitesListCreatedAtErrorComponent, BreedingsitesListOrderByErrorComponent, BreedingsitesListReceivedAtErrorComponent, BreedingsitesListShortIdErrorComponent, BreedingsitesListUpdatedAtErrorComponent, BreedingsitesListUserUuidErrorComponent. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], BreedingsitesListCountryIdErrorComponent, BreedingsitesListCreatedAtErrorComponent, BreedingsitesListOrderByErrorComponent, BreedingsitesListReceivedAtErrorComponent, BreedingsitesListShortIdErrorComponent, BreedingsitesListUpdatedAtErrorComponent, BreedingsitesListUserUuidErrorComponent]]:
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


