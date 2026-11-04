# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DimensionValues", "Value"]


class Value(BaseModel):
    value: Optional[str] = None

    views: int


class DimensionValues(BaseModel):
    dimension: Literal[
        "browser_name",
        "os_name",
        "device_type",
        "video_id",
        "viewer_id",
        "continent",
        "country",
        "city",
        "page_origin",
        "page_path",
    ]

    next_cursor: Optional[str] = None

    values: List[Value]
