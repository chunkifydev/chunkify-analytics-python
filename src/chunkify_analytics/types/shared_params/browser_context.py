# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BrowserContext"]


class BrowserContext(TypedDict, total=False):
    """Browser and device information.

    The Chunkify player sends every field, with null for unavailable measurements. Other integrations may omit any field except schema_version. Extra properties are preserved.
    """

    schema_version: Required[Literal[1]]

    browser_name: Optional[str]

    browser_version: Optional[str]

    device_family: Optional[str]

    device_type: Literal["desktop", "mobile", "tablet", "unknown"]

    language: Optional[str]

    language_prefix: Optional[str]

    os_name: Optional[str]

    os_version: Optional[str]

    page_origin: Optional[str]
    """Current document HTTP(S) origin, without credentials.

    Null when unavailable or longer than 2048 characters.
    """

    page_path: Optional[str]
    """Current document pathname, without query parameters or fragment.

    Null when unavailable or longer than 2048 characters. Paths may contain
    application-defined identifiers.
    """

    pixel_ratio: Optional[float]

    screen_height_px: Optional[int]

    screen_width_px: Optional[int]

    timezone: Optional[str]

    timezone_offset_minutes: Optional[int]

    user_agent: Optional[str]

    viewport_height_px: Optional[int]

    viewport_width_px: Optional[int]
