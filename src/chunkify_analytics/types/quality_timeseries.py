# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .quality_timeseries_bucket import QualityTimeseriesBucket

__all__ = ["QualityTimeseries"]


class QualityTimeseries(BaseModel):
    buckets: List[QualityTimeseriesBucket]

    from_: datetime = FieldInfo(alias="from")
    """Inclusive query bound normalized to UTC milliseconds."""

    interval: Literal["hour", "day"]

    kind: Literal["quality"]

    timezone: Literal["UTC"]

    to: datetime
    """Exclusive query bound normalized to UTC milliseconds."""
