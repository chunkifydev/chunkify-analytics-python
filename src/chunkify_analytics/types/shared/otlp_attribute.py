# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel
from .otlp_attribute_value import OtlpAttributeValue

__all__ = ["OtlpAttribute"]


class OtlpAttribute(BaseModel):
    """
    An absent or null key decodes to the empty string; duplicate decoded keys reject the request. An absent value decodes to null.
    """

    key: Optional[str] = None

    value: Optional[OtlpAttributeValue] = None
    """A typed log attribute.

    At most one value field can be set. Binary values are unsupported.
    """
