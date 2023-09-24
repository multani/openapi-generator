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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, StrictFloat, StrictStr
from petstore_api.models.deprecated_object import DeprecatedObject
from pydantic import Field

class ObjectWithDeprecatedFields(BaseModel):
    """
    ObjectWithDeprecatedFields
    """
    uuid: Optional[StrictStr] = None
    id: Optional[StrictFloat] = None
    deprecated_ref: Optional[DeprecatedObject] = Field(default=None, serialization_alias="deprecatedRef")
    bars: Optional[List[StrictStr]] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["uuid", "id", "deprecatedRef", "bars"]

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
    def from_json(cls, json_str: str) -> ObjectWithDeprecatedFields:
        """Create an instance of ObjectWithDeprecatedFields from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of deprecated_ref
        if self.deprecated_ref:
            _dict['deprecatedRef'] = self.deprecated_ref.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ObjectWithDeprecatedFields:
        """Create an instance of ObjectWithDeprecatedFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ObjectWithDeprecatedFields.parse_obj(obj)

        _obj = ObjectWithDeprecatedFields.parse_obj({
            "uuid": obj.get("uuid"),
            "id": obj.get("id"),
            "deprecated_ref": DeprecatedObject.from_dict(obj.get("deprecatedRef")) if obj.get("deprecatedRef") is not None else None,
            "bars": obj.get("bars")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties.default:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


