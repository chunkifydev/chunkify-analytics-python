# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SubtitlePlayingTime"]


class SubtitlePlayingTime(TypedDict, total=False):
    language: Required[Optional[str]]
    """Subtitle language tag, or null for subtitles off."""

    playing_time_ms: Required[float]
