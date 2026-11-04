# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import error_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncErrorsPage, AsyncErrorsPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.error_group import ErrorGroup

__all__ = ["ErrorsResource", "AsyncErrorsResource"]


class ErrorsResource(SyncAPIResource):
    """Private retained-event and view-cohort queries."""

    @cached_property
    def with_raw_response(self) -> ErrorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#accessing-raw-response-data-eg-headers
        """
        return ErrorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ErrorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#with_streaming_response
        """
        return ErrorsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        browser_name: str | Omit = omit,
        city: str | Omit = omit,
        continent: Literal["AF", "AN", "AS", "EU", "NA", "OC", "SA"] | Omit = omit,
        country: str | Omit = omit,
        cursor: str | Omit = omit,
        device_type: Literal["desktop", "mobile", "tablet", "unknown"] | Omit = omit,
        from_: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        os_name: str | Omit = omit,
        page_origin: str | Omit = omit,
        page_path: str | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        video_id: str | Omit = omit,
        view_id: str | Omit = omit,
        viewer_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncErrorsPage[ErrorGroup]:
        """Filters select first retained starts.

        Error events from the selected view
        identity contribute even after to. Group by exact JSON error_code and fatal
        status, distinguishing numeric codes from text and missing from false. Sort by
        affected_views descending, then canonical JSON code and fatal status ascending
        for ties. error_events counts distinct event IDs per group, affected_views
        counts distinct view IDs. Groups are not additive across codes. Cursors exclude
        later arrivals.

        Args:
          browser_name: Exact browser name, such as Chrome. Missing values do not match.

          city: Exact, case-sensitive city name from the local lookup, with 1 to 256 Unicode
              characters. Use country alongside city to distinguish places with the same name.
              Missing locations do not match.

          continent: Exact continent code from the local lookup. Missing locations do not match.

          country: Exact uppercase ISO 3166-1 alpha-2 country code, such as GB. Missing locations
              do not match.

          cursor: Use next_cursor from the previous page. Keep the same filters, sort_by and
              order. Video cursors from earlier versions are invalid; start a new pagination
              sequence after upgrading.

          device_type: Exact device class. unknown matches an explicit unknown value.

          from_: Inclusive RFC3339 occurrence-time lower bound, with timezone. Summary/video
              queries apply it to the selected view_started event. Must be before to.

          limit: Maximum rows on this page. Events and videos always support pagination; summary,
              quality and engagement support it only with group_by.

          os_name: Exact operating-system name, such as macOS. Missing values do not match.

          page_origin: Exact, case-sensitive page origin captured by the player, such as
              https://example.com. Metrics use the first retained view start; raw events use
              each event context. Missing values do not match.

          page_path: Exact, case-sensitive page path captured by the player, such as /watch/video.
              Filter by page_origin as well to distinguish identical paths on different sites.
              Metrics use the first retained view start; raw events use each event context.
              Missing values do not match.

          to: Exclusive RFC3339 occurrence-time upper bound, with timezone. Summary/video
              queries apply it to the selected view_started event.

          video_id: Exact video ID. Combined with all other filters using AND.

          view_id: Filter one playback attempt by view ID. Metrics use its first retained start.

          viewer_id: Exact supplied viewer ID. Missing/null viewer IDs do not match.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/errors",
            page=SyncErrorsPage[ErrorGroup],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "browser_name": browser_name,
                        "city": city,
                        "continent": continent,
                        "country": country,
                        "cursor": cursor,
                        "device_type": device_type,
                        "from_": from_,
                        "limit": limit,
                        "os_name": os_name,
                        "page_origin": page_origin,
                        "page_path": page_path,
                        "to": to,
                        "video_id": video_id,
                        "view_id": view_id,
                        "viewer_id": viewer_id,
                    },
                    error_list_params.ErrorListParams,
                ),
                security={"secret_key": True},
            ),
            model=ErrorGroup,
        )


class AsyncErrorsResource(AsyncAPIResource):
    """Private retained-event and view-cohort queries."""

    @cached_property
    def with_raw_response(self) -> AsyncErrorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncErrorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncErrorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#with_streaming_response
        """
        return AsyncErrorsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        browser_name: str | Omit = omit,
        city: str | Omit = omit,
        continent: Literal["AF", "AN", "AS", "EU", "NA", "OC", "SA"] | Omit = omit,
        country: str | Omit = omit,
        cursor: str | Omit = omit,
        device_type: Literal["desktop", "mobile", "tablet", "unknown"] | Omit = omit,
        from_: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        os_name: str | Omit = omit,
        page_origin: str | Omit = omit,
        page_path: str | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        video_id: str | Omit = omit,
        view_id: str | Omit = omit,
        viewer_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ErrorGroup, AsyncErrorsPage[ErrorGroup]]:
        """Filters select first retained starts.

        Error events from the selected view
        identity contribute even after to. Group by exact JSON error_code and fatal
        status, distinguishing numeric codes from text and missing from false. Sort by
        affected_views descending, then canonical JSON code and fatal status ascending
        for ties. error_events counts distinct event IDs per group, affected_views
        counts distinct view IDs. Groups are not additive across codes. Cursors exclude
        later arrivals.

        Args:
          browser_name: Exact browser name, such as Chrome. Missing values do not match.

          city: Exact, case-sensitive city name from the local lookup, with 1 to 256 Unicode
              characters. Use country alongside city to distinguish places with the same name.
              Missing locations do not match.

          continent: Exact continent code from the local lookup. Missing locations do not match.

          country: Exact uppercase ISO 3166-1 alpha-2 country code, such as GB. Missing locations
              do not match.

          cursor: Use next_cursor from the previous page. Keep the same filters, sort_by and
              order. Video cursors from earlier versions are invalid; start a new pagination
              sequence after upgrading.

          device_type: Exact device class. unknown matches an explicit unknown value.

          from_: Inclusive RFC3339 occurrence-time lower bound, with timezone. Summary/video
              queries apply it to the selected view_started event. Must be before to.

          limit: Maximum rows on this page. Events and videos always support pagination; summary,
              quality and engagement support it only with group_by.

          os_name: Exact operating-system name, such as macOS. Missing values do not match.

          page_origin: Exact, case-sensitive page origin captured by the player, such as
              https://example.com. Metrics use the first retained view start; raw events use
              each event context. Missing values do not match.

          page_path: Exact, case-sensitive page path captured by the player, such as /watch/video.
              Filter by page_origin as well to distinguish identical paths on different sites.
              Metrics use the first retained view start; raw events use each event context.
              Missing values do not match.

          to: Exclusive RFC3339 occurrence-time upper bound, with timezone. Summary/video
              queries apply it to the selected view_started event.

          video_id: Exact video ID. Combined with all other filters using AND.

          view_id: Filter one playback attempt by view ID. Metrics use its first retained start.

          viewer_id: Exact supplied viewer ID. Missing/null viewer IDs do not match.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/errors",
            page=AsyncErrorsPage[ErrorGroup],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "browser_name": browser_name,
                        "city": city,
                        "continent": continent,
                        "country": country,
                        "cursor": cursor,
                        "device_type": device_type,
                        "from_": from_,
                        "limit": limit,
                        "os_name": os_name,
                        "page_origin": page_origin,
                        "page_path": page_path,
                        "to": to,
                        "video_id": video_id,
                        "view_id": view_id,
                        "viewer_id": viewer_id,
                    },
                    error_list_params.ErrorListParams,
                ),
                security={"secret_key": True},
            ),
            model=ErrorGroup,
        )


class ErrorsResourceWithRawResponse:
    def __init__(self, errors: ErrorsResource) -> None:
        self._errors = errors

        self.list = to_raw_response_wrapper(
            errors.list,
        )


class AsyncErrorsResourceWithRawResponse:
    def __init__(self, errors: AsyncErrorsResource) -> None:
        self._errors = errors

        self.list = async_to_raw_response_wrapper(
            errors.list,
        )


class ErrorsResourceWithStreamingResponse:
    def __init__(self, errors: ErrorsResource) -> None:
        self._errors = errors

        self.list = to_streamed_response_wrapper(
            errors.list,
        )


class AsyncErrorsResourceWithStreamingResponse:
    def __init__(self, errors: AsyncErrorsResource) -> None:
        self._errors = errors

        self.list = async_to_streamed_response_wrapper(
            errors.list,
        )
