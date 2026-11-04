# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .timeseries import Timeseries
from .quality_timeseries import QualityTimeseries
from .engagement_timeseries import EngagementTimeseries

__all__ = ["TimeseriesResponse"]

TimeseriesResponse: TypeAlias = Union[Timeseries, QualityTimeseries, EngagementTimeseries]
