# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .rendition_metric import RenditionMetric

__all__ = ["RenditionReport"]


class RenditionReport(BaseModel):
    average_bitrate_bps: Optional[float] = None
    """Time-weighted mean declared bitrate.

    Null without playing time with a known bitrate.
    """

    bitrate_sample_playing_time_ms: float
    """
    Measured playing time with a known rendition bitrate, used as the average
    denominator.
    """

    renditions: List[RenditionMetric]
    """Most-played renditions first.

    Defaults to 100 rows, maximum 1000. CSV exports include all matching rows.
    """

    sample_views: int
    """Attempts with positive measured rendition playing time."""

    total_playing_time_ms: float
    """Total measured rendition playing time across all matching rows.

    Can be less than overall watch time when rendition information is missing.
    """

    total_renditions: int
    """Number of distinct renditions before applying the row limit."""

    views: int
    """All attempts in the filtered start cohort."""
