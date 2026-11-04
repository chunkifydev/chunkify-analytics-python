# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .view import View
from .._models import BaseModel

__all__ = ["ViewPage"]


class ViewPage(BaseModel):
    next_cursor: Optional[str] = None

    views: List[View]
