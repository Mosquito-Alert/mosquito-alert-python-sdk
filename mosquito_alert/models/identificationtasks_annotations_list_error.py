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
from mosquito_alert.models.identificationtasks_annotations_list_classification_confidence_error_component import IdentificationtasksAnnotationsListClassificationConfidenceErrorComponent
from mosquito_alert.models.identificationtasks_annotations_list_classification_confidence_label_error_component import IdentificationtasksAnnotationsListClassificationConfidenceLabelErrorComponent
from mosquito_alert.models.identificationtasks_annotations_list_classification_taxon_ids_error_component import IdentificationtasksAnnotationsListClassificationTaxonIdsErrorComponent
from mosquito_alert.models.identificationtasks_annotations_list_created_at_error_component import IdentificationtasksAnnotationsListCreatedAtErrorComponent
from mosquito_alert.models.identificationtasks_annotations_list_order_by_error_component import IdentificationtasksAnnotationsListOrderByErrorComponent
from mosquito_alert.models.identificationtasks_annotations_list_type_error_component import IdentificationtasksAnnotationsListTypeErrorComponent
from mosquito_alert.models.identificationtasks_annotations_list_updated_at_error_component import IdentificationtasksAnnotationsListUpdatedAtErrorComponent
from mosquito_alert.models.identificationtasks_annotations_list_user_ids_error_component import IdentificationtasksAnnotationsListUserIdsErrorComponent
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

IDENTIFICATIONTASKSANNOTATIONSLISTERROR_ONE_OF_SCHEMAS = ["IdentificationtasksAnnotationsListClassificationConfidenceErrorComponent", "IdentificationtasksAnnotationsListClassificationConfidenceLabelErrorComponent", "IdentificationtasksAnnotationsListClassificationTaxonIdsErrorComponent", "IdentificationtasksAnnotationsListCreatedAtErrorComponent", "IdentificationtasksAnnotationsListOrderByErrorComponent", "IdentificationtasksAnnotationsListTypeErrorComponent", "IdentificationtasksAnnotationsListUpdatedAtErrorComponent", "IdentificationtasksAnnotationsListUserIdsErrorComponent"]

class IdentificationtasksAnnotationsListError(BaseModel):
    """
    IdentificationtasksAnnotationsListError
    """
    # data type: IdentificationtasksAnnotationsListUserIdsErrorComponent
    oneof_schema_1_validator: Optional[IdentificationtasksAnnotationsListUserIdsErrorComponent] = None
    # data type: IdentificationtasksAnnotationsListClassificationTaxonIdsErrorComponent
    oneof_schema_2_validator: Optional[IdentificationtasksAnnotationsListClassificationTaxonIdsErrorComponent] = None
    # data type: IdentificationtasksAnnotationsListClassificationConfidenceErrorComponent
    oneof_schema_3_validator: Optional[IdentificationtasksAnnotationsListClassificationConfidenceErrorComponent] = None
    # data type: IdentificationtasksAnnotationsListClassificationConfidenceLabelErrorComponent
    oneof_schema_4_validator: Optional[IdentificationtasksAnnotationsListClassificationConfidenceLabelErrorComponent] = None
    # data type: IdentificationtasksAnnotationsListCreatedAtErrorComponent
    oneof_schema_5_validator: Optional[IdentificationtasksAnnotationsListCreatedAtErrorComponent] = None
    # data type: IdentificationtasksAnnotationsListUpdatedAtErrorComponent
    oneof_schema_6_validator: Optional[IdentificationtasksAnnotationsListUpdatedAtErrorComponent] = None
    # data type: IdentificationtasksAnnotationsListTypeErrorComponent
    oneof_schema_7_validator: Optional[IdentificationtasksAnnotationsListTypeErrorComponent] = None
    # data type: IdentificationtasksAnnotationsListOrderByErrorComponent
    oneof_schema_8_validator: Optional[IdentificationtasksAnnotationsListOrderByErrorComponent] = None
    actual_instance: Optional[Union[IdentificationtasksAnnotationsListClassificationConfidenceErrorComponent, IdentificationtasksAnnotationsListClassificationConfidenceLabelErrorComponent, IdentificationtasksAnnotationsListClassificationTaxonIdsErrorComponent, IdentificationtasksAnnotationsListCreatedAtErrorComponent, IdentificationtasksAnnotationsListOrderByErrorComponent, IdentificationtasksAnnotationsListTypeErrorComponent, IdentificationtasksAnnotationsListUpdatedAtErrorComponent, IdentificationtasksAnnotationsListUserIdsErrorComponent]] = None
    one_of_schemas: Set[str] = { "IdentificationtasksAnnotationsListClassificationConfidenceErrorComponent", "IdentificationtasksAnnotationsListClassificationConfidenceLabelErrorComponent", "IdentificationtasksAnnotationsListClassificationTaxonIdsErrorComponent", "IdentificationtasksAnnotationsListCreatedAtErrorComponent", "IdentificationtasksAnnotationsListOrderByErrorComponent", "IdentificationtasksAnnotationsListTypeErrorComponent", "IdentificationtasksAnnotationsListUpdatedAtErrorComponent", "IdentificationtasksAnnotationsListUserIdsErrorComponent" }

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
        instance = IdentificationtasksAnnotationsListError.model_construct()
        error_messages = []
        match = 0
        # validate data type: IdentificationtasksAnnotationsListUserIdsErrorComponent
        if not isinstance(v, IdentificationtasksAnnotationsListUserIdsErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IdentificationtasksAnnotationsListUserIdsErrorComponent`")
        else:
            match += 1
        # validate data type: IdentificationtasksAnnotationsListClassificationTaxonIdsErrorComponent
        if not isinstance(v, IdentificationtasksAnnotationsListClassificationTaxonIdsErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IdentificationtasksAnnotationsListClassificationTaxonIdsErrorComponent`")
        else:
            match += 1
        # validate data type: IdentificationtasksAnnotationsListClassificationConfidenceErrorComponent
        if not isinstance(v, IdentificationtasksAnnotationsListClassificationConfidenceErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IdentificationtasksAnnotationsListClassificationConfidenceErrorComponent`")
        else:
            match += 1
        # validate data type: IdentificationtasksAnnotationsListClassificationConfidenceLabelErrorComponent
        if not isinstance(v, IdentificationtasksAnnotationsListClassificationConfidenceLabelErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IdentificationtasksAnnotationsListClassificationConfidenceLabelErrorComponent`")
        else:
            match += 1
        # validate data type: IdentificationtasksAnnotationsListCreatedAtErrorComponent
        if not isinstance(v, IdentificationtasksAnnotationsListCreatedAtErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IdentificationtasksAnnotationsListCreatedAtErrorComponent`")
        else:
            match += 1
        # validate data type: IdentificationtasksAnnotationsListUpdatedAtErrorComponent
        if not isinstance(v, IdentificationtasksAnnotationsListUpdatedAtErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IdentificationtasksAnnotationsListUpdatedAtErrorComponent`")
        else:
            match += 1
        # validate data type: IdentificationtasksAnnotationsListTypeErrorComponent
        if not isinstance(v, IdentificationtasksAnnotationsListTypeErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IdentificationtasksAnnotationsListTypeErrorComponent`")
        else:
            match += 1
        # validate data type: IdentificationtasksAnnotationsListOrderByErrorComponent
        if not isinstance(v, IdentificationtasksAnnotationsListOrderByErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IdentificationtasksAnnotationsListOrderByErrorComponent`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in IdentificationtasksAnnotationsListError with oneOf schemas: IdentificationtasksAnnotationsListClassificationConfidenceErrorComponent, IdentificationtasksAnnotationsListClassificationConfidenceLabelErrorComponent, IdentificationtasksAnnotationsListClassificationTaxonIdsErrorComponent, IdentificationtasksAnnotationsListCreatedAtErrorComponent, IdentificationtasksAnnotationsListOrderByErrorComponent, IdentificationtasksAnnotationsListTypeErrorComponent, IdentificationtasksAnnotationsListUpdatedAtErrorComponent, IdentificationtasksAnnotationsListUserIdsErrorComponent. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in IdentificationtasksAnnotationsListError with oneOf schemas: IdentificationtasksAnnotationsListClassificationConfidenceErrorComponent, IdentificationtasksAnnotationsListClassificationConfidenceLabelErrorComponent, IdentificationtasksAnnotationsListClassificationTaxonIdsErrorComponent, IdentificationtasksAnnotationsListCreatedAtErrorComponent, IdentificationtasksAnnotationsListOrderByErrorComponent, IdentificationtasksAnnotationsListTypeErrorComponent, IdentificationtasksAnnotationsListUpdatedAtErrorComponent, IdentificationtasksAnnotationsListUserIdsErrorComponent. Details: " + ", ".join(error_messages))
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

        # deserialize data into IdentificationtasksAnnotationsListUserIdsErrorComponent
        try:
            instance.actual_instance = IdentificationtasksAnnotationsListUserIdsErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into IdentificationtasksAnnotationsListClassificationTaxonIdsErrorComponent
        try:
            instance.actual_instance = IdentificationtasksAnnotationsListClassificationTaxonIdsErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into IdentificationtasksAnnotationsListClassificationConfidenceErrorComponent
        try:
            instance.actual_instance = IdentificationtasksAnnotationsListClassificationConfidenceErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into IdentificationtasksAnnotationsListClassificationConfidenceLabelErrorComponent
        try:
            instance.actual_instance = IdentificationtasksAnnotationsListClassificationConfidenceLabelErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into IdentificationtasksAnnotationsListCreatedAtErrorComponent
        try:
            instance.actual_instance = IdentificationtasksAnnotationsListCreatedAtErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into IdentificationtasksAnnotationsListUpdatedAtErrorComponent
        try:
            instance.actual_instance = IdentificationtasksAnnotationsListUpdatedAtErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into IdentificationtasksAnnotationsListTypeErrorComponent
        try:
            instance.actual_instance = IdentificationtasksAnnotationsListTypeErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into IdentificationtasksAnnotationsListOrderByErrorComponent
        try:
            instance.actual_instance = IdentificationtasksAnnotationsListOrderByErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into IdentificationtasksAnnotationsListError with oneOf schemas: IdentificationtasksAnnotationsListClassificationConfidenceErrorComponent, IdentificationtasksAnnotationsListClassificationConfidenceLabelErrorComponent, IdentificationtasksAnnotationsListClassificationTaxonIdsErrorComponent, IdentificationtasksAnnotationsListCreatedAtErrorComponent, IdentificationtasksAnnotationsListOrderByErrorComponent, IdentificationtasksAnnotationsListTypeErrorComponent, IdentificationtasksAnnotationsListUpdatedAtErrorComponent, IdentificationtasksAnnotationsListUserIdsErrorComponent. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into IdentificationtasksAnnotationsListError with oneOf schemas: IdentificationtasksAnnotationsListClassificationConfidenceErrorComponent, IdentificationtasksAnnotationsListClassificationConfidenceLabelErrorComponent, IdentificationtasksAnnotationsListClassificationTaxonIdsErrorComponent, IdentificationtasksAnnotationsListCreatedAtErrorComponent, IdentificationtasksAnnotationsListOrderByErrorComponent, IdentificationtasksAnnotationsListTypeErrorComponent, IdentificationtasksAnnotationsListUpdatedAtErrorComponent, IdentificationtasksAnnotationsListUserIdsErrorComponent. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], IdentificationtasksAnnotationsListClassificationConfidenceErrorComponent, IdentificationtasksAnnotationsListClassificationConfidenceLabelErrorComponent, IdentificationtasksAnnotationsListClassificationTaxonIdsErrorComponent, IdentificationtasksAnnotationsListCreatedAtErrorComponent, IdentificationtasksAnnotationsListOrderByErrorComponent, IdentificationtasksAnnotationsListTypeErrorComponent, IdentificationtasksAnnotationsListUpdatedAtErrorComponent, IdentificationtasksAnnotationsListUserIdsErrorComponent]]:
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


