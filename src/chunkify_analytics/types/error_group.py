# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional

from .._models import BaseModel

__all__ = ["ErrorGroup"]


class ErrorGroup(BaseModel):
    affected_views: int

    error_code: Union[str, float, None] = None

    error_events: int

    fatal: Optional[bool] = None
