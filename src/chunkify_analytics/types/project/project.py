# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Project"]


class Project(BaseModel):
    allowed_origins: List[str]

    effective_allowed_origins: List[str]
    """Combined shared and project origins."""

    effective_retention_seconds: int
    """Effective retention in seconds after resolving the installation default.

    0 disables expiration.
    """

    name: str

    project_id: str

    restart_required: Literal[False]

    retention_seconds: Optional[int] = None
    """Retention by server receipt time, in seconds.

    0 disables expiration; null inherits the installation default.
    """

    warning: Optional[str] = None
