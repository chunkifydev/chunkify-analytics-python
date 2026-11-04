# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .analytics_event import AnalyticsEvent
from .shared.event_context import EventContext

__all__ = ["StoredEvent"]


class StoredEvent(BaseModel):
    event: AnalyticsEvent
    """A schema version 1 playback event. Extra properties are preserved."""

    ingest_key_id: Optional[str] = None
    """ID of the public key used to receive this event. Null when unavailable."""

    project_id: str
    """Trusted project identifier resolved from the public key.

    Historical events migrate to default.
    """

    received_at: datetime

    event_context: Optional[EventContext] = None
    """Browser context and locally derived continent/country/city.

    Request IP addresses are never added to events or stored context.
    """

    otlp: Optional["StoredOtlpContext"] = None
    """
    Legacy context present for an event received through OTLP by an earlier
    collector version. Existing context remains readable; new ingestion accepts
    native JSON events only.
    """


from .shared.stored_otlp_context import StoredOtlpContext
