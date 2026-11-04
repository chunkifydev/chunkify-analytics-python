# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["WatchTimeDistribution", "Distribution"]


class Distribution(BaseModel):
    """
    Mutually exclusive playing-time buckets: [0,10s), [10s,30s), [30s,60s), [1m,5m), [5m,infinity). Counts sum to sample_views.
    """

    at_least_5_minutes: int

    from_1_to_5_minutes: int

    from_10_to_30_seconds: int

    from_30_to_60_seconds: int

    under_10_seconds: int


class WatchTimeDistribution(BaseModel):
    """
    Playing time in milliseconds from one selected final event or latest snapshot per view. Measured zero is included; missing measurements are excluded. Percentiles use linear interpolation and are null without samples. This sample denominator differs from average_playing_time_ms, which uses all attempts.
    """

    distribution: Distribution
    """
    Mutually exclusive playing-time buckets: [0,10s), [10s,30s), [30s,60s), [1m,5m),
    [5m,infinity). Counts sum to sample_views.
    """

    median: Optional[float] = None

    p95: Optional[float] = None

    sample_views: int
