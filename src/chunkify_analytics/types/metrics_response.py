# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .metrics import Metrics
from .metrics_breakdown_page import MetricsBreakdownPage

__all__ = ["MetricsResponse"]

MetricsResponse: TypeAlias = Union[Metrics, MetricsBreakdownPage]
