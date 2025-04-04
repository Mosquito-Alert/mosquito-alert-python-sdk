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
from typing import Any, ClassVar, Dict, List, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class PredictionScore(BaseModel):
    """
    PredictionScore
    """ # noqa: E501
    ae_albopictus: Union[Annotated[float, Field(le=1.0, strict=True, ge=0.0)], Annotated[int, Field(le=1, strict=True, ge=0)]] = Field(description="Score value for the class Aedes albopictus")
    ae_aegypti: Union[Annotated[float, Field(le=1.0, strict=True, ge=0.0)], Annotated[int, Field(le=1, strict=True, ge=0)]] = Field(description="Score value for the class Aedes aegypti")
    ae_japonicus: Union[Annotated[float, Field(le=1.0, strict=True, ge=0.0)], Annotated[int, Field(le=1, strict=True, ge=0)]] = Field(description="Score value for the class Aedes japonicus")
    ae_koreicus: Union[Annotated[float, Field(le=1.0, strict=True, ge=0.0)], Annotated[int, Field(le=1, strict=True, ge=0)]] = Field(description="Score value for the class Aedes koreicus")
    culex: Union[Annotated[float, Field(le=1.0, strict=True, ge=0.0)], Annotated[int, Field(le=1, strict=True, ge=0)]] = Field(description="Score value for the class Culex (s.p)")
    anopheles: Union[Annotated[float, Field(le=1.0, strict=True, ge=0.0)], Annotated[int, Field(le=1, strict=True, ge=0)]] = Field(description="Score value for the class Anopheles (s.p.)")
    culiseta: Union[Annotated[float, Field(le=1.0, strict=True, ge=0.0)], Annotated[int, Field(le=1, strict=True, ge=0)]] = Field(description="Score value for the class Culiseta (s.p.)")
    other_species: Union[Annotated[float, Field(le=1.0, strict=True, ge=0.0)], Annotated[int, Field(le=1, strict=True, ge=0)]] = Field(description="Score value for the class Ohter species")
    not_sure: Union[Annotated[float, Field(le=1.0, strict=True, ge=0.0)], Annotated[int, Field(le=1, strict=True, ge=0)]] = Field(description="Score value for the class Unidentifiable")
    __properties: ClassVar[List[str]] = ["ae_albopictus", "ae_aegypti", "ae_japonicus", "ae_koreicus", "culex", "anopheles", "culiseta", "other_species", "not_sure"]

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
        """Create an instance of PredictionScore from a JSON string"""
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
        """Create an instance of PredictionScore from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ae_albopictus": obj.get("ae_albopictus"),
            "ae_aegypti": obj.get("ae_aegypti"),
            "ae_japonicus": obj.get("ae_japonicus"),
            "ae_koreicus": obj.get("ae_koreicus"),
            "culex": obj.get("culex"),
            "anopheles": obj.get("anopheles"),
            "culiseta": obj.get("culiseta"),
            "other_species": obj.get("other_species"),
            "not_sure": obj.get("not_sure")
        })
        return _obj


