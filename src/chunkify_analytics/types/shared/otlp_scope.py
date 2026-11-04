# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OtlpScope"]


class OtlpScope(BaseModel):
    attributes: Optional[List["OtlpContextAttribute"]] = None

    dropped_attributes_count: Optional[int] = FieldInfo(alias="droppedAttributesCount", default=None)

    name: Optional[str] = None

    version: Optional[str] = None


from .otlp_context_attribute import OtlpContextAttribute
