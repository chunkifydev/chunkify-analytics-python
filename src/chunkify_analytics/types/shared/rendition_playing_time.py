# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RenditionPlayingTime"]


class RenditionPlayingTime(BaseModel):
    bitrate_bps: Optional[float] = None

    codec: Optional[str] = None

    frame_rate: Optional[float] = None

    height: Optional[float] = None

    playing_time_ms: float

    width: Optional[float] = None
