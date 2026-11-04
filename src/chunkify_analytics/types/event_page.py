# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel

__all__ = ["EventPage"]


class EventPage(BaseModel):
    events: List["StoredEvent"]

    next_cursor: Optional[str] = None


from .stored_event import StoredEvent
