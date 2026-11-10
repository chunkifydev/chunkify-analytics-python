# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DimensionValues", "Value"]


class Value(BaseModel):
    value: Optional[str] = None

    views: int


class DimensionValues(BaseModel):
    dimension: Union[
        Literal[
            "browser_name",
            "os_name",
            "device_type",
            "video_id",
            "viewer_id",
            "user_id",
            "video_title",
            "continent",
            "country",
            "city",
            "page_origin",
            "page_path",
            "subtitle_language",
            "playback_rate",
            "custom_keys",
        ],
        str,
    ]
    """One custom dimension's values, such as custom.plan."""

    next_cursor: Optional[str] = None

    values: List[Value]
