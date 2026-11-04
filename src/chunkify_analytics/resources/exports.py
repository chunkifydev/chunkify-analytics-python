# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import export_create_params, export_list_columns_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.export import Export
from ..types.export_columns import ExportColumns
from ..types.export_query_param import ExportQueryParam

__all__ = ["ExportsResource", "AsyncExportsResource"]


class ExportsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#accessing-raw-response-data-eg-headers
        """
        return ExportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#with_streaming_response
        """
        return ExportsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        resource: Literal[
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
            "retention",
        ],
        columns: SequenceNotStr[str] | Omit = omit,
        query: ExportQueryParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Export:
        """Create a scoped 256-bit random download token for all matching rows.

        Requires a
        project private key; read-only keys are allowed. The link expires after 30
        minutes and is invalidated by issuer-key rotation/revocation, project deletion
        or collector restart. No CSV is generated or retained at creation. limit/cursor
        are rejected. Existing query endpoints continue returning JSON. Event CSV files
        contain documented scalar event fields and flat context.\\** columns. Custom
        attributes, nested arrays and historical OTLP payloads are excluded. CSV cells
        never contain JSON objects or arrays; use GET /v1/events for original payloads.

        Args:
          columns: CSV column names in output order. Omit for all columns. Get the available names
              from GET /v1/exports using the same resource, kind and group_by. Unknown names,
              duplicates and empty selections are rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/exports",
            body=maybe_transform(
                {
                    "resource": resource,
                    "columns": columns,
                    "query": query,
                },
                export_create_params.ExportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"secret_key": True},
            ),
            cast_to=Export,
        )

    def download(
        self,
        token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """The token authorizes only its saved project and query.

        Requires no Authorization
        header and accepts no query parameters. Generate CSV on demand from one read
        snapshot on a dedicated connection; stream with bounded application buffers and
        backpressure. Dataset is selected when the link is opened. Rows are not capped
        by query pagination. Nested metric columns use slash-separated paths. Events
        have documented scalar columns and flat context.\\** columns. Custom attributes,
        nested arrays and historical OTLP payloads are excluded. CSV cells never contain
        JSON objects or arrays. Nulls are empty cells; spreadsheet-formula strings are
        prefixed with an apostrophe. Interrupted or failed downloads terminate the
        stream; retry the full download. No files are retained. Defaults: 2 download
        starts/minute per project with burst capacity 2, one active CSV generation per
        project and four server-wide. Limits are shared across keys and links. Excess
        requests receive 429 with Retry-After instead of queueing. Override limits in
        config.toml [rate_limits]. Link expiry is checked before starting, not during an
        active download. S3 retention/deletion can remove source objects during a
        download.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        extra_headers = {"Accept": "text/csv", **(extra_headers or {})}
        return self._get(
            path_template("/v1/exports/{token}", token=token),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=str,
        )

    def list_columns(
        self,
        *,
        resource: Literal[
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
            "retention",
        ],
        group_by: Literal[
            "browser_name", "os_name", "device_type", "continent", "country", "city", "page_origin", "page_path"
        ]
        | Omit = omit,
        kind: Literal["summary", "quality", "engagement"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExportColumns:
        """Discover column names before creating an export.

        Requires a project private key;
        read-only keys are allowed. kind applies only to timeseries. group_by applies to
        summary, quality and engagement. Date ranges and filters do not change the
        columns.

        Args:
          resource: Report whose CSV columns to list.

          group_by: Optional on summary, quality and engagement. Group views by this field on their
              first retained start. Missing, null and nonstring context forms a null group;
              the literal device type unknown stays separate. Groups sort by views descending,
              then value ascending with null first for ties. Pagination is available only with
              group_by. Location uses the first retained start too. City groups use the stored
              name; filter by country to avoid combining names shared by different countries.
              Page groups use the first retained start even if playback continues after
              navigation. Filter by page_origin when grouping page_path to distinguish
              identical paths on different sites.

          kind: Metric set for every time bucket. Uses the same calculations and sample counts
              as the corresponding totals route.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/exports",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "resource": resource,
                        "group_by": group_by,
                        "kind": kind,
                    },
                    export_list_columns_params.ExportListColumnsParams,
                ),
                security={"secret_key": True},
            ),
            cast_to=ExportColumns,
        )


class AsyncExportsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#with_streaming_response
        """
        return AsyncExportsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        resource: Literal[
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
            "retention",
        ],
        columns: SequenceNotStr[str] | Omit = omit,
        query: ExportQueryParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Export:
        """Create a scoped 256-bit random download token for all matching rows.

        Requires a
        project private key; read-only keys are allowed. The link expires after 30
        minutes and is invalidated by issuer-key rotation/revocation, project deletion
        or collector restart. No CSV is generated or retained at creation. limit/cursor
        are rejected. Existing query endpoints continue returning JSON. Event CSV files
        contain documented scalar event fields and flat context.\\** columns. Custom
        attributes, nested arrays and historical OTLP payloads are excluded. CSV cells
        never contain JSON objects or arrays; use GET /v1/events for original payloads.

        Args:
          columns: CSV column names in output order. Omit for all columns. Get the available names
              from GET /v1/exports using the same resource, kind and group_by. Unknown names,
              duplicates and empty selections are rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/exports",
            body=await async_maybe_transform(
                {
                    "resource": resource,
                    "columns": columns,
                    "query": query,
                },
                export_create_params.ExportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"secret_key": True},
            ),
            cast_to=Export,
        )

    async def download(
        self,
        token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """The token authorizes only its saved project and query.

        Requires no Authorization
        header and accepts no query parameters. Generate CSV on demand from one read
        snapshot on a dedicated connection; stream with bounded application buffers and
        backpressure. Dataset is selected when the link is opened. Rows are not capped
        by query pagination. Nested metric columns use slash-separated paths. Events
        have documented scalar columns and flat context.\\** columns. Custom attributes,
        nested arrays and historical OTLP payloads are excluded. CSV cells never contain
        JSON objects or arrays. Nulls are empty cells; spreadsheet-formula strings are
        prefixed with an apostrophe. Interrupted or failed downloads terminate the
        stream; retry the full download. No files are retained. Defaults: 2 download
        starts/minute per project with burst capacity 2, one active CSV generation per
        project and four server-wide. Limits are shared across keys and links. Excess
        requests receive 429 with Retry-After instead of queueing. Override limits in
        config.toml [rate_limits]. Link expiry is checked before starting, not during an
        active download. S3 retention/deletion can remove source objects during a
        download.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        extra_headers = {"Accept": "text/csv", **(extra_headers or {})}
        return await self._get(
            path_template("/v1/exports/{token}", token=token),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=str,
        )

    async def list_columns(
        self,
        *,
        resource: Literal[
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
            "retention",
        ],
        group_by: Literal[
            "browser_name", "os_name", "device_type", "continent", "country", "city", "page_origin", "page_path"
        ]
        | Omit = omit,
        kind: Literal["summary", "quality", "engagement"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExportColumns:
        """Discover column names before creating an export.

        Requires a project private key;
        read-only keys are allowed. kind applies only to timeseries. group_by applies to
        summary, quality and engagement. Date ranges and filters do not change the
        columns.

        Args:
          resource: Report whose CSV columns to list.

          group_by: Optional on summary, quality and engagement. Group views by this field on their
              first retained start. Missing, null and nonstring context forms a null group;
              the literal device type unknown stays separate. Groups sort by views descending,
              then value ascending with null first for ties. Pagination is available only with
              group_by. Location uses the first retained start too. City groups use the stored
              name; filter by country to avoid combining names shared by different countries.
              Page groups use the first retained start even if playback continues after
              navigation. Filter by page_origin when grouping page_path to distinguish
              identical paths on different sites.

          kind: Metric set for every time bucket. Uses the same calculations and sample counts
              as the corresponding totals route.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/exports",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "resource": resource,
                        "group_by": group_by,
                        "kind": kind,
                    },
                    export_list_columns_params.ExportListColumnsParams,
                ),
                security={"secret_key": True},
            ),
            cast_to=ExportColumns,
        )


class ExportsResourceWithRawResponse:
    def __init__(self, exports: ExportsResource) -> None:
        self._exports = exports

        self.create = to_raw_response_wrapper(
            exports.create,
        )
        self.download = to_raw_response_wrapper(
            exports.download,
        )
        self.list_columns = to_raw_response_wrapper(
            exports.list_columns,
        )


class AsyncExportsResourceWithRawResponse:
    def __init__(self, exports: AsyncExportsResource) -> None:
        self._exports = exports

        self.create = async_to_raw_response_wrapper(
            exports.create,
        )
        self.download = async_to_raw_response_wrapper(
            exports.download,
        )
        self.list_columns = async_to_raw_response_wrapper(
            exports.list_columns,
        )


class ExportsResourceWithStreamingResponse:
    def __init__(self, exports: ExportsResource) -> None:
        self._exports = exports

        self.create = to_streamed_response_wrapper(
            exports.create,
        )
        self.download = to_streamed_response_wrapper(
            exports.download,
        )
        self.list_columns = to_streamed_response_wrapper(
            exports.list_columns,
        )


class AsyncExportsResourceWithStreamingResponse:
    def __init__(self, exports: AsyncExportsResource) -> None:
        self._exports = exports

        self.create = async_to_streamed_response_wrapper(
            exports.create,
        )
        self.download = async_to_streamed_response_wrapper(
            exports.download,
        )
        self.list_columns = async_to_streamed_response_wrapper(
            exports.list_columns,
        )
