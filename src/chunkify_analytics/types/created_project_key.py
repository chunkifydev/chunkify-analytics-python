# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CreatedProjectKey"]


class CreatedProjectKey(BaseModel):
    """A newly created key.

    Save the key value now; later key listings contain only metadata.
    """

    key: str
    """New key value. Save it now; it is returned once."""

    key_id: str

    permission: Literal["public", "secret"]

    project_id: str

    read_only: bool
    """True for a private key limited to analytics reads through HTTP and MCP.

    Public keys always report false. Rotation preserves this setting.
    """

    restart_required: Literal[False]

    warning: Optional[str] = None
