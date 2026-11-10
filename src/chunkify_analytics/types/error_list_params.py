# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ErrorListParams"]


class ErrorListParams(TypedDict, total=False):
    browser_name: str
    """Exact browser name, such as Chrome. Missing values do not match."""

    city: str
    """
    Exact, case-sensitive city name from the local lookup, with 1 to 256 Unicode
    characters. Use country alongside city to distinguish places with the same name.
    Missing locations do not match.
    """

    continent: Literal["AF", "AN", "AS", "EU", "NA", "OC", "SA"]
    """Exact continent code from the local lookup. Missing locations do not match."""

    country: str
    """Exact uppercase ISO 3166-1 alpha-2 country code, such as GB.

    Missing locations do not match.
    """

    cursor: str
    """Use next_cursor from the previous page.

    Keep the same filters, sort_by and order. Video cursors from earlier versions
    are invalid; start a new pagination sequence after upgrading.
    """

    device_type: Literal["desktop", "mobile", "tablet", "unknown"]
    """Exact device class. unknown matches an explicit unknown value."""

    from_: Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]
    """Inclusive RFC3339 occurrence-time lower bound, with timezone.

    Summary/video queries apply it to the selected view_started event. Must be
    before to.
    """

    limit: int
    """Maximum rows on this page.

    Events and videos always support pagination; summary, quality and engagement
    support it only with group_by.
    """

    os_name: str
    """Exact operating-system name, such as macOS. Missing values do not match."""

    page_origin: str
    """
    Exact, case-sensitive page origin captured by the player, such as
    https://example.com. Metrics use the first retained view start; raw events use
    each event context. Missing values do not match.
    """

    page_path: str
    """Exact, case-sensitive page path captured by the player, such as /watch/video.

    Filter by page_origin as well to distinguish identical paths on different sites.
    Metrics use the first retained view start; raw events use each event context.
    Missing values do not match.
    """

    playback_rate: str
    """
    Playback rate from 0.01 to 16 with at most two decimals, such as 1, 1.5 or 2;
    2.0 and 2 are the same rate. Metrics use the rate on the first retained view
    start; raw events use each event's value.
    """

    subtitle_language: str
    """
    Exact, case-sensitive, non-blank subtitle language tag, such as fr or en-US; und
    for a subtitles track without a language. Metrics use the language showing on
    the first retained view start; raw events use each event's value. Views without
    subtitles at start do not match.
    """

    to: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Exclusive RFC3339 occurrence-time upper bound, with timezone.

    Summary/video queries apply it to the selected view_started event.
    """

    user_id: str
    """Exact integrator-supplied user ID.

    Selects views by their start event; event lists match each event's own value.
    Missing/null user IDs do not match. Reports with this filter read one stored row
    per view.
    """

    video_id: str
    """Exact video ID; must not be blank. Combined with all other filters using AND."""

    video_title: str
    """Exact, case-sensitive video title.

    Selects views by the title on their first retained start; event lists match each
    event's own value. Views without a title do not match. Reports with this filter
    read one stored row per view.
    """

    view_id: str
    """Filter one playback attempt by view ID. Metrics use its first retained start."""

    viewer_id: str
    """Exact viewer ID.

    The Chunkify player SDK generates one per browser; missing/null viewer IDs do
    not match.
    """
