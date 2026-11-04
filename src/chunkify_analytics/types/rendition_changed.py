# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.rendition_playing_time import RenditionPlayingTime

__all__ = ["RenditionChanged"]


class RenditionChanged(BaseModel):
    connector_name: str

    connector_version: Optional[str] = None

    delivery_hostname: Optional[str] = None

    environment: Optional[str] = None

    error_category: Optional[Literal["aborted", "network", "decode", "unsupported", "unknown"]] = None

    error_code: Union[str, float, None] = None

    error_fatal: Optional[bool] = None

    error_playhead_seconds: Optional[float] = None

    event_id: str

    event_name: Literal["chunkify.video.rendition_changed"]

    occurred_at: datetime

    player_height_px: Optional[float] = None

    player_name: Optional[str] = None

    player_version: Optional[str] = None

    player_width_px: Optional[float] = None

    playhead_seconds: Optional[float] = None

    previous_rendition_bitrate_bps: Optional[float] = None

    previous_rendition_codec: Optional[str] = None

    previous_rendition_frame_rate: Optional[float] = None

    previous_rendition_height: Optional[float] = None

    previous_rendition_width: Optional[float] = None

    reason: Optional[Literal["ended", "destroyed", "source_changed", "page_exit"]] = None

    schema_version: Literal[1]

    sdk_name: str
    """Name of the SDK or integration that produced the event.

    Informational metadata, preserved as received. Must contain at least one
    non-whitespace character.
    """

    sdk_version: str

    selected_rendition_bitrate_bps: Optional[float] = None

    selected_rendition_codec: Optional[str] = None

    selected_rendition_frame_rate: Optional[float] = None

    selected_rendition_height: Optional[float] = None

    selected_rendition_width: Optional[float] = None

    sequence: int

    startup_outcome: Optional[Literal["started", "failed_before_start", "ended_before_start"]] = None

    video_id: str

    view_id: str

    viewer_id: Optional[str] = None

    browser_context: Optional[object] = None
    """Optional browser information supplied by the player."""

    delivery_request_count: Optional[float] = None

    delivery_throughput_bps: Optional[float] = None

    delivery_transferred_bytes: Optional[float] = None

    dropped_video_frames: Optional[float] = None

    first_video_frame_time_ms: Optional[float] = None

    furthest_progress_ratio: Optional[float] = None

    maximum_playhead_seconds: Optional[float] = None

    media_duration_seconds: Optional[float] = None

    media_height_px: Optional[float] = None

    media_width_px: Optional[float] = None

    playing_time_ms: Optional[float] = None

    rebuffer_count: Optional[float] = None

    rebuffer_duration_ms: Optional[float] = None

    rebuffer_ratio: Optional[float] = None

    rendition_playing_time: Optional[List[RenditionPlayingTime]] = None

    rendition_switch_count: Optional[float] = None

    seek_count: Optional[float] = None

    seek_duration_ms: Optional[float] = None

    startup_time_ms: Optional[float] = None

    total_video_frames: Optional[float] = None

    visibility_state: Optional[Literal["visible", "hidden"]] = None
    """Tab visibility when the event was recorded.

    Hidden does not imply paused playback or identify the cause of a pause. Missing
    on older events; null when unavailable.
    """
