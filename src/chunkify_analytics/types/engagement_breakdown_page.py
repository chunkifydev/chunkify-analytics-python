# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .engagement import Engagement

__all__ = ["EngagementBreakdownPage", "Group"]


class Group(BaseModel):
    data: Engagement
    """Observed watch time and end-of-media for the same start cohort as summary.

    Missing delivery can undercount both.
    """

    value: Optional[str] = None


class EngagementBreakdownPage(BaseModel):
    group_by: Literal[
        "browser_name", "os_name", "device_type", "continent", "country", "city", "page_origin", "page_path"
    ]

    groups: List[Group]

    next_cursor: Optional[str] = None
