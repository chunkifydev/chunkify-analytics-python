# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .played_range import PlayedRange
from .subtitle_playing_time import SubtitlePlayingTime
from .rendition_playing_time import RenditionPlayingTime
from .playback_rate_playing_time import PlaybackRatePlayingTime

__all__ = ["ViewMetrics"]


class ViewMetrics(BaseModel):
    delivery_request_count: Optional[float] = None

    delivery_throughput_bps: Optional[float] = None

    delivery_transferred_bytes: Optional[float] = None

    dropped_video_frames: Optional[float] = None

    first_video_frame_time_ms: Optional[float] = None

    furthest_progress_ratio: Optional[float] = None

    maximum_playhead_seconds: float

    media_duration_seconds: Optional[float] = None

    media_height_px: Optional[float] = None

    media_width_px: Optional[float] = None

    player_height_px: Optional[float] = None

    player_width_px: Optional[float] = None

    playing_time_ms: float

    rebuffer_count: float

    rebuffer_duration_ms: float

    rebuffer_ratio: Optional[float] = None

    rendition_playing_time: Optional[List[RenditionPlayingTime]] = None

    rendition_switch_count: Optional[float] = None

    seek_count: float

    seek_duration_ms: float

    selected_rendition_bitrate_bps: Optional[float] = None

    selected_rendition_codec: Optional[str] = None

    selected_rendition_height: Optional[float] = None

    selected_rendition_width: Optional[float] = None

    startup_time_ms: Optional[float] = None

    total_video_frames: Optional[float] = None

    playback_rate: Optional[float] = None
    """
    Current playback rate, rounded to two decimals, such as 1, 1.5 or 2; from 0.01
    to 16. Optional.
    """

    playback_rate_playing_time: Optional[List[PlaybackRatePlayingTime]] = None
    """Cumulative playing time per playback rate for this attempt.

    At most 32 entries. Optional.
    """

    played_ranges: Optional[List[PlayedRange]] = None
    """
    Cumulative played media ranges for this attempt, sorted and merged without
    overlaps. Seeking, pauses and buffering are excluded. Missing or null means
    unavailable; an empty array means measured but no section played. Replaying a
    section does not add another range.
    """

    playhead_seconds: Optional[float] = None
    """Current media position at this event, not the maximum reached."""

    subtitle_language: Optional[str] = None
    """
    Language tag (BCP 47) of the showing subtitles or captions track; und when the
    track declares no language; null when subtitles are off. Optional.
    """

    subtitle_playing_time: Optional[List[SubtitlePlayingTime]] = None
    """
    Cumulative playing time per subtitle language for this attempt, null language
    meaning subtitles off. At most 32 entries. Optional.
    """
