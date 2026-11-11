# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["PlaybackRateMetric"]


class PlaybackRateMetric(BaseModel):
    """Watch time at one playback rate."""

    playing_time_ms: float
    """Cumulative measured playing time at this rate, summed once per attempt."""

    playing_time_ratio: float
    """Share of all measured playing time, including rows outside the returned limit."""

    rate: float
    """Playback rate, rounded to two decimals."""

    views: int
    """Distinct attempts with positive playing time at this rate."""
