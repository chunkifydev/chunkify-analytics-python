# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["StoredOtlpContext", "ResourceLogs", "ScopeLogs"]


class ResourceLogs(BaseModel):
    """Original resource group excluding scopeLogs."""

    resource: Optional["OtlpResource"] = None

    schema_url: Optional[str] = FieldInfo(alias="schemaUrl", default=None)


class ScopeLogs(BaseModel):
    """Original scope group excluding logRecords."""

    schema_url: Optional[str] = FieldInfo(alias="schemaUrl", default=None)

    scope: Optional["OtlpScope"] = None


class StoredOtlpContext(BaseModel):
    """
    Legacy context present for an event received through OTLP by an earlier collector version. Existing context remains readable; new ingestion accepts native JSON events only.
    """

    log_record: "OtlpLogRecord"
    """A playback event in log attributes.

    Duplicate attributes and invalid event fields reject the request.
    """

    resource_logs: ResourceLogs
    """Original resource group excluding scopeLogs."""

    scope_logs: ScopeLogs
    """Original scope group excluding logRecords."""


from .otlp_scope import OtlpScope
from .otlp_resource import OtlpResource
from .otlp_log_record import OtlpLogRecord
