# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TimeseryRetrieveParams"]


class TimeseryRetrieveParams(TypedDict, total=False):
    from_: Required[Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]]
    """Inclusive view-start time in RFC3339 format with a timezone."""

    interval: Required[Literal["hour", "day"]]
    """UTC hour or day. The requested range can contain at most 1000 buckets."""

    to: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Exclusive view-start time in RFC3339 format with a timezone.

    Must be later than from.
    """

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

    device_type: Literal["desktop", "mobile", "tablet", "unknown"]
    """Exact device class. unknown matches an explicit unknown value."""

    kind: Literal["summary", "quality", "engagement"]
    """Metric set for every time bucket.

    Uses the same calculations and sample counts as the corresponding totals route.
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

    video_id: str
    """Exact video ID. Combined with all other filters using AND."""

    view_id: str
    """Filter one playback attempt by view ID. Metrics use its first retained start."""

    viewer_id: str
    """Exact supplied viewer ID. Missing/null viewer IDs do not match."""
