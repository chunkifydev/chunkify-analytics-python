# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["EventContext"]


class EventContext(BaseModel):
    """Browser context and locally derived continent/country/city.

    Request IP addresses are never added to events or stored context.
    """

    schema_version: Literal[1]

    browser_name: Union[str, float, bool, None] = None
    """Copied from browser_context.browser_name when primitive.

    See BrowserContext for the SDK type; the collector currently accepts any
    primitive here.
    """

    browser_version: Union[str, float, bool, None] = None
    """Copied from browser_context.browser_version when primitive.

    See BrowserContext for the SDK type; the collector currently accepts any
    primitive here.
    """

    city: Optional[str] = None
    """Approximate city name in English from the local City MMDB lookup.

    Null when unknown. Location displays using the bundled DB-IP data must link to
    https://db-ip.com.
    """

    continent: Optional[Literal["AF", "AN", "AS", "EU", "NA", "OC", "SA"]] = None
    """
    Continent code from the local City MMDB lookup: Africa, Antarctica, Asia,
    Europe, North America, Oceania or South America. Null when unknown.
    """

    country: Optional[str] = None
    """Country ISO 3166-1 alpha-2 code from the local City MMDB lookup.

    Null when unknown. The request IP is discarded.
    """

    device_family: Union[str, float, bool, None] = None
    """Copied from browser_context.device_family when primitive.

    See BrowserContext for the SDK type; the collector currently accepts any
    primitive here.
    """

    device_type: Union[str, float, bool, None] = None
    """Copied from browser_context.device_type when primitive.

    See BrowserContext for the SDK type; the collector currently accepts any
    primitive here.
    """

    language: Union[str, float, bool, None] = None
    """Copied from browser_context.language when primitive.

    See BrowserContext for the SDK type; the collector currently accepts any
    primitive here.
    """

    language_prefix: Union[str, float, bool, None] = None
    """Copied from browser_context.language_prefix when primitive.

    See BrowserContext for the SDK type; the collector currently accepts any
    primitive here.
    """

    os_name: Union[str, float, bool, None] = None
    """Copied from browser_context.os_name when primitive.

    See BrowserContext for the SDK type; the collector currently accepts any
    primitive here.
    """

    os_version: Union[str, float, bool, None] = None
    """Copied from browser_context.os_version when primitive.

    See BrowserContext for the SDK type; the collector currently accepts any
    primitive here.
    """

    page_origin: Optional[str] = None
    """Current document HTTP(S) origin, without credentials.

    Null when unavailable or longer than 2048 characters.
    """

    page_path: Optional[str] = None
    """Current document pathname, without query parameters or fragment.

    Null when unavailable or longer than 2048 characters. Paths may contain
    application-defined identifiers.
    """

    pixel_ratio: Union[str, float, bool, None] = None
    """Copied from browser_context.pixel_ratio when primitive.

    See BrowserContext for the SDK type; the collector currently accepts any
    primitive here.
    """

    screen_height_px: Union[str, float, bool, None] = None
    """Copied from browser_context.screen_height_px when primitive.

    See BrowserContext for the SDK type; the collector currently accepts any
    primitive here.
    """

    screen_width_px: Union[str, float, bool, None] = None
    """Copied from browser_context.screen_width_px when primitive.

    See BrowserContext for the SDK type; the collector currently accepts any
    primitive here.
    """

    timezone: Union[str, float, bool, None] = None
    """Copied from browser_context.timezone when primitive.

    See BrowserContext for the SDK type; the collector currently accepts any
    primitive here.
    """

    timezone_offset_minutes: Union[str, float, bool, None] = None
    """Copied from browser_context.timezone_offset_minutes when primitive.

    See BrowserContext for the SDK type; the collector currently accepts any
    primitive here.
    """

    user_agent: Union[str, float, bool, None] = None
    """Copied from browser_context.user_agent when primitive.

    See BrowserContext for the SDK type; the collector currently accepts any
    primitive here.
    """

    viewport_height_px: Union[str, float, bool, None] = None
    """Copied from browser_context.viewport_height_px when primitive.

    See BrowserContext for the SDK type; the collector currently accepts any
    primitive here.
    """

    viewport_width_px: Union[str, float, bool, None] = None
    """Copied from browser_context.viewport_width_px when primitive.

    See BrowserContext for the SDK type; the collector currently accepts any
    primitive here.
    """
