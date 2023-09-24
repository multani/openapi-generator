# coding: utf-8

"""
    Echo Server API

    Echo Server API

    The version of the OpenAPI document: 0.1.0
    Contact: team@openapitools.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt
from pydantic import Field
from typing_extensions import Annotated

class NumberPropertiesOnly(BaseModel):
    """
    NumberPropertiesOnly
    """
    number: Optional[Union[StrictFloat, StrictInt]] = None
    # TODO: pydantic v2: this field name override the default `float` type
    # float: Optional[Union[StrictFloat, StrictInt]] = None
    double: Optional[Union[Annotated[float, Field(le=50.2, strict=True, ge=0.8)], Annotated[int, Field(le=50, strict=True, ge=1)]]] = None
    __properties = ["number", "float", "double"]

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
    def from_json(cls, json_str: str) -> NumberPropertiesOnly:
        """Create an instance of NumberPropertiesOnly from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NumberPropertiesOnly:
        """Create an instance of NumberPropertiesOnly from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NumberPropertiesOnly.parse_obj(obj)

        _obj = NumberPropertiesOnly.parse_obj({
            "number": obj.get("number"),
            "float": obj.get("float"),
            "double": obj.get("double")
        })
        return _obj


