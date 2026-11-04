# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["AdminCreateProjectParams"]


class AdminCreateProjectParams(TypedDict, total=False):
    name: Required[str]
    """Project display name."""

    allowed_origins: SequenceNotStr[str]
    """Additional project origins. Shared TOML origins are always included."""

    retention_seconds: Optional[int]
    """Retention by server receipt time, in seconds.

    0 disables expiration; null inherits the installation default. Omission also
    inherits the default.
    """
