# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from petstore_api.models.enum_string1 import EnumString1
from petstore_api.models.enum_string2 import EnumString2
from typing import Union, Any, List, TYPE_CHECKING, Literal, Optional, Dict
from pydantic import StrictStr, Field

ONEOFENUMSTRING_ONE_OF_SCHEMAS = ["EnumString1", "EnumString2"]

class OneOfEnumString(BaseModel):
    """
    oneOf enum strings
    """
    # data type: EnumString1
    oneof_schema_1_validator: Optional[EnumString1] = None
    # data type: EnumString2
    oneof_schema_2_validator: Optional[EnumString2] = None
    actual_instance: Optional[Union[EnumString1, EnumString2]] = None
    one_of_schemas: List[str] = Literal[ONEOFENUMSTRING_ONE_OF_SCHEMAS]

    class Config:
        validate_assignment = True

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = OneOfEnumString.construct()
        error_messages = []
        match = 0
        # validate data type: EnumString1
        if not isinstance(v, EnumString1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `EnumString1`")
        else:
            match += 1
        # validate data type: EnumString2
        if not isinstance(v, EnumString2):
            error_messages.append(f"Error! Input type `{type(v)}` is not `EnumString2`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in OneOfEnumString with oneOf schemas: EnumString1, EnumString2. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in OneOfEnumString with oneOf schemas: EnumString1, EnumString2. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> OneOfEnumString:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> OneOfEnumString:
        """Returns the object represented by the json string"""
        instance = OneOfEnumString.construct()
        error_messages = []
        match = 0

        # deserialize data into EnumString1
        try:
            instance.actual_instance = EnumString1.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into EnumString2
        try:
            instance.actual_instance = EnumString2.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into OneOfEnumString with oneOf schemas: EnumString1, EnumString2. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into OneOfEnumString with oneOf schemas: EnumString1, EnumString2. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())


