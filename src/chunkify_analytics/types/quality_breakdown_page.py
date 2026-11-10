# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from .quality import Quality
from .._models import BaseModel

__all__ = ["QualityBreakdownPage", "Group"]


class Group(BaseModel):
    data: Quality
    """Playback quality for the same start cohort as summary.

    All rates are fractions. Counts expose measurement coverage.
    """

    value: Optional[str] = None


class QualityBreakdownPage(BaseModel):
    group_by: Union[
        Literal[
            "browser_name",
            "os_name",
            "device_type",
            "continent",
            "country",
            "city",
            "page_origin",
            "page_path",
            "subtitle_language",
            "playback_rate",
            "video_title",
            "user_id",
        ],
        str,
    ]
    """A custom dimension key, such as custom.plan."""

    groups: List[Group]

    next_cursor: Optional[str] = None
