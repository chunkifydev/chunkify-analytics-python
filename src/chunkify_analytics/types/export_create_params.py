# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .export_query_param import ExportQueryParam

__all__ = ["ExportCreateParams"]


class ExportCreateParams(TypedDict, total=False):
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

    columns: SequenceNotStr[str]
    """CSV column names in output order.

    Omit for all columns. Get the available names from GET /v1/exports using the
    same resource, kind and group_by. Unknown names, duplicates and empty selections
    are rejected.
    """

    query: ExportQueryParam
