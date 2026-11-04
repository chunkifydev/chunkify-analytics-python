# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ViewRetrieveParams"]


class ViewRetrieveParams(TypedDict, total=False):
    cursor: str
    """Use next_cursor from the previous page.

    Keep the same filters, sort_by and order. Video cursors from earlier versions
    are invalid; start a new pagination sequence after upgrading.
    """

    limit: int
    """Maximum rows on this page.

    Events and videos always support pagination; summary, quality and engagement
    support it only with group_by.
    """
