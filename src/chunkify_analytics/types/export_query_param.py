# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ExportQueryParam"]

_ExportQueryParamReservedKeywords = TypedDict(
    "_ExportQueryParamReservedKeywords",
    {
        "from": Union[str, datetime],
    },
    total=False,
)


class ExportQueryParam(_ExportQueryParamReservedKeywords, total=False):
    browser_name: str

    city: str

    continent: Literal["AF", "AN", "AS", "EU", "NA", "OC", "SA"]

    country: str

    device_type: Literal["desktop", "mobile", "tablet", "unknown"]

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

    event_name: Literal[
        "chunkify.video.view_started",
        "chunkify.video.view_snapshot",
        "chunkify.video.playback_error",
        "chunkify.video.view_ended",
        "chunkify.video.playback_state_changed",
        "chunkify.video.rendition_changed",
        "chunkify.video.seek_completed",
        "chunkify.video.subtitle_changed",
        "chunkify.video.playback_rate_changed",
    ]

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

    has_fatal_error: bool

    interval: Literal["hour", "day"]

    kind: Literal["summary", "quality", "engagement"]

    order: Literal["asc", "desc"]

    os_name: str

    page_origin: str
    """
    Exact, case-sensitive page_origin from the first retained view start, or each
    event for raw-event exports.
    """

    page_path: str
    """
    Exact, case-sensitive page_path from the first retained view start, or each
    event for raw-event exports.
    """

    playback_rate: str

    sort_by: Literal[
        "video_id",
        "views",
        "unique_viewers",
        "total_playing_time_ms",
        "playback_score",
        "started_at",
        "view_id",
        "device_type",
        "playing_time_ms",
        "startup_time_ms",
        "rebuffer_duration_ms",
    ]
    """Videos or views only.

    Use a sort field supported by the selected resource. Defaults to video_id for
    videos and started_at for views.
    """

    subtitle_language: str

    to: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    user_id: str

    video_id: str

    video_title: str

    view_id: str

    viewer_id: str
