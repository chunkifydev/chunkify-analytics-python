# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel

__all__ = ["OtlpContextAttribute"]


class OtlpContextAttribute(BaseModel):
    key: Optional[str] = None

    value: Optional["OtlpAnyValue"] = None
    """Standard OTLP AnyValue in a preserved resource, scope or body.

    This collector does not decode these fields into the event.
    """


from .otlp_any_value import OtlpAnyValue
