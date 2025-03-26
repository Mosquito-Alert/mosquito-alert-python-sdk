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
from mosquito_alert.models.breedingsites_list_mine_created_at_error_component import BreedingsitesListMineCreatedAtErrorComponent
from mosquito_alert.models.breedingsites_list_mine_location_adm_nuts2_error_component import BreedingsitesListMineLocationAdmNuts2ErrorComponent
from mosquito_alert.models.breedingsites_list_mine_location_adm_nuts3_error_component import BreedingsitesListMineLocationAdmNuts3ErrorComponent
from mosquito_alert.models.breedingsites_list_mine_location_country_id_error_component import BreedingsitesListMineLocationCountryIdErrorComponent
from mosquito_alert.models.breedingsites_list_mine_order_by_error_component import BreedingsitesListMineOrderByErrorComponent
from mosquito_alert.models.breedingsites_list_mine_received_at_error_component import BreedingsitesListMineReceivedAtErrorComponent
from mosquito_alert.models.breedingsites_list_mine_short_id_error_component import BreedingsitesListMineShortIdErrorComponent
from mosquito_alert.models.breedingsites_list_mine_updated_at_error_component import BreedingsitesListMineUpdatedAtErrorComponent
from mosquito_alert.models.breedingsites_list_mine_user_uuid_error_component import BreedingsitesListMineUserUuidErrorComponent
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

BREEDINGSITESLISTMINEERROR_ONE_OF_SCHEMAS = ["BreedingsitesListMineCreatedAtErrorComponent", "BreedingsitesListMineLocationAdmNuts2ErrorComponent", "BreedingsitesListMineLocationAdmNuts3ErrorComponent", "BreedingsitesListMineLocationCountryIdErrorComponent", "BreedingsitesListMineOrderByErrorComponent", "BreedingsitesListMineReceivedAtErrorComponent", "BreedingsitesListMineShortIdErrorComponent", "BreedingsitesListMineUpdatedAtErrorComponent", "BreedingsitesListMineUserUuidErrorComponent"]

class BreedingsitesListMineError(BaseModel):
    """
    BreedingsitesListMineError
    """
    # data type: BreedingsitesListMineShortIdErrorComponent
    oneof_schema_1_validator: Optional[BreedingsitesListMineShortIdErrorComponent] = None
    # data type: BreedingsitesListMineCreatedAtErrorComponent
    oneof_schema_2_validator: Optional[BreedingsitesListMineCreatedAtErrorComponent] = None
    # data type: BreedingsitesListMineReceivedAtErrorComponent
    oneof_schema_3_validator: Optional[BreedingsitesListMineReceivedAtErrorComponent] = None
    # data type: BreedingsitesListMineUpdatedAtErrorComponent
    oneof_schema_4_validator: Optional[BreedingsitesListMineUpdatedAtErrorComponent] = None
    # data type: BreedingsitesListMineLocationCountryIdErrorComponent
    oneof_schema_5_validator: Optional[BreedingsitesListMineLocationCountryIdErrorComponent] = None
    # data type: BreedingsitesListMineLocationAdmNuts3ErrorComponent
    oneof_schema_6_validator: Optional[BreedingsitesListMineLocationAdmNuts3ErrorComponent] = None
    # data type: BreedingsitesListMineLocationAdmNuts2ErrorComponent
    oneof_schema_7_validator: Optional[BreedingsitesListMineLocationAdmNuts2ErrorComponent] = None
    # data type: BreedingsitesListMineUserUuidErrorComponent
    oneof_schema_8_validator: Optional[BreedingsitesListMineUserUuidErrorComponent] = None
    # data type: BreedingsitesListMineOrderByErrorComponent
    oneof_schema_9_validator: Optional[BreedingsitesListMineOrderByErrorComponent] = None
    actual_instance: Optional[Union[BreedingsitesListMineCreatedAtErrorComponent, BreedingsitesListMineLocationAdmNuts2ErrorComponent, BreedingsitesListMineLocationAdmNuts3ErrorComponent, BreedingsitesListMineLocationCountryIdErrorComponent, BreedingsitesListMineOrderByErrorComponent, BreedingsitesListMineReceivedAtErrorComponent, BreedingsitesListMineShortIdErrorComponent, BreedingsitesListMineUpdatedAtErrorComponent, BreedingsitesListMineUserUuidErrorComponent]] = None
    one_of_schemas: Set[str] = { "BreedingsitesListMineCreatedAtErrorComponent", "BreedingsitesListMineLocationAdmNuts2ErrorComponent", "BreedingsitesListMineLocationAdmNuts3ErrorComponent", "BreedingsitesListMineLocationCountryIdErrorComponent", "BreedingsitesListMineOrderByErrorComponent", "BreedingsitesListMineReceivedAtErrorComponent", "BreedingsitesListMineShortIdErrorComponent", "BreedingsitesListMineUpdatedAtErrorComponent", "BreedingsitesListMineUserUuidErrorComponent" }

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
        instance = BreedingsitesListMineError.model_construct()
        error_messages = []
        match = 0
        # validate data type: BreedingsitesListMineShortIdErrorComponent
        if not isinstance(v, BreedingsitesListMineShortIdErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreedingsitesListMineShortIdErrorComponent`")
        else:
            match += 1
        # validate data type: BreedingsitesListMineCreatedAtErrorComponent
        if not isinstance(v, BreedingsitesListMineCreatedAtErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreedingsitesListMineCreatedAtErrorComponent`")
        else:
            match += 1
        # validate data type: BreedingsitesListMineReceivedAtErrorComponent
        if not isinstance(v, BreedingsitesListMineReceivedAtErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreedingsitesListMineReceivedAtErrorComponent`")
        else:
            match += 1
        # validate data type: BreedingsitesListMineUpdatedAtErrorComponent
        if not isinstance(v, BreedingsitesListMineUpdatedAtErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreedingsitesListMineUpdatedAtErrorComponent`")
        else:
            match += 1
        # validate data type: BreedingsitesListMineLocationCountryIdErrorComponent
        if not isinstance(v, BreedingsitesListMineLocationCountryIdErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreedingsitesListMineLocationCountryIdErrorComponent`")
        else:
            match += 1
        # validate data type: BreedingsitesListMineLocationAdmNuts3ErrorComponent
        if not isinstance(v, BreedingsitesListMineLocationAdmNuts3ErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreedingsitesListMineLocationAdmNuts3ErrorComponent`")
        else:
            match += 1
        # validate data type: BreedingsitesListMineLocationAdmNuts2ErrorComponent
        if not isinstance(v, BreedingsitesListMineLocationAdmNuts2ErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreedingsitesListMineLocationAdmNuts2ErrorComponent`")
        else:
            match += 1
        # validate data type: BreedingsitesListMineUserUuidErrorComponent
        if not isinstance(v, BreedingsitesListMineUserUuidErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreedingsitesListMineUserUuidErrorComponent`")
        else:
            match += 1
        # validate data type: BreedingsitesListMineOrderByErrorComponent
        if not isinstance(v, BreedingsitesListMineOrderByErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreedingsitesListMineOrderByErrorComponent`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in BreedingsitesListMineError with oneOf schemas: BreedingsitesListMineCreatedAtErrorComponent, BreedingsitesListMineLocationAdmNuts2ErrorComponent, BreedingsitesListMineLocationAdmNuts3ErrorComponent, BreedingsitesListMineLocationCountryIdErrorComponent, BreedingsitesListMineOrderByErrorComponent, BreedingsitesListMineReceivedAtErrorComponent, BreedingsitesListMineShortIdErrorComponent, BreedingsitesListMineUpdatedAtErrorComponent, BreedingsitesListMineUserUuidErrorComponent. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in BreedingsitesListMineError with oneOf schemas: BreedingsitesListMineCreatedAtErrorComponent, BreedingsitesListMineLocationAdmNuts2ErrorComponent, BreedingsitesListMineLocationAdmNuts3ErrorComponent, BreedingsitesListMineLocationCountryIdErrorComponent, BreedingsitesListMineOrderByErrorComponent, BreedingsitesListMineReceivedAtErrorComponent, BreedingsitesListMineShortIdErrorComponent, BreedingsitesListMineUpdatedAtErrorComponent, BreedingsitesListMineUserUuidErrorComponent. Details: " + ", ".join(error_messages))
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

        # deserialize data into BreedingsitesListMineShortIdErrorComponent
        try:
            instance.actual_instance = BreedingsitesListMineShortIdErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BreedingsitesListMineCreatedAtErrorComponent
        try:
            instance.actual_instance = BreedingsitesListMineCreatedAtErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BreedingsitesListMineReceivedAtErrorComponent
        try:
            instance.actual_instance = BreedingsitesListMineReceivedAtErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BreedingsitesListMineUpdatedAtErrorComponent
        try:
            instance.actual_instance = BreedingsitesListMineUpdatedAtErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BreedingsitesListMineLocationCountryIdErrorComponent
        try:
            instance.actual_instance = BreedingsitesListMineLocationCountryIdErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BreedingsitesListMineLocationAdmNuts3ErrorComponent
        try:
            instance.actual_instance = BreedingsitesListMineLocationAdmNuts3ErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BreedingsitesListMineLocationAdmNuts2ErrorComponent
        try:
            instance.actual_instance = BreedingsitesListMineLocationAdmNuts2ErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BreedingsitesListMineUserUuidErrorComponent
        try:
            instance.actual_instance = BreedingsitesListMineUserUuidErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BreedingsitesListMineOrderByErrorComponent
        try:
            instance.actual_instance = BreedingsitesListMineOrderByErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into BreedingsitesListMineError with oneOf schemas: BreedingsitesListMineCreatedAtErrorComponent, BreedingsitesListMineLocationAdmNuts2ErrorComponent, BreedingsitesListMineLocationAdmNuts3ErrorComponent, BreedingsitesListMineLocationCountryIdErrorComponent, BreedingsitesListMineOrderByErrorComponent, BreedingsitesListMineReceivedAtErrorComponent, BreedingsitesListMineShortIdErrorComponent, BreedingsitesListMineUpdatedAtErrorComponent, BreedingsitesListMineUserUuidErrorComponent. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into BreedingsitesListMineError with oneOf schemas: BreedingsitesListMineCreatedAtErrorComponent, BreedingsitesListMineLocationAdmNuts2ErrorComponent, BreedingsitesListMineLocationAdmNuts3ErrorComponent, BreedingsitesListMineLocationCountryIdErrorComponent, BreedingsitesListMineOrderByErrorComponent, BreedingsitesListMineReceivedAtErrorComponent, BreedingsitesListMineShortIdErrorComponent, BreedingsitesListMineUpdatedAtErrorComponent, BreedingsitesListMineUserUuidErrorComponent. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], BreedingsitesListMineCreatedAtErrorComponent, BreedingsitesListMineLocationAdmNuts2ErrorComponent, BreedingsitesListMineLocationAdmNuts3ErrorComponent, BreedingsitesListMineLocationCountryIdErrorComponent, BreedingsitesListMineOrderByErrorComponent, BreedingsitesListMineReceivedAtErrorComponent, BreedingsitesListMineShortIdErrorComponent, BreedingsitesListMineUpdatedAtErrorComponent, BreedingsitesListMineUserUuidErrorComponent]]:
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


