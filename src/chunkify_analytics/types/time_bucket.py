# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["TimeBucket"]


class TimeBucket(BaseModel):
    bucket_start: datetime
    """UTC interval start in RFC3339 with milliseconds and Z.

    May precede from in a partial first bucket; only starts inside [from, to)
    contribute.
    """

    total_playing_time_ms: float

    unique_viewers: int

    views: int
