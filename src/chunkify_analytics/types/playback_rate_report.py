# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .playback_rate_metric import PlaybackRateMetric

__all__ = ["PlaybackRateReport"]


class PlaybackRateReport(BaseModel):
    rates: List[PlaybackRateMetric]
    """Most-watched first, then value ascending with null first.

    Defaults to 100 rows, maximum 1000. CSV exports include all matching rows.
    """

    sample_views: int
    """Attempts with positive measured playing time in this report.

    Older SDKs send no measurement.
    """

    total_playing_time_ms: float
    """Total measured playing time across all matching rows."""

    total_rates: int
    """Number of distinct values before applying the row limit."""

    views: int
    """All attempts in the filtered start cohort."""
