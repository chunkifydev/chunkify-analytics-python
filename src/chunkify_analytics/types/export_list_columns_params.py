# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExportListColumnsParams"]


class ExportListColumnsParams(TypedDict, total=False):
    resource: Required[
        Literal[
            "summary",
            "quality",
            "engagement",
            "timeseries",
            "videos",
            "events",
            "views",
            "errors",
            "dimensions",
            "renditions",
            "subtitles",
            "playback_rates",
            "retention",
        ]
    ]
    """Report whose CSV columns to list."""

    group_by: Union[
        Literal[
            "browser_name",
            "os_name",
            "device_type",
            "continent",
            "country",
            "city",
            "page_origin",
            "page_path",
            "subtitle_language",
            "playback_rate",
            "video_title",
            "user_id",
        ],
        str,
    ]
    """Optional on summary, quality and engagement.

    Group views by this field on their first retained start. Missing, null and
    nonstring context forms a null group; the literal device type unknown stays
    separate. Groups sort by views descending, then value ascending with null first
    for ties. Pagination is available only with group_by. Location uses the first
    retained start too. City groups use the stored name; filter by country to avoid
    combining names shared by different countries. Page groups use the first
    retained start even if playback continues after navigation. Filter by
    page_origin when grouping page_path to distinguish identical paths on different
    sites. video_title groups by the title on each view's first retained start, so a
    renamed video counts each view under the title it started with. user_id groups
    by the user ID on each view's first retained start. Use custom.<key>, such as
    custom.plan, to group by a custom dimension; views without the key form the null
    group.
    """

    kind: Literal["summary", "quality", "engagement"]
    """Metric set for every time bucket.

    Uses the same calculations and sample counts as the corresponding totals route.
    """
