# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .subtitle_metric import SubtitleMetric

__all__ = ["SubtitleReport"]


class SubtitleReport(BaseModel):
    languages: List[SubtitleMetric]
    """Most-watched first, then value ascending with null first.

    Defaults to 100 rows, maximum 1000. CSV exports include all matching rows.
    """

    sample_views: int
    """Attempts with positive measured playing time in this report.

    Older SDKs send no measurement.
    """

    total_languages: int
    """Number of distinct values before applying the row limit."""

    total_playing_time_ms: float
    """Total measured playing time across all matching rows."""

    views: int
    """All attempts in the filtered start cohort."""
