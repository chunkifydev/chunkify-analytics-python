# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["PlaybackRatePlayingTime"]


class PlaybackRatePlayingTime(BaseModel):
    playing_time_ms: float

    rate: float
    """Playback rate, rounded to two decimals."""
