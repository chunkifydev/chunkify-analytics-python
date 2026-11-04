# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.rendition_playing_time import RenditionPlayingTime

__all__ = ["RenditionChangedParam"]


class RenditionChangedParam(TypedDict, total=False):
    connector_name: Required[str]

    connector_version: Required[Optional[str]]

    delivery_hostname: Required[Optional[str]]

    environment: Required[Optional[str]]

    error_category: Required[Optional[Literal["aborted", "network", "decode", "unsupported", "unknown"]]]

    error_code: Required[Union[str, float, None]]

    error_fatal: Required[Optional[bool]]

    error_playhead_seconds: Required[Optional[float]]

    event_id: Required[str]

    event_name: Required[Literal["chunkify.video.rendition_changed"]]

    occurred_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    player_height_px: Required[Optional[float]]

    player_name: Required[Optional[str]]

    player_version: Required[Optional[str]]

    player_width_px: Required[Optional[float]]

    playhead_seconds: Required[Optional[float]]

    previous_rendition_bitrate_bps: Required[Optional[float]]

    previous_rendition_codec: Required[Optional[str]]

    previous_rendition_frame_rate: Required[Optional[float]]

    previous_rendition_height: Required[Optional[float]]

    previous_rendition_width: Required[Optional[float]]

    reason: Required[Optional[Literal["ended", "destroyed", "source_changed", "page_exit"]]]

    schema_version: Required[Literal[1]]

    sdk_name: Required[str]
    """Name of the SDK or integration that produced the event.

    Informational metadata, preserved as received. Must contain at least one
    non-whitespace character.
    """

    sdk_version: Required[str]

    selected_rendition_bitrate_bps: Required[Optional[float]]

    selected_rendition_codec: Required[Optional[str]]

    selected_rendition_frame_rate: Required[Optional[float]]

    selected_rendition_height: Required[Optional[float]]

    selected_rendition_width: Required[Optional[float]]

    sequence: Required[int]

    startup_outcome: Required[Optional[Literal["started", "failed_before_start", "ended_before_start"]]]

    video_id: Required[str]

    view_id: Required[str]

    viewer_id: Required[Optional[str]]

    browser_context: object
    """Optional browser information supplied by the player."""

    delivery_request_count: Optional[float]

    delivery_throughput_bps: Optional[float]

    delivery_transferred_bytes: Optional[float]

    dropped_video_frames: Optional[float]

    first_video_frame_time_ms: Optional[float]

    furthest_progress_ratio: Optional[float]

    maximum_playhead_seconds: float

    media_duration_seconds: Optional[float]

    media_height_px: Optional[float]

    media_width_px: Optional[float]

    playing_time_ms: float

    rebuffer_count: float

    rebuffer_duration_ms: float

    rebuffer_ratio: Optional[float]

    rendition_playing_time: Optional[Iterable[RenditionPlayingTime]]

    rendition_switch_count: Optional[float]

    seek_count: float

    seek_duration_ms: float

    startup_time_ms: Optional[float]

    total_video_frames: Optional[float]

    visibility_state: Optional[Literal["visible", "hidden"]]
    """Tab visibility when the event was recorded.

    Hidden does not imply paused playback or identify the cause of a pause. Missing
    on older events; null when unavailable.
    """
