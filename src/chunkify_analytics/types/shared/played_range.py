# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["PlayedRange"]


class PlayedRange(BaseModel):
    end_seconds: float
    """Exclusive media position in seconds, greater than start_seconds."""

    start_seconds: float
    """Inclusive media position in seconds."""
