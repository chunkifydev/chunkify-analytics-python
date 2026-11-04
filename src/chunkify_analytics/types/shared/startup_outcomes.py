# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .metric_count_ratio import MetricCountRatio

__all__ = ["StartupOutcomes"]


class StartupOutcomes(BaseModel):
    """Mutually exclusive outcomes.

    An explicit startup_outcome on the selected final event takes precedence. Otherwise an available startup time, including zero, or positive playing time on the selected measurement proves started. All other views are unknown. sample_views excludes unknown; every ratio uses all selected attempts, including unknown. Missing final delivery does not prove an exit or failure.
    """

    ended_before_start: MetricCountRatio
    """View count and fraction of its documented denominator.

    The ratio is null when that denominator is zero.
    """

    failed_before_start: MetricCountRatio
    """View count and fraction of its documented denominator.

    The ratio is null when that denominator is zero.
    """

    sample_views: int

    started: MetricCountRatio
    """View count and fraction of its documented denominator.

    The ratio is null when that denominator is zero.
    """

    unknown: MetricCountRatio
    """View count and fraction of its documented denominator.

    The ratio is null when that denominator is zero.
    """
