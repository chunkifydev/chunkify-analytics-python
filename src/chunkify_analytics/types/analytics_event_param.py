# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .view_ended_param import ViewEndedParam
from .view_started_param import ViewStartedParam
from .view_snapshot_param import ViewSnapshotParam
from .playback_error_param import PlaybackErrorParam
from .seek_completed_param import SeekCompletedParam
from .subtitle_changed_param import SubtitleChangedParam
from .rendition_changed_param import RenditionChangedParam
from .playback_rate_changed_param import PlaybackRateChangedParam
from .playback_state_changed_param import PlaybackStateChangedParam

__all__ = ["AnalyticsEventParam"]

AnalyticsEventParam: TypeAlias = Union[
    ViewStartedParam,
    ViewSnapshotParam,
    PlaybackErrorParam,
    ViewEndedParam,
    PlaybackStateChangedParam,
    RenditionChangedParam,
    SeekCompletedParam,
    SubtitleChangedParam,
    PlaybackRateChangedParam,
]
