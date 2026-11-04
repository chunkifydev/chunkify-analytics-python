# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .error_group import ErrorGroup

__all__ = ["ErrorPage"]


class ErrorPage(BaseModel):
    errors: List[ErrorGroup]

    next_cursor: Optional[str] = None
