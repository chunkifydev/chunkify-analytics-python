# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .shared.playback_score import PlaybackScore

__all__ = ["VideoMetrics"]


class VideoMetrics(BaseModel):
    playback_score: PlaybackScore

    total_playing_time_ms: float

    unique_viewers: int

    video_id: str

    views: int
