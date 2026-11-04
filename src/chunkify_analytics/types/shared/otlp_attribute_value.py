# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "OtlpAttributeValue",
    "UnionMember0",
    "UnionMember1",
    "UnionMember2",
    "UnionMember3",
    "UnionMember4",
    "UnionMember5",
    "UnionMember6",
]


class UnionMember0(BaseModel):
    array_value: None = FieldInfo(alias="arrayValue", default=None)

    bool_value: None = FieldInfo(alias="boolValue", default=None)

    bytes_value: None = FieldInfo(alias="bytesValue", default=None)

    double_value: None = FieldInfo(alias="doubleValue", default=None)

    int_value: None = FieldInfo(alias="intValue", default=None)

    kvlist_value: None = FieldInfo(alias="kvlistValue", default=None)

    string_value: None = FieldInfo(alias="stringValue", default=None)


class UnionMember1(BaseModel):
    string_value: object = FieldInfo(alias="stringValue")

    array_value: None = FieldInfo(alias="arrayValue", default=None)

    bool_value: None = FieldInfo(alias="boolValue", default=None)

    bytes_value: None = FieldInfo(alias="bytesValue", default=None)

    double_value: None = FieldInfo(alias="doubleValue", default=None)

    int_value: None = FieldInfo(alias="intValue", default=None)

    kvlist_value: None = FieldInfo(alias="kvlistValue", default=None)


class UnionMember2(BaseModel):
    bool_value: object = FieldInfo(alias="boolValue")

    array_value: None = FieldInfo(alias="arrayValue", default=None)

    bytes_value: None = FieldInfo(alias="bytesValue", default=None)

    double_value: None = FieldInfo(alias="doubleValue", default=None)

    int_value: None = FieldInfo(alias="intValue", default=None)

    kvlist_value: None = FieldInfo(alias="kvlistValue", default=None)

    string_value: None = FieldInfo(alias="stringValue", default=None)


class UnionMember3(BaseModel):
    int_value: object = FieldInfo(alias="intValue")

    array_value: None = FieldInfo(alias="arrayValue", default=None)

    bool_value: None = FieldInfo(alias="boolValue", default=None)

    bytes_value: None = FieldInfo(alias="bytesValue", default=None)

    double_value: None = FieldInfo(alias="doubleValue", default=None)

    kvlist_value: None = FieldInfo(alias="kvlistValue", default=None)

    string_value: None = FieldInfo(alias="stringValue", default=None)


class UnionMember4(BaseModel):
    double_value: object = FieldInfo(alias="doubleValue")

    array_value: None = FieldInfo(alias="arrayValue", default=None)

    bool_value: None = FieldInfo(alias="boolValue", default=None)

    bytes_value: None = FieldInfo(alias="bytesValue", default=None)

    int_value: None = FieldInfo(alias="intValue", default=None)

    kvlist_value: None = FieldInfo(alias="kvlistValue", default=None)

    string_value: None = FieldInfo(alias="stringValue", default=None)


class UnionMember5(BaseModel):
    array_value: object = FieldInfo(alias="arrayValue")

    bool_value: None = FieldInfo(alias="boolValue", default=None)

    bytes_value: None = FieldInfo(alias="bytesValue", default=None)

    double_value: None = FieldInfo(alias="doubleValue", default=None)

    int_value: None = FieldInfo(alias="intValue", default=None)

    kvlist_value: None = FieldInfo(alias="kvlistValue", default=None)

    string_value: None = FieldInfo(alias="stringValue", default=None)


class UnionMember6(BaseModel):
    kvlist_value: object = FieldInfo(alias="kvlistValue")

    array_value: None = FieldInfo(alias="arrayValue", default=None)

    bool_value: None = FieldInfo(alias="boolValue", default=None)

    bytes_value: None = FieldInfo(alias="bytesValue", default=None)

    double_value: None = FieldInfo(alias="doubleValue", default=None)

    int_value: None = FieldInfo(alias="intValue", default=None)

    string_value: None = FieldInfo(alias="stringValue", default=None)


OtlpAttributeValue: TypeAlias = Union[
    UnionMember0, UnionMember1, UnionMember2, UnionMember3, UnionMember4, UnionMember5, UnionMember6, None
]
