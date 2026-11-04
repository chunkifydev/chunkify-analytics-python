# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .metric_count_ratio import MetricCountRatio

__all__ = ["ProgressReached"]


class ProgressReached(BaseModel):
    """Furthest progress on the selected final event or latest snapshot.

    Only views with a positive known media duration and a progress ratio in [0,1] are samples. Each milestone ratio uses sample_views. Seeking can count; this is not watched coverage or audience retention.
    """

    at_100_percent: MetricCountRatio
    """View count and fraction of its documented denominator.

    The ratio is null when that denominator is zero.
    """

    at_25_percent: MetricCountRatio
    """View count and fraction of its documented denominator.

    The ratio is null when that denominator is zero.
    """

    at_50_percent: MetricCountRatio
    """View count and fraction of its documented denominator.

    The ratio is null when that denominator is zero.
    """

    at_75_percent: MetricCountRatio
    """View count and fraction of its documented denominator.

    The ratio is null when that denominator is zero.
    """

    sample_views: int
