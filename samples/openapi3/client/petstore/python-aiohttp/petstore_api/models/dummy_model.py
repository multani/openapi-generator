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

class DummyModel(BaseModel):
    """
    DummyModel
    """
    category: Optional[StrictStr] = None
    self_ref: Optional[SelfReferenceModel] = None
    __properties = ["category", "self_ref"]

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
    def from_json(cls, json_str: str) -> DummyModel:
        """Create an instance of DummyModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of self_ref
        if self.self_ref:
            _dict['self_ref'] = self.self_ref.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DummyModel:
        """Create an instance of DummyModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DummyModel.parse_obj(obj)

        _obj = DummyModel.parse_obj({
            "category": obj.get("category"),
            "self_ref": SelfReferenceModel.from_dict(obj.get("self_ref")) if obj.get("self_ref") is not None else None
        })
        return _obj

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from petstore_api.models.self_reference_model import SelfReferenceModel
    # TODO: pydantic v2
    # DummyModel.model_rebuild()

