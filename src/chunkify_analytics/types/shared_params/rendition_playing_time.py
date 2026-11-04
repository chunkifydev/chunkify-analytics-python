# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["RenditionPlayingTime"]


class RenditionPlayingTime(TypedDict, total=False):
    bitrate_bps: Required[Optional[float]]

    codec: Required[Optional[str]]

    frame_rate: Required[Optional[float]]

    height: Required[Optional[float]]

    playing_time_ms: Required[float]

    width: Required[Optional[float]]
