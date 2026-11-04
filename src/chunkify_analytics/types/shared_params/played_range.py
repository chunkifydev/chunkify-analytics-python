# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PlayedRange"]


class PlayedRange(TypedDict, total=False):
    end_seconds: Required[float]
    """Exclusive media position in seconds, greater than start_seconds."""

    start_seconds: Required[float]
    """Inclusive media position in seconds."""
