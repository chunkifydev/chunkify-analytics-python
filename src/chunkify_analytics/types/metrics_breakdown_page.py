# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .metrics import Metrics
from .._models import BaseModel

__all__ = ["MetricsBreakdownPage", "Group"]


class Group(BaseModel):
    data: Metrics

    value: Optional[str] = None


class MetricsBreakdownPage(BaseModel):
    group_by: Literal[
        "browser_name", "os_name", "device_type", "continent", "country", "city", "page_origin", "page_path"
    ]

    groups: List[Group]

    next_cursor: Optional[str] = None
