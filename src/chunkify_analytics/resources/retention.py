# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import retention_retrieve_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.retention_report import RetentionReport

__all__ = ["RetentionResource", "AsyncRetentionResource"]


class RetentionResource(SyncAPIResource):
    """Private retained-event and view-cohort queries."""

    @cached_property
    def with_raw_response(self) -> RetentionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#accessing-raw-response-data-eg-headers
        """
        return RetentionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RetentionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#with_streaming_response
        """
        return RetentionResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        video_id: str,
        browser_name: str | Omit = omit,
        city: str | Omit = omit,
        continent: Literal["AF", "AN", "AS", "EU", "NA", "OC", "SA"] | Omit = omit,
        country: str | Omit = omit,
        device_type: Literal["desktop", "mobile", "tablet", "unknown"] | Omit = omit,
        from_: Union[str, datetime] | Omit = omit,
        os_name: str | Omit = omit,
        page_origin: str | Omit = omit,
        page_path: str | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        view_id: str | Omit = omit,
        viewer_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RetentionReport:
        """Count views along the video using recorded played ranges.

        Requires video_id.
        Uses the final measurement, or the latest snapshot without an end event, for
        each retained start matching the date and audience filters. Each attempt counts
        once in each section it overlapped, including replays. Skipped sections do not
        count. Older events without played ranges and attempts without a finite positive
        duration are excluded from sample_views. Returns at most 200 consecutive
        buckets, including zero counts, at a width of at least one second. This is media
        position, not wall-clock time.

        Args:
          video_id: Video to report. Retention measures one video at a time.

          browser_name: Exact browser name, such as Chrome. Missing values do not match.

          city: Exact, case-sensitive city name from the local lookup, with 1 to 256 Unicode
              characters. Use country alongside city to distinguish places with the same name.
              Missing locations do not match.

          continent: Exact continent code from the local lookup. Missing locations do not match.

          country: Exact uppercase ISO 3166-1 alpha-2 country code, such as GB. Missing locations
              do not match.

          device_type: Exact device class. unknown matches an explicit unknown value.

          from_: Inclusive RFC3339 occurrence-time lower bound, with timezone. Summary/video
              queries apply it to the selected view_started event. Must be before to.

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

          view_id: Filter one playback attempt by view ID. Metrics use its first retained start.

          viewer_id: Exact supplied viewer ID. Missing/null viewer IDs do not match.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/retention",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "video_id": video_id,
                        "browser_name": browser_name,
                        "city": city,
                        "continent": continent,
                        "country": country,
                        "device_type": device_type,
                        "from_": from_,
                        "os_name": os_name,
                        "page_origin": page_origin,
                        "page_path": page_path,
                        "to": to,
                        "view_id": view_id,
                        "viewer_id": viewer_id,
                    },
                    retention_retrieve_params.RetentionRetrieveParams,
                ),
                security={"secret_key": True},
            ),
            cast_to=RetentionReport,
        )


class AsyncRetentionResource(AsyncAPIResource):
    """Private retained-event and view-cohort queries."""

    @cached_property
    def with_raw_response(self) -> AsyncRetentionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRetentionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRetentionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#with_streaming_response
        """
        return AsyncRetentionResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        video_id: str,
        browser_name: str | Omit = omit,
        city: str | Omit = omit,
        continent: Literal["AF", "AN", "AS", "EU", "NA", "OC", "SA"] | Omit = omit,
        country: str | Omit = omit,
        device_type: Literal["desktop", "mobile", "tablet", "unknown"] | Omit = omit,
        from_: Union[str, datetime] | Omit = omit,
        os_name: str | Omit = omit,
        page_origin: str | Omit = omit,
        page_path: str | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        view_id: str | Omit = omit,
        viewer_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RetentionReport:
        """Count views along the video using recorded played ranges.

        Requires video_id.
        Uses the final measurement, or the latest snapshot without an end event, for
        each retained start matching the date and audience filters. Each attempt counts
        once in each section it overlapped, including replays. Skipped sections do not
        count. Older events without played ranges and attempts without a finite positive
        duration are excluded from sample_views. Returns at most 200 consecutive
        buckets, including zero counts, at a width of at least one second. This is media
        position, not wall-clock time.

        Args:
          video_id: Video to report. Retention measures one video at a time.

          browser_name: Exact browser name, such as Chrome. Missing values do not match.

          city: Exact, case-sensitive city name from the local lookup, with 1 to 256 Unicode
              characters. Use country alongside city to distinguish places with the same name.
              Missing locations do not match.

          continent: Exact continent code from the local lookup. Missing locations do not match.

          country: Exact uppercase ISO 3166-1 alpha-2 country code, such as GB. Missing locations
              do not match.

          device_type: Exact device class. unknown matches an explicit unknown value.

          from_: Inclusive RFC3339 occurrence-time lower bound, with timezone. Summary/video
              queries apply it to the selected view_started event. Must be before to.

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

          view_id: Filter one playback attempt by view ID. Metrics use its first retained start.

          viewer_id: Exact supplied viewer ID. Missing/null viewer IDs do not match.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/retention",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "video_id": video_id,
                        "browser_name": browser_name,
                        "city": city,
                        "continent": continent,
                        "country": country,
                        "device_type": device_type,
                        "from_": from_,
                        "os_name": os_name,
                        "page_origin": page_origin,
                        "page_path": page_path,
                        "to": to,
                        "view_id": view_id,
                        "viewer_id": viewer_id,
                    },
                    retention_retrieve_params.RetentionRetrieveParams,
                ),
                security={"secret_key": True},
            ),
            cast_to=RetentionReport,
        )


class RetentionResourceWithRawResponse:
    def __init__(self, retention: RetentionResource) -> None:
        self._retention = retention

        self.retrieve = to_raw_response_wrapper(
            retention.retrieve,
        )


class AsyncRetentionResourceWithRawResponse:
    def __init__(self, retention: AsyncRetentionResource) -> None:
        self._retention = retention

        self.retrieve = async_to_raw_response_wrapper(
            retention.retrieve,
        )


class RetentionResourceWithStreamingResponse:
    def __init__(self, retention: RetentionResource) -> None:
        self._retention = retention

        self.retrieve = to_streamed_response_wrapper(
            retention.retrieve,
        )


class AsyncRetentionResourceWithStreamingResponse:
    def __init__(self, retention: AsyncRetentionResource) -> None:
        self._retention = retention

        self.retrieve = async_to_streamed_response_wrapper(
            retention.retrieve,
        )
