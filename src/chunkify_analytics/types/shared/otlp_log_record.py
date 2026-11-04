# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OtlpLogRecord"]


class OtlpLogRecord(BaseModel):
    """A playback event in log attributes.

    Duplicate attributes and invalid event fields reject the request.
    """

    attributes: List["OtlpAttribute"]

    body: Optional["OtlpAnyValue"] = None
    """Standard OTLP AnyValue in a preserved resource, scope or body.

    This collector does not decode these fields into the event.
    """

    dropped_attributes_count: Optional[int] = FieldInfo(alias="droppedAttributesCount", default=None)

    event_name: Optional[str] = FieldInfo(alias="eventName", default=None)

    flags: Optional[int] = None

    observed_time_unix_nano: Optional[str] = FieldInfo(alias="observedTimeUnixNano", default=None)

    severity_number: Optional[int] = FieldInfo(alias="severityNumber", default=None)

    severity_text: Optional[str] = FieldInfo(alias="severityText", default=None)

    span_id: Optional[str] = FieldInfo(alias="spanId", default=None)

    time_unix_nano: Optional[str] = FieldInfo(alias="timeUnixNano", default=None)

    trace_id: Optional[str] = FieldInfo(alias="traceId", default=None)


from .otlp_any_value import OtlpAnyValue
from .otlp_attribute import OtlpAttribute
