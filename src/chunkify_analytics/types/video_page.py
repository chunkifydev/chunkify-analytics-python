# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .video_metrics import VideoMetrics

__all__ = ["VideoPage"]


class VideoPage(BaseModel):
    next_cursor: Optional[str] = None

    videos: List[VideoMetrics]
