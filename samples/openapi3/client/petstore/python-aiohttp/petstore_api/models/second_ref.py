# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictStr

class SecondRef(BaseModel):
    """
    SecondRef
    """
    category: Optional[StrictStr] = None
    circular_ref: Optional[CircularReferenceModel] = None
    __properties = ["category", "circular_ref"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> SecondRef:
        """Create an instance of SecondRef from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of circular_ref
        if self.circular_ref:
            _dict['circular_ref'] = self.circular_ref.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SecondRef:
        """Create an instance of SecondRef from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SecondRef.parse_obj(obj)

        _obj = SecondRef.parse_obj({
            "category": obj.get("category"),
            "circular_ref": CircularReferenceModel.from_dict(obj.get("circular_ref")) if obj.get("circular_ref") is not None else None
        })
        return _obj

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from petstore_api.models.circular_reference_model import CircularReferenceModel
    # TODO: pydantic v2
    # SecondRef.model_rebuild()

