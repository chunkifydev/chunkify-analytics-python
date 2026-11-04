# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CreatedProject"]


class CreatedProject(BaseModel):
    effective_retention_seconds: int
    """Effective retention in seconds after resolving the installation default.

    0 disables expiration.
    """

    name: str
    """Project display name."""

    project_id: str

    public_key: str
    """Public key for sending events."""

    restart_required: Literal[False]

    retention_seconds: Optional[int] = None
    """Retention by server receipt time, in seconds.

    0 disables expiration; null inherits the installation default.
    """

    secret_key: str
    """Secret key for this project. Save it now; it is returned once."""

    warning: Optional[str] = None
