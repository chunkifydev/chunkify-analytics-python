# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["KeyCreateParams"]


class KeyCreateParams(TypedDict, total=False):
    name: Required[str]
    """Key display name, up to 128 UTF-8 bytes. Whitespace-only names are rejected."""

    permission: Required[Literal["public", "secret"]]

    read_only: bool
    """Only secret keys can be read-only.

    False grants full project management access to secret keys; public keys only
    ingest events.
    """
