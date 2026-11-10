# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .shared.playback_score import PlaybackScore

__all__ = ["View"]


class View(BaseModel):
    browser_name: Optional[str] = None

    device_type: Optional[str] = None

    has_ended_event: bool

    has_fatal_error: bool

    os_name: Optional[str] = None

    playback_score: PlaybackScore

    playing_time_ms: float

    reached_end: bool

    rebuffer_duration_ms: Optional[float] = None

    started_at: datetime

    startup_time_ms: Optional[float] = None

    user_id: Optional[str] = None

    video_id: str

    video_title: Optional[str] = None

    view_id: str

    viewer_id: Optional[str] = None
