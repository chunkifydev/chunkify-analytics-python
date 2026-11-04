# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .view import View
from .._models import BaseModel

__all__ = ["ViewDetail"]


class ViewDetail(BaseModel):
    events: List["StoredEvent"]

    next_cursor: Optional[str] = None

    view: View


from .stored_event import StoredEvent
