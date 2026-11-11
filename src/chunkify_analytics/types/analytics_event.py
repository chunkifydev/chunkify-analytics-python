# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .view_ended import ViewEnded
from .view_started import ViewStarted
from .view_snapshot import ViewSnapshot
from .playback_error import PlaybackError
from .seek_completed import SeekCompleted
from .subtitle_changed import SubtitleChanged
from .rendition_changed import RenditionChanged
from .playback_rate_changed import PlaybackRateChanged
from .playback_state_changed import PlaybackStateChanged

__all__ = ["AnalyticsEvent"]

AnalyticsEvent: TypeAlias = Annotated[
    Union[
        ViewStarted,
        ViewSnapshot,
        PlaybackError,
        ViewEnded,
        PlaybackStateChanged,
        RenditionChanged,
        SeekCompleted,
        SubtitleChanged,
        PlaybackRateChanged,
    ],
    PropertyInfo(discriminator="event_name"),
]
