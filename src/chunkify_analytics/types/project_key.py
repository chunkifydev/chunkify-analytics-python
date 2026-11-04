# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ProjectKey"]


class ProjectKey(BaseModel):
    id: str

    name: str

    permission: Literal["public", "secret"]

    read_only: bool
    """True for a private key limited to analytics reads through HTTP and MCP.

    Public keys always report false. Rotation preserves this setting.
    """
