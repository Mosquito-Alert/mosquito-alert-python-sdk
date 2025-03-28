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
from mosquito_alert.models.identificationtasks_list_assignees_error_component import IdentificationtasksListAssigneesErrorComponent
from mosquito_alert.models.identificationtasks_list_created_at_error_component import IdentificationtasksListCreatedAtErrorComponent
from mosquito_alert.models.identificationtasks_list_num_annotations_error_component import IdentificationtasksListNumAnnotationsErrorComponent
from mosquito_alert.models.identificationtasks_list_num_assignations_error_component import IdentificationtasksListNumAssignationsErrorComponent
from mosquito_alert.models.identificationtasks_list_order_by_error_component import IdentificationtasksListOrderByErrorComponent
from mosquito_alert.models.identificationtasks_list_revision_type_error_component import IdentificationtasksListRevisionTypeErrorComponent
from mosquito_alert.models.identificationtasks_list_status_error_component import IdentificationtasksListStatusErrorComponent
from mosquito_alert.models.identificationtasks_list_updated_at_error_component import IdentificationtasksListUpdatedAtErrorComponent
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

IDENTIFICATIONTASKSLISTERROR_ONE_OF_SCHEMAS = ["IdentificationtasksListAssigneesErrorComponent", "IdentificationtasksListCreatedAtErrorComponent", "IdentificationtasksListNumAnnotationsErrorComponent", "IdentificationtasksListNumAssignationsErrorComponent", "IdentificationtasksListOrderByErrorComponent", "IdentificationtasksListRevisionTypeErrorComponent", "IdentificationtasksListStatusErrorComponent", "IdentificationtasksListUpdatedAtErrorComponent"]

class IdentificationtasksListError(BaseModel):
    """
    IdentificationtasksListError
    """
    # data type: IdentificationtasksListAssigneesErrorComponent
    oneof_schema_1_validator: Optional[IdentificationtasksListAssigneesErrorComponent] = None
    # data type: IdentificationtasksListStatusErrorComponent
    oneof_schema_2_validator: Optional[IdentificationtasksListStatusErrorComponent] = None
    # data type: IdentificationtasksListRevisionTypeErrorComponent
    oneof_schema_3_validator: Optional[IdentificationtasksListRevisionTypeErrorComponent] = None
    # data type: IdentificationtasksListNumAssignationsErrorComponent
    oneof_schema_4_validator: Optional[IdentificationtasksListNumAssignationsErrorComponent] = None
    # data type: IdentificationtasksListNumAnnotationsErrorComponent
    oneof_schema_5_validator: Optional[IdentificationtasksListNumAnnotationsErrorComponent] = None
    # data type: IdentificationtasksListCreatedAtErrorComponent
    oneof_schema_6_validator: Optional[IdentificationtasksListCreatedAtErrorComponent] = None
    # data type: IdentificationtasksListUpdatedAtErrorComponent
    oneof_schema_7_validator: Optional[IdentificationtasksListUpdatedAtErrorComponent] = None
    # data type: IdentificationtasksListOrderByErrorComponent
    oneof_schema_8_validator: Optional[IdentificationtasksListOrderByErrorComponent] = None
    actual_instance: Optional[Union[IdentificationtasksListAssigneesErrorComponent, IdentificationtasksListCreatedAtErrorComponent, IdentificationtasksListNumAnnotationsErrorComponent, IdentificationtasksListNumAssignationsErrorComponent, IdentificationtasksListOrderByErrorComponent, IdentificationtasksListRevisionTypeErrorComponent, IdentificationtasksListStatusErrorComponent, IdentificationtasksListUpdatedAtErrorComponent]] = None
    one_of_schemas: Set[str] = { "IdentificationtasksListAssigneesErrorComponent", "IdentificationtasksListCreatedAtErrorComponent", "IdentificationtasksListNumAnnotationsErrorComponent", "IdentificationtasksListNumAssignationsErrorComponent", "IdentificationtasksListOrderByErrorComponent", "IdentificationtasksListRevisionTypeErrorComponent", "IdentificationtasksListStatusErrorComponent", "IdentificationtasksListUpdatedAtErrorComponent" }

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
        instance = IdentificationtasksListError.model_construct()
        error_messages = []
        match = 0
        # validate data type: IdentificationtasksListAssigneesErrorComponent
        if not isinstance(v, IdentificationtasksListAssigneesErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IdentificationtasksListAssigneesErrorComponent`")
        else:
            match += 1
        # validate data type: IdentificationtasksListStatusErrorComponent
        if not isinstance(v, IdentificationtasksListStatusErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IdentificationtasksListStatusErrorComponent`")
        else:
            match += 1
        # validate data type: IdentificationtasksListRevisionTypeErrorComponent
        if not isinstance(v, IdentificationtasksListRevisionTypeErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IdentificationtasksListRevisionTypeErrorComponent`")
        else:
            match += 1
        # validate data type: IdentificationtasksListNumAssignationsErrorComponent
        if not isinstance(v, IdentificationtasksListNumAssignationsErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IdentificationtasksListNumAssignationsErrorComponent`")
        else:
            match += 1
        # validate data type: IdentificationtasksListNumAnnotationsErrorComponent
        if not isinstance(v, IdentificationtasksListNumAnnotationsErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IdentificationtasksListNumAnnotationsErrorComponent`")
        else:
            match += 1
        # validate data type: IdentificationtasksListCreatedAtErrorComponent
        if not isinstance(v, IdentificationtasksListCreatedAtErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IdentificationtasksListCreatedAtErrorComponent`")
        else:
            match += 1
        # validate data type: IdentificationtasksListUpdatedAtErrorComponent
        if not isinstance(v, IdentificationtasksListUpdatedAtErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IdentificationtasksListUpdatedAtErrorComponent`")
        else:
            match += 1
        # validate data type: IdentificationtasksListOrderByErrorComponent
        if not isinstance(v, IdentificationtasksListOrderByErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IdentificationtasksListOrderByErrorComponent`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in IdentificationtasksListError with oneOf schemas: IdentificationtasksListAssigneesErrorComponent, IdentificationtasksListCreatedAtErrorComponent, IdentificationtasksListNumAnnotationsErrorComponent, IdentificationtasksListNumAssignationsErrorComponent, IdentificationtasksListOrderByErrorComponent, IdentificationtasksListRevisionTypeErrorComponent, IdentificationtasksListStatusErrorComponent, IdentificationtasksListUpdatedAtErrorComponent. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in IdentificationtasksListError with oneOf schemas: IdentificationtasksListAssigneesErrorComponent, IdentificationtasksListCreatedAtErrorComponent, IdentificationtasksListNumAnnotationsErrorComponent, IdentificationtasksListNumAssignationsErrorComponent, IdentificationtasksListOrderByErrorComponent, IdentificationtasksListRevisionTypeErrorComponent, IdentificationtasksListStatusErrorComponent, IdentificationtasksListUpdatedAtErrorComponent. Details: " + ", ".join(error_messages))
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

        # deserialize data into IdentificationtasksListAssigneesErrorComponent
        try:
            instance.actual_instance = IdentificationtasksListAssigneesErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into IdentificationtasksListStatusErrorComponent
        try:
            instance.actual_instance = IdentificationtasksListStatusErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into IdentificationtasksListRevisionTypeErrorComponent
        try:
            instance.actual_instance = IdentificationtasksListRevisionTypeErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into IdentificationtasksListNumAssignationsErrorComponent
        try:
            instance.actual_instance = IdentificationtasksListNumAssignationsErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into IdentificationtasksListNumAnnotationsErrorComponent
        try:
            instance.actual_instance = IdentificationtasksListNumAnnotationsErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into IdentificationtasksListCreatedAtErrorComponent
        try:
            instance.actual_instance = IdentificationtasksListCreatedAtErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into IdentificationtasksListUpdatedAtErrorComponent
        try:
            instance.actual_instance = IdentificationtasksListUpdatedAtErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into IdentificationtasksListOrderByErrorComponent
        try:
            instance.actual_instance = IdentificationtasksListOrderByErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into IdentificationtasksListError with oneOf schemas: IdentificationtasksListAssigneesErrorComponent, IdentificationtasksListCreatedAtErrorComponent, IdentificationtasksListNumAnnotationsErrorComponent, IdentificationtasksListNumAssignationsErrorComponent, IdentificationtasksListOrderByErrorComponent, IdentificationtasksListRevisionTypeErrorComponent, IdentificationtasksListStatusErrorComponent, IdentificationtasksListUpdatedAtErrorComponent. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into IdentificationtasksListError with oneOf schemas: IdentificationtasksListAssigneesErrorComponent, IdentificationtasksListCreatedAtErrorComponent, IdentificationtasksListNumAnnotationsErrorComponent, IdentificationtasksListNumAssignationsErrorComponent, IdentificationtasksListOrderByErrorComponent, IdentificationtasksListRevisionTypeErrorComponent, IdentificationtasksListStatusErrorComponent, IdentificationtasksListUpdatedAtErrorComponent. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], IdentificationtasksListAssigneesErrorComponent, IdentificationtasksListCreatedAtErrorComponent, IdentificationtasksListNumAnnotationsErrorComponent, IdentificationtasksListNumAssignationsErrorComponent, IdentificationtasksListOrderByErrorComponent, IdentificationtasksListRevisionTypeErrorComponent, IdentificationtasksListStatusErrorComponent, IdentificationtasksListUpdatedAtErrorComponent]]:
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


