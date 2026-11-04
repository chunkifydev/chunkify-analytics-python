# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["MetricCountRatio"]


class MetricCountRatio(BaseModel):
    """View count and fraction of its documented denominator.

    The ratio is null when that denominator is zero.
    """

    ratio: Optional[float] = None

    views: int
