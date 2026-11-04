# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .shared.playback_score import PlaybackScore
from .shared.startup_outcomes import StartupOutcomes

__all__ = ["QualityTimeseriesBucket", "Buffering", "FatalErrors", "StartupTimeMs"]


class Buffering(BaseModel):
    """Duration-weighted buffering.

    Startup wait, pauses and seeking are excluded by the SDK. Unknown durations are not treated as zero.
    """

    ratio: Optional[float] = None
    """Total rebuffer time divided by combined playing and rebuffer time.

    Null without samples. Multiply by 100 for percent.
    """

    sample_views: int
    """
    Views with playing and rebuffer durations available and positive combined
    duration.
    """

    total_playing_time_ms: float
    """Sum of playing time for eligible buffering samples only."""

    total_rebuffer_duration_ms: float
    """Sum of rebuffer time for the same samples."""


class FatalErrors(BaseModel):
    """Observed fatal errors.

    Lost events can undercount this metric; absence of an error is not proof of successful playback.
    """

    affected_views: int
    """
    Distinct selected views with at least one observed matching fatal
    playback_error, including before playback starts.
    """

    ratio: Optional[float] = None
    """Affected views divided by all selected attempts; null when views is zero.

    Multiply by 100 for percent.
    """


class StartupTimeMs(BaseModel):
    """Time from attempt to first playing, measured once per eligible view.

    This is not first-frame timing.
    """

    median: Optional[float] = None
    """Continuous median startup time in milliseconds, or null without samples."""

    p95: Optional[float] = None
    """
    Continuous 95th percentile startup time in milliseconds, or null without
    samples.
    """

    sample_views: int
    """
    Views with a non-null startup measurement on the selected final event or latest
    snapshot.
    """


class QualityTimeseriesBucket(BaseModel):
    """Playback quality for the same start cohort as summary.

    All rates are fractions. Counts expose measurement coverage.
    """

    bucket_start: datetime

    buffering: Buffering
    """Duration-weighted buffering.

    Startup wait, pauses and seeking are excluded by the SDK. Unknown durations are
    not treated as zero.
    """

    fatal_errors: FatalErrors
    """Observed fatal errors.

    Lost events can undercount this metric; absence of an error is not proof of
    successful playback.
    """

    playback_score: PlaybackScore

    startup_outcomes: StartupOutcomes
    """Mutually exclusive outcomes.

    An explicit startup_outcome on the selected final event takes precedence.
    Otherwise an available startup time, including zero, or positive playing time on
    the selected measurement proves started. All other views are unknown.
    sample_views excludes unknown; every ratio uses all selected attempts, including
    unknown. Missing final delivery does not prove an exit or failure.
    """

    startup_time_ms: StartupTimeMs
    """Time from attempt to first playing, measured once per eligible view.

    This is not first-frame timing.
    """

    views: int
    """Selected playback attempts with a retained start, including failed attempts."""
