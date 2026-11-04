# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["RenditionMetric"]


class RenditionMetric(BaseModel):
    """
    One rendition identified by its dimensions, codec, declared bitrate and frame rate.
    """

    bitrate_bps: Optional[float] = None
    """Declared rendition bitrate in bits per second, not measured network throughput."""

    codec: Optional[str] = None
    """Reported codec; null when unknown."""

    frame_rate: Optional[float] = None
    """Reported frames per second; null when unknown."""

    height: Optional[float] = None
    """Reported height in pixels; null when unknown."""

    playing_time_ms: float
    """Cumulative measured playing time for this rendition, summed once per attempt."""

    playing_time_ratio: float
    """
    Share of all measured rendition playing time, including rows outside the
    returned limit.
    """

    views: int
    """Distinct attempts with positive playing time for this rendition."""

    width: Optional[float] = None
    """Reported width in pixels; null when unknown."""
