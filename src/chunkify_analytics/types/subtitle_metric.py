# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SubtitleMetric"]


class SubtitleMetric(BaseModel):
    """Watch time with one subtitle language, or with subtitles off."""

    language: Optional[str] = None
    """
    Subtitle language tag; und for a track without a language; null for subtitles
    off.
    """

    playing_time_ms: float
    """Cumulative measured playing time in this language, summed once per attempt."""

    playing_time_ratio: float
    """Share of all measured playing time, including rows outside the returned limit."""

    views: int
    """Distinct attempts with positive playing time in this language."""
