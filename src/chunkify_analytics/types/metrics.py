# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Metrics"]


class Metrics(BaseModel):
    total_playing_time_ms: float

    unique_viewers: int

    views: int
