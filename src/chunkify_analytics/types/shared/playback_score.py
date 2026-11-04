# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PlaybackScore"]


class PlaybackScore(BaseModel):
    sample_views: int
    """Sessions contributing a score, including recorded failures.

    A per-session result is zero or one.
    """

    value: Optional[float] = None
    """Mean of measured per-session playback scores, or null without scored sessions.

    Each session uses startup = 8 / (8 + startup_time_ms / 1000), smoothness =
    exp(-10 _ buffering_ratio), and scores 100 _ startup^0.30 \\** smoothness^0.70.
    Buffering ratio is rebuffer duration divided by playing plus rebuffer duration.
    The 30% startup and 70% smoothness weights are heuristic. A recorded fatal error
    or failed_before_start outcome scores zero. Other sessions require positive
    playing time and known startup and rebuffer durations; ended_before_start and
    unknown outcomes are unscored. Buffering excludes startup, pauses and seeks. The
    score does not use interruption count or measure picture quality.
    """
