# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["ProjectUpdateParams"]


class ProjectUpdateParams(TypedDict, total=False):
    allowed_origins: SequenceNotStr[str]
    """Additional project origins. Shared TOML origins are always included."""

    name: str

    retention_seconds: Optional[int]
    """Retention by server receipt time, in seconds.

    0 disables expiration; null inherits the installation default. Omission leaves
    the current setting unchanged. Applies to existing and new events; removed data
    cannot be recovered.
    """
