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
from mosquito_alert.models.breedingsites_create_created_at_error_component import BreedingsitesCreateCreatedAtErrorComponent
from mosquito_alert.models.breedingsites_create_has_larvae_error_component import BreedingsitesCreateHasLarvaeErrorComponent
from mosquito_alert.models.breedingsites_create_has_near_mosquitoes_error_component import BreedingsitesCreateHasNearMosquitoesErrorComponent
from mosquito_alert.models.breedingsites_create_has_water_error_component import BreedingsitesCreateHasWaterErrorComponent
from mosquito_alert.models.breedingsites_create_in_public_area_error_component import BreedingsitesCreateInPublicAreaErrorComponent
from mosquito_alert.models.breedingsites_create_location_non_field_errors_error_component import BreedingsitesCreateLocationNonFieldErrorsErrorComponent
from mosquito_alert.models.breedingsites_create_location_point_error_component import BreedingsitesCreateLocationPointErrorComponent
from mosquito_alert.models.breedingsites_create_location_source_error_component import BreedingsitesCreateLocationSourceErrorComponent
from mosquito_alert.models.breedingsites_create_non_field_errors_error_component import BreedingsitesCreateNonFieldErrorsErrorComponent
from mosquito_alert.models.breedingsites_create_note_error_component import BreedingsitesCreateNoteErrorComponent
from mosquito_alert.models.breedingsites_create_photos_index_file_error_component import BreedingsitesCreatePhotosINDEXFileErrorComponent
from mosquito_alert.models.breedingsites_create_photos_index_non_field_errors_error_component import BreedingsitesCreatePhotosINDEXNonFieldErrorsErrorComponent
from mosquito_alert.models.breedingsites_create_photos_non_field_errors_error_component import BreedingsitesCreatePhotosNonFieldErrorsErrorComponent
from mosquito_alert.models.breedingsites_create_sent_at_error_component import BreedingsitesCreateSentAtErrorComponent
from mosquito_alert.models.breedingsites_create_site_type_error_component import BreedingsitesCreateSiteTypeErrorComponent
from mosquito_alert.models.breedingsites_create_tags_error_component import BreedingsitesCreateTagsErrorComponent
from mosquito_alert.models.breedingsites_create_tags_index_error_component import BreedingsitesCreateTagsINDEXErrorComponent
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

BREEDINGSITESCREATEERROR_ONE_OF_SCHEMAS = ["BreedingsitesCreateCreatedAtErrorComponent", "BreedingsitesCreateHasLarvaeErrorComponent", "BreedingsitesCreateHasNearMosquitoesErrorComponent", "BreedingsitesCreateHasWaterErrorComponent", "BreedingsitesCreateInPublicAreaErrorComponent", "BreedingsitesCreateLocationNonFieldErrorsErrorComponent", "BreedingsitesCreateLocationPointErrorComponent", "BreedingsitesCreateLocationSourceErrorComponent", "BreedingsitesCreateNonFieldErrorsErrorComponent", "BreedingsitesCreateNoteErrorComponent", "BreedingsitesCreatePhotosINDEXFileErrorComponent", "BreedingsitesCreatePhotosINDEXNonFieldErrorsErrorComponent", "BreedingsitesCreatePhotosNonFieldErrorsErrorComponent", "BreedingsitesCreateSentAtErrorComponent", "BreedingsitesCreateSiteTypeErrorComponent", "BreedingsitesCreateTagsErrorComponent", "BreedingsitesCreateTagsINDEXErrorComponent"]

class BreedingsitesCreateError(BaseModel):
    """
    BreedingsitesCreateError
    """
    # data type: BreedingsitesCreateNonFieldErrorsErrorComponent
    oneof_schema_1_validator: Optional[BreedingsitesCreateNonFieldErrorsErrorComponent] = None
    # data type: BreedingsitesCreateCreatedAtErrorComponent
    oneof_schema_2_validator: Optional[BreedingsitesCreateCreatedAtErrorComponent] = None
    # data type: BreedingsitesCreateSentAtErrorComponent
    oneof_schema_3_validator: Optional[BreedingsitesCreateSentAtErrorComponent] = None
    # data type: BreedingsitesCreateLocationNonFieldErrorsErrorComponent
    oneof_schema_4_validator: Optional[BreedingsitesCreateLocationNonFieldErrorsErrorComponent] = None
    # data type: BreedingsitesCreateLocationSourceErrorComponent
    oneof_schema_5_validator: Optional[BreedingsitesCreateLocationSourceErrorComponent] = None
    # data type: BreedingsitesCreateLocationPointErrorComponent
    oneof_schema_6_validator: Optional[BreedingsitesCreateLocationPointErrorComponent] = None
    # data type: BreedingsitesCreateNoteErrorComponent
    oneof_schema_7_validator: Optional[BreedingsitesCreateNoteErrorComponent] = None
    # data type: BreedingsitesCreateTagsErrorComponent
    oneof_schema_8_validator: Optional[BreedingsitesCreateTagsErrorComponent] = None
    # data type: BreedingsitesCreateTagsINDEXErrorComponent
    oneof_schema_9_validator: Optional[BreedingsitesCreateTagsINDEXErrorComponent] = None
    # data type: BreedingsitesCreatePhotosNonFieldErrorsErrorComponent
    oneof_schema_10_validator: Optional[BreedingsitesCreatePhotosNonFieldErrorsErrorComponent] = None
    # data type: BreedingsitesCreatePhotosINDEXNonFieldErrorsErrorComponent
    oneof_schema_11_validator: Optional[BreedingsitesCreatePhotosINDEXNonFieldErrorsErrorComponent] = None
    # data type: BreedingsitesCreatePhotosINDEXFileErrorComponent
    oneof_schema_12_validator: Optional[BreedingsitesCreatePhotosINDEXFileErrorComponent] = None
    # data type: BreedingsitesCreateSiteTypeErrorComponent
    oneof_schema_13_validator: Optional[BreedingsitesCreateSiteTypeErrorComponent] = None
    # data type: BreedingsitesCreateHasWaterErrorComponent
    oneof_schema_14_validator: Optional[BreedingsitesCreateHasWaterErrorComponent] = None
    # data type: BreedingsitesCreateInPublicAreaErrorComponent
    oneof_schema_15_validator: Optional[BreedingsitesCreateInPublicAreaErrorComponent] = None
    # data type: BreedingsitesCreateHasNearMosquitoesErrorComponent
    oneof_schema_16_validator: Optional[BreedingsitesCreateHasNearMosquitoesErrorComponent] = None
    # data type: BreedingsitesCreateHasLarvaeErrorComponent
    oneof_schema_17_validator: Optional[BreedingsitesCreateHasLarvaeErrorComponent] = None
    actual_instance: Optional[Union[BreedingsitesCreateCreatedAtErrorComponent, BreedingsitesCreateHasLarvaeErrorComponent, BreedingsitesCreateHasNearMosquitoesErrorComponent, BreedingsitesCreateHasWaterErrorComponent, BreedingsitesCreateInPublicAreaErrorComponent, BreedingsitesCreateLocationNonFieldErrorsErrorComponent, BreedingsitesCreateLocationPointErrorComponent, BreedingsitesCreateLocationSourceErrorComponent, BreedingsitesCreateNonFieldErrorsErrorComponent, BreedingsitesCreateNoteErrorComponent, BreedingsitesCreatePhotosINDEXFileErrorComponent, BreedingsitesCreatePhotosINDEXNonFieldErrorsErrorComponent, BreedingsitesCreatePhotosNonFieldErrorsErrorComponent, BreedingsitesCreateSentAtErrorComponent, BreedingsitesCreateSiteTypeErrorComponent, BreedingsitesCreateTagsErrorComponent, BreedingsitesCreateTagsINDEXErrorComponent]] = None
    one_of_schemas: Set[str] = { "BreedingsitesCreateCreatedAtErrorComponent", "BreedingsitesCreateHasLarvaeErrorComponent", "BreedingsitesCreateHasNearMosquitoesErrorComponent", "BreedingsitesCreateHasWaterErrorComponent", "BreedingsitesCreateInPublicAreaErrorComponent", "BreedingsitesCreateLocationNonFieldErrorsErrorComponent", "BreedingsitesCreateLocationPointErrorComponent", "BreedingsitesCreateLocationSourceErrorComponent", "BreedingsitesCreateNonFieldErrorsErrorComponent", "BreedingsitesCreateNoteErrorComponent", "BreedingsitesCreatePhotosINDEXFileErrorComponent", "BreedingsitesCreatePhotosINDEXNonFieldErrorsErrorComponent", "BreedingsitesCreatePhotosNonFieldErrorsErrorComponent", "BreedingsitesCreateSentAtErrorComponent", "BreedingsitesCreateSiteTypeErrorComponent", "BreedingsitesCreateTagsErrorComponent", "BreedingsitesCreateTagsINDEXErrorComponent" }

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
        instance = BreedingsitesCreateError.model_construct()
        error_messages = []
        match = 0
        # validate data type: BreedingsitesCreateNonFieldErrorsErrorComponent
        if not isinstance(v, BreedingsitesCreateNonFieldErrorsErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreedingsitesCreateNonFieldErrorsErrorComponent`")
        else:
            match += 1
        # validate data type: BreedingsitesCreateCreatedAtErrorComponent
        if not isinstance(v, BreedingsitesCreateCreatedAtErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreedingsitesCreateCreatedAtErrorComponent`")
        else:
            match += 1
        # validate data type: BreedingsitesCreateSentAtErrorComponent
        if not isinstance(v, BreedingsitesCreateSentAtErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreedingsitesCreateSentAtErrorComponent`")
        else:
            match += 1
        # validate data type: BreedingsitesCreateLocationNonFieldErrorsErrorComponent
        if not isinstance(v, BreedingsitesCreateLocationNonFieldErrorsErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreedingsitesCreateLocationNonFieldErrorsErrorComponent`")
        else:
            match += 1
        # validate data type: BreedingsitesCreateLocationSourceErrorComponent
        if not isinstance(v, BreedingsitesCreateLocationSourceErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreedingsitesCreateLocationSourceErrorComponent`")
        else:
            match += 1
        # validate data type: BreedingsitesCreateLocationPointErrorComponent
        if not isinstance(v, BreedingsitesCreateLocationPointErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreedingsitesCreateLocationPointErrorComponent`")
        else:
            match += 1
        # validate data type: BreedingsitesCreateNoteErrorComponent
        if not isinstance(v, BreedingsitesCreateNoteErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreedingsitesCreateNoteErrorComponent`")
        else:
            match += 1
        # validate data type: BreedingsitesCreateTagsErrorComponent
        if not isinstance(v, BreedingsitesCreateTagsErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreedingsitesCreateTagsErrorComponent`")
        else:
            match += 1
        # validate data type: BreedingsitesCreateTagsINDEXErrorComponent
        if not isinstance(v, BreedingsitesCreateTagsINDEXErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreedingsitesCreateTagsINDEXErrorComponent`")
        else:
            match += 1
        # validate data type: BreedingsitesCreatePhotosNonFieldErrorsErrorComponent
        if not isinstance(v, BreedingsitesCreatePhotosNonFieldErrorsErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreedingsitesCreatePhotosNonFieldErrorsErrorComponent`")
        else:
            match += 1
        # validate data type: BreedingsitesCreatePhotosINDEXNonFieldErrorsErrorComponent
        if not isinstance(v, BreedingsitesCreatePhotosINDEXNonFieldErrorsErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreedingsitesCreatePhotosINDEXNonFieldErrorsErrorComponent`")
        else:
            match += 1
        # validate data type: BreedingsitesCreatePhotosINDEXFileErrorComponent
        if not isinstance(v, BreedingsitesCreatePhotosINDEXFileErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreedingsitesCreatePhotosINDEXFileErrorComponent`")
        else:
            match += 1
        # validate data type: BreedingsitesCreateSiteTypeErrorComponent
        if not isinstance(v, BreedingsitesCreateSiteTypeErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreedingsitesCreateSiteTypeErrorComponent`")
        else:
            match += 1
        # validate data type: BreedingsitesCreateHasWaterErrorComponent
        if not isinstance(v, BreedingsitesCreateHasWaterErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreedingsitesCreateHasWaterErrorComponent`")
        else:
            match += 1
        # validate data type: BreedingsitesCreateInPublicAreaErrorComponent
        if not isinstance(v, BreedingsitesCreateInPublicAreaErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreedingsitesCreateInPublicAreaErrorComponent`")
        else:
            match += 1
        # validate data type: BreedingsitesCreateHasNearMosquitoesErrorComponent
        if not isinstance(v, BreedingsitesCreateHasNearMosquitoesErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreedingsitesCreateHasNearMosquitoesErrorComponent`")
        else:
            match += 1
        # validate data type: BreedingsitesCreateHasLarvaeErrorComponent
        if not isinstance(v, BreedingsitesCreateHasLarvaeErrorComponent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreedingsitesCreateHasLarvaeErrorComponent`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in BreedingsitesCreateError with oneOf schemas: BreedingsitesCreateCreatedAtErrorComponent, BreedingsitesCreateHasLarvaeErrorComponent, BreedingsitesCreateHasNearMosquitoesErrorComponent, BreedingsitesCreateHasWaterErrorComponent, BreedingsitesCreateInPublicAreaErrorComponent, BreedingsitesCreateLocationNonFieldErrorsErrorComponent, BreedingsitesCreateLocationPointErrorComponent, BreedingsitesCreateLocationSourceErrorComponent, BreedingsitesCreateNonFieldErrorsErrorComponent, BreedingsitesCreateNoteErrorComponent, BreedingsitesCreatePhotosINDEXFileErrorComponent, BreedingsitesCreatePhotosINDEXNonFieldErrorsErrorComponent, BreedingsitesCreatePhotosNonFieldErrorsErrorComponent, BreedingsitesCreateSentAtErrorComponent, BreedingsitesCreateSiteTypeErrorComponent, BreedingsitesCreateTagsErrorComponent, BreedingsitesCreateTagsINDEXErrorComponent. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in BreedingsitesCreateError with oneOf schemas: BreedingsitesCreateCreatedAtErrorComponent, BreedingsitesCreateHasLarvaeErrorComponent, BreedingsitesCreateHasNearMosquitoesErrorComponent, BreedingsitesCreateHasWaterErrorComponent, BreedingsitesCreateInPublicAreaErrorComponent, BreedingsitesCreateLocationNonFieldErrorsErrorComponent, BreedingsitesCreateLocationPointErrorComponent, BreedingsitesCreateLocationSourceErrorComponent, BreedingsitesCreateNonFieldErrorsErrorComponent, BreedingsitesCreateNoteErrorComponent, BreedingsitesCreatePhotosINDEXFileErrorComponent, BreedingsitesCreatePhotosINDEXNonFieldErrorsErrorComponent, BreedingsitesCreatePhotosNonFieldErrorsErrorComponent, BreedingsitesCreateSentAtErrorComponent, BreedingsitesCreateSiteTypeErrorComponent, BreedingsitesCreateTagsErrorComponent, BreedingsitesCreateTagsINDEXErrorComponent. Details: " + ", ".join(error_messages))
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

        # deserialize data into BreedingsitesCreateNonFieldErrorsErrorComponent
        try:
            instance.actual_instance = BreedingsitesCreateNonFieldErrorsErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BreedingsitesCreateCreatedAtErrorComponent
        try:
            instance.actual_instance = BreedingsitesCreateCreatedAtErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BreedingsitesCreateSentAtErrorComponent
        try:
            instance.actual_instance = BreedingsitesCreateSentAtErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BreedingsitesCreateLocationNonFieldErrorsErrorComponent
        try:
            instance.actual_instance = BreedingsitesCreateLocationNonFieldErrorsErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BreedingsitesCreateLocationSourceErrorComponent
        try:
            instance.actual_instance = BreedingsitesCreateLocationSourceErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BreedingsitesCreateLocationPointErrorComponent
        try:
            instance.actual_instance = BreedingsitesCreateLocationPointErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BreedingsitesCreateNoteErrorComponent
        try:
            instance.actual_instance = BreedingsitesCreateNoteErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BreedingsitesCreateTagsErrorComponent
        try:
            instance.actual_instance = BreedingsitesCreateTagsErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BreedingsitesCreateTagsINDEXErrorComponent
        try:
            instance.actual_instance = BreedingsitesCreateTagsINDEXErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BreedingsitesCreatePhotosNonFieldErrorsErrorComponent
        try:
            instance.actual_instance = BreedingsitesCreatePhotosNonFieldErrorsErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BreedingsitesCreatePhotosINDEXNonFieldErrorsErrorComponent
        try:
            instance.actual_instance = BreedingsitesCreatePhotosINDEXNonFieldErrorsErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BreedingsitesCreatePhotosINDEXFileErrorComponent
        try:
            instance.actual_instance = BreedingsitesCreatePhotosINDEXFileErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BreedingsitesCreateSiteTypeErrorComponent
        try:
            instance.actual_instance = BreedingsitesCreateSiteTypeErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BreedingsitesCreateHasWaterErrorComponent
        try:
            instance.actual_instance = BreedingsitesCreateHasWaterErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BreedingsitesCreateInPublicAreaErrorComponent
        try:
            instance.actual_instance = BreedingsitesCreateInPublicAreaErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BreedingsitesCreateHasNearMosquitoesErrorComponent
        try:
            instance.actual_instance = BreedingsitesCreateHasNearMosquitoesErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BreedingsitesCreateHasLarvaeErrorComponent
        try:
            instance.actual_instance = BreedingsitesCreateHasLarvaeErrorComponent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into BreedingsitesCreateError with oneOf schemas: BreedingsitesCreateCreatedAtErrorComponent, BreedingsitesCreateHasLarvaeErrorComponent, BreedingsitesCreateHasNearMosquitoesErrorComponent, BreedingsitesCreateHasWaterErrorComponent, BreedingsitesCreateInPublicAreaErrorComponent, BreedingsitesCreateLocationNonFieldErrorsErrorComponent, BreedingsitesCreateLocationPointErrorComponent, BreedingsitesCreateLocationSourceErrorComponent, BreedingsitesCreateNonFieldErrorsErrorComponent, BreedingsitesCreateNoteErrorComponent, BreedingsitesCreatePhotosINDEXFileErrorComponent, BreedingsitesCreatePhotosINDEXNonFieldErrorsErrorComponent, BreedingsitesCreatePhotosNonFieldErrorsErrorComponent, BreedingsitesCreateSentAtErrorComponent, BreedingsitesCreateSiteTypeErrorComponent, BreedingsitesCreateTagsErrorComponent, BreedingsitesCreateTagsINDEXErrorComponent. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into BreedingsitesCreateError with oneOf schemas: BreedingsitesCreateCreatedAtErrorComponent, BreedingsitesCreateHasLarvaeErrorComponent, BreedingsitesCreateHasNearMosquitoesErrorComponent, BreedingsitesCreateHasWaterErrorComponent, BreedingsitesCreateInPublicAreaErrorComponent, BreedingsitesCreateLocationNonFieldErrorsErrorComponent, BreedingsitesCreateLocationPointErrorComponent, BreedingsitesCreateLocationSourceErrorComponent, BreedingsitesCreateNonFieldErrorsErrorComponent, BreedingsitesCreateNoteErrorComponent, BreedingsitesCreatePhotosINDEXFileErrorComponent, BreedingsitesCreatePhotosINDEXNonFieldErrorsErrorComponent, BreedingsitesCreatePhotosNonFieldErrorsErrorComponent, BreedingsitesCreateSentAtErrorComponent, BreedingsitesCreateSiteTypeErrorComponent, BreedingsitesCreateTagsErrorComponent, BreedingsitesCreateTagsINDEXErrorComponent. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], BreedingsitesCreateCreatedAtErrorComponent, BreedingsitesCreateHasLarvaeErrorComponent, BreedingsitesCreateHasNearMosquitoesErrorComponent, BreedingsitesCreateHasWaterErrorComponent, BreedingsitesCreateInPublicAreaErrorComponent, BreedingsitesCreateLocationNonFieldErrorsErrorComponent, BreedingsitesCreateLocationPointErrorComponent, BreedingsitesCreateLocationSourceErrorComponent, BreedingsitesCreateNonFieldErrorsErrorComponent, BreedingsitesCreateNoteErrorComponent, BreedingsitesCreatePhotosINDEXFileErrorComponent, BreedingsitesCreatePhotosINDEXNonFieldErrorsErrorComponent, BreedingsitesCreatePhotosNonFieldErrorsErrorComponent, BreedingsitesCreateSentAtErrorComponent, BreedingsitesCreateSiteTypeErrorComponent, BreedingsitesCreateTagsErrorComponent, BreedingsitesCreateTagsINDEXErrorComponent]]:
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


