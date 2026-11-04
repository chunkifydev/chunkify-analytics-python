# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .shared.progress_reached import ProgressReached
from .shared.watch_time_distribution import WatchTimeDistribution

__all__ = ["EngagementTimeseriesBucket"]


class EngagementTimeseriesBucket(BaseModel):
    """Observed watch time and end-of-media for the same start cohort as summary.

    Missing delivery can undercount both.
    """

    average_playing_time_ms: Optional[float] = None
    """Total playing time divided by all selected attempts.

    Null with no views; zero when views exist with no measured time.
    """

    bucket_start: datetime

    progress_reached: ProgressReached
    """Furthest progress on the selected final event or latest snapshot.

    Only views with a positive known media duration and a progress ratio in [0,1]
    are samples. Each milestone ratio uses sample_views. Seeking can count; this is
    not watched coverage or audience retention.
    """

    reached_end_ratio: Optional[float] = None
    """Reached-end views divided by all selected attempts.

    Null without views. Multiply by 100 for percent. Does not imply the whole video
    was watched.
    """

    reached_end_views: int
    """Views whose winning final event has reason=ended.

    Counts each selected view at most once.
    """

    total_playing_time_ms: float
    """Cumulative playing time summed once per selected view, as in summary."""

    views: int
    """
    Selected playback attempts with a retained start, including failed, ongoing and
    start-only attempts.
    """

    watch_time_ms: WatchTimeDistribution
    """
    Playing time in milliseconds from one selected final event or latest snapshot
    per view. Measured zero is included; missing measurements are excluded.
    Percentiles use linear interpolation and are null without samples. This sample
    denominator differs from average_playing_time_ms, which uses all attempts.
    """
