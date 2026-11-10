# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SubtitlePlayingTime"]


class SubtitlePlayingTime(BaseModel):
    language: Optional[str] = None
    """Subtitle language tag, or null for subtitles off."""

    playing_time_ms: float
