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
from mosquito_alert.models.observations_prediction_create_is_executive_validation_error_component import ObservationsPredictionCreateIsExecutiveValidationErrorComponent
from mosquito_alert.models.observations_prediction_create_non_field_errors_error_component import ObservationsPredictionCreateNonFieldErrorsErrorComponent
from mosquito_alert.models.observations_prediction_create_ref_photo_uuid_error_component import ObservationsPredictionCreateRefPhotoUuidErrorComponent
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

OBSERVATIONSPREDICTIONCREATEERROR_ONE_OF_SCHEMAS = ["ObservationsPredictionCreateIsExecutiveValidationErrorComponent", "ObservationsPredictionCreateNonFieldErrorsErrorComponent", "ObservationsPredictionCreateRefPhotoUuidErrorComponent"]

class ObservationsPredictionCreateError(BaseModel):
    """
    ObservationsPredictionCreateError
    """
    # data type: ObservationsPredictionCreateNonFieldErrorsErrorComponent
    oneof_schema_1_validator: Optional[ObservationsPredictionCreateNonFieldErrorsErrorComponent] = None
    # data type: ObservationsPredictionCreateRefPhotoUuidErrorComponent
    oneof_schema_2_validator: Optional[ObservationsPredictionCreateRefPhotoUuidErrorComponent] = None
    # data type: ObservationsPredictionCreateIsExecutiveValidationErrorComponent
    oneof_schema_3_validator: Optional[ObservationsPredictionCreateIsExecutiveValidationErrorComponent] = None
    actual_instance: Optional[Union[ObservationsPredictionCreateIsExecutiveValidationErrorComponent, ObservationsPredictionCreateNonFieldErrorsErrorComponent, ObservationsPredictionCreateRefPhotoUuidErrorComponent]] = None
    one_of_schemas: Set[str] = { "ObservationsPredictionCreateIsExecutiveValidationErrorComponent", "ObservationsPredictionCreateNonFieldErrorsErrorComponent", "ObservationsPredictionCreateRefPhotoUuidErrorComponent" }

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
        instance = ObservationsPredictionCreateError.model_construct()
        error_messages = []
        match = 0
        # validate data type: ObservationsPredictionCreateNonFieldErrorsErrorComponent
        if not isinstance(v, ObservationsPredictionCreateNonFieldErrorsErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ObservationsPredictionCreateNonFieldErrorsErrorComponent`")
        else:
            match += 1
        # validate data type: ObservationsPredictionCreateRefPhotoUuidErrorComponent
        if not isinstance(v, ObservationsPredictionCreateRefPhotoUuidErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ObservationsPredictionCreateRefPhotoUuidErrorComponent`")
        else:
            match += 1
        # validate data type: ObservationsPredictionCreateIsExecutiveValidationErrorComponent
        if not isinstance(v, ObservationsPredictionCreateIsExecutiveValidationErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ObservationsPredictionCreateIsExecutiveValidationErrorComponent`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ObservationsPredictionCreateError with oneOf schemas: ObservationsPredictionCreateIsExecutiveValidationErrorComponent, ObservationsPredictionCreateNonFieldErrorsErrorComponent, ObservationsPredictionCreateRefPhotoUuidErrorComponent. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ObservationsPredictionCreateError with oneOf schemas: ObservationsPredictionCreateIsExecutiveValidationErrorComponent, ObservationsPredictionCreateNonFieldErrorsErrorComponent, ObservationsPredictionCreateRefPhotoUuidErrorComponent. Details: " + ", ".join(error_messages))
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

        # deserialize data into ObservationsPredictionCreateNonFieldErrorsErrorComponent
        try:
            instance.actual_instance = ObservationsPredictionCreateNonFieldErrorsErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ObservationsPredictionCreateRefPhotoUuidErrorComponent
        try:
            instance.actual_instance = ObservationsPredictionCreateRefPhotoUuidErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ObservationsPredictionCreateIsExecutiveValidationErrorComponent
        try:
            instance.actual_instance = ObservationsPredictionCreateIsExecutiveValidationErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ObservationsPredictionCreateError with oneOf schemas: ObservationsPredictionCreateIsExecutiveValidationErrorComponent, ObservationsPredictionCreateNonFieldErrorsErrorComponent, ObservationsPredictionCreateRefPhotoUuidErrorComponent. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ObservationsPredictionCreateError with oneOf schemas: ObservationsPredictionCreateIsExecutiveValidationErrorComponent, ObservationsPredictionCreateNonFieldErrorsErrorComponent, ObservationsPredictionCreateRefPhotoUuidErrorComponent. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], ObservationsPredictionCreateIsExecutiveValidationErrorComponent, ObservationsPredictionCreateNonFieldErrorsErrorComponent, ObservationsPredictionCreateRefPhotoUuidErrorComponent]]:
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


