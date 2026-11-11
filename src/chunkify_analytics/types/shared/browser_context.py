# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BrowserContext"]


class BrowserContext(BaseModel):
    """Browser and device information.

    The Chunkify player sends every field, with null for unavailable measurements. Other integrations may omit any field except schema_version. Extra properties are preserved.
    """

    schema_version: Literal[1]

    browser_name: Optional[str] = None

    browser_version: Optional[str] = None

    device_family: Optional[str] = None

    device_type: Optional[Literal["desktop", "mobile", "tablet", "unknown"]] = None

    language: Optional[str] = None

    language_prefix: Optional[str] = None

    os_name: Optional[str] = None

    os_version: Optional[str] = None

    page_origin: Optional[str] = None
    """Current document HTTP(S) origin, without credentials.

    Null when unavailable or longer than 2048 characters.
    """

    page_path: Optional[str] = None
    """Current document pathname, without query parameters or fragment.

    Null when unavailable or longer than 2048 characters. Paths may contain
    application-defined identifiers.
    """

    pixel_ratio: Optional[float] = None

    screen_height_px: Optional[int] = None

    screen_width_px: Optional[int] = None

    timezone: Optional[str] = None

    timezone_offset_minutes: Optional[int] = None

    user_agent: Optional[str] = None

    viewport_height_px: Optional[int] = None

    viewport_width_px: Optional[int] = None
