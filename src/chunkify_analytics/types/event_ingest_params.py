# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .analytics_event_param import AnalyticsEventParam

__all__ = ["EventIngestParams"]


class EventIngestParams(TypedDict, total=False):
    event: Required[AnalyticsEventParam]
    """A schema version 1 playback event. Extra properties are preserved."""

    content_encoding: Annotated[Literal["identity"], PropertyInfo(alias="Content-Encoding")]

    origin: Annotated[str, PropertyInfo(alias="Origin")]
