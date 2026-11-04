# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .retention_bucket import RetentionBucket

__all__ = ["RetentionReport"]


class RetentionReport(BaseModel):
    buckets: List[RetentionBucket]

    duration_seconds: Optional[float] = None
    """Longest measured duration in this selection.

    Null when there are no measured attempts.
    """

    interval_seconds: Optional[float] = None
    """Bucket width, ceil(duration_seconds / 200), with a minimum of one second.

    Null without measurements.
    """

    sample_views: int
    """
    Attempts whose selected final or latest snapshot contains played ranges and a
    finite positive media duration. Includes measured empty ranges.
    """

    views: int
    """All matching attempts with a retained start."""
