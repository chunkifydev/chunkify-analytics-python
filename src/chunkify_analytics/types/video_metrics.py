# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .shared.playback_score import PlaybackScore

__all__ = ["VideoMetrics"]


class VideoMetrics(BaseModel):
    playback_score: PlaybackScore

    total_playing_time_ms: float

    unique_viewers: int

    video_id: str

    video_title: Optional[str] = None
    """Title from the most recently received selected start that supplied one."""

    views: int
