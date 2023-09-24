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


from typing import Dict, Optional
from pydantic import BaseModel
from petstore_api.models.inner_dict_with_property import InnerDictWithProperty
from pydantic import Field

class Parent(BaseModel):
    """
    Parent
    """
    optional_dict: Optional[Dict[str, InnerDictWithProperty]] = Field(default=None, serialization_alias="optionalDict")
    __properties = ["optionalDict"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Parent:
        """Create an instance of Parent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in optional_dict (dict)
        _field_dict = {}
        if self.optional_dict:
            for _key in self.optional_dict:
                if self.optional_dict[_key]:
                    _field_dict[_key] = self.optional_dict[_key].to_dict()
            _dict['optionalDict'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Parent:
        """Create an instance of Parent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Parent.parse_obj(obj)

        _obj = Parent.parse_obj({
            "optional_dict": dict(
                (_k, InnerDictWithProperty.from_dict(_v))
                for _k, _v in obj.get("optionalDict").items()
            )
            if obj.get("optionalDict") is not None
            else None
        })
        return _obj


