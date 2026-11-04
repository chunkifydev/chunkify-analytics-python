# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["RetentionBucket"]


class RetentionBucket(BaseModel):
    end_seconds: float
    """Exclusive end of the section, capped at the reported duration."""

    ratio: float
    """views divided by sample_views."""

    start_seconds: float
    """Inclusive start of the video section."""

    views: int
    """Distinct attempts that played any part of this section.

    Each attempt counts at most once.
    """
