# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OtlpAnyValue", "ArrayValue", "KvlistValue"]


class ArrayValue(BaseModel):
    values: Optional[List[Optional["OtlpAnyValue"]]] = None


class KvlistValue(BaseModel):
    values: Optional[List["OtlpContextAttribute"]] = None


class OtlpAnyValue(BaseModel):
    """Standard OTLP AnyValue in a preserved resource, scope or body.

    This collector does not decode these fields into the event.
    """

    array_value: Optional[ArrayValue] = FieldInfo(alias="arrayValue", default=None)

    bool_value: Optional[bool] = FieldInfo(alias="boolValue", default=None)

    bytes_value: Optional[str] = FieldInfo(alias="bytesValue", default=None)

    double_value: Optional[float] = FieldInfo(alias="doubleValue", default=None)

    int_value: Union[str, int, None] = FieldInfo(alias="intValue", default=None)
    """Signed int64. Strings avoid JavaScript precision loss."""

    kvlist_value: Optional[KvlistValue] = FieldInfo(alias="kvlistValue", default=None)

    string_value: Optional[str] = FieldInfo(alias="stringValue", default=None)

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


from .otlp_context_attribute import OtlpContextAttribute
