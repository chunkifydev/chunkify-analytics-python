# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import timesery_retrieve_params
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
from ..types.timeseries_response import TimeseriesResponse

__all__ = ["TimeseriesResource", "AsyncTimeseriesResource"]


class TimeseriesResource(SyncAPIResource):
    """Private retained-event and view-cohort queries."""

    @cached_property
    def with_raw_response(self) -> TimeseriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#accessing-raw-response-data-eg-headers
        """
        return TimeseriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TimeseriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#with_streaming_response
        """
        return TimeseriesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        from_: Union[str, datetime],
        interval: Literal["hour", "day"],
        to: Union[str, datetime],
        browser_name: str | Omit = omit,
        city: str | Omit = omit,
        continent: Literal["AF", "AN", "AS", "EU", "NA", "OC", "SA"] | Omit = omit,
        country: str | Omit = omit,
        device_type: Literal["desktop", "mobile", "tablet", "unknown"] | Omit = omit,
        kind: Literal["summary", "quality", "engagement"] | Omit = omit,
        os_name: str | Omit = omit,
        page_origin: str | Omit = omit,
        page_path: str | Omit = omit,
        video_id: str | Omit = omit,
        view_id: str | Omit = omit,
        viewer_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeseriesResponse:
        """Supply from, to and interval=hour|day.

        kind defaults to summary and also accepts
        quality or engagement. Every bucket selects first retained starts in its UTC
        interval and includes each selected view's whole retained measurement and
        errors, even after to. Empty buckets have zero counts and null unavailable
        measurements or ratios. At most 1000 buckets. Unique viewer counts are not
        additive.

        Args:
          from_: Inclusive view-start time in RFC3339 format with a timezone.

          interval: UTC hour or day. The requested range can contain at most 1000 buckets.

          to: Exclusive view-start time in RFC3339 format with a timezone. Must be later than
              from.

          browser_name: Exact browser name, such as Chrome. Missing values do not match.

          city: Exact, case-sensitive city name from the local lookup, with 1 to 256 Unicode
              characters. Use country alongside city to distinguish places with the same name.
              Missing locations do not match.

          continent: Exact continent code from the local lookup. Missing locations do not match.

          country: Exact uppercase ISO 3166-1 alpha-2 country code, such as GB. Missing locations
              do not match.

          device_type: Exact device class. unknown matches an explicit unknown value.

          kind: Metric set for every time bucket. Uses the same calculations and sample counts
              as the corresponding totals route.

          os_name: Exact operating-system name, such as macOS. Missing values do not match.

          page_origin: Exact, case-sensitive page origin captured by the player, such as
              https://example.com. Metrics use the first retained view start; raw events use
              each event context. Missing values do not match.

          page_path: Exact, case-sensitive page path captured by the player, such as /watch/video.
              Filter by page_origin as well to distinguish identical paths on different sites.
              Metrics use the first retained view start; raw events use each event context.
              Missing values do not match.

          video_id: Exact video ID. Combined with all other filters using AND.

          view_id: Filter one playback attempt by view ID. Metrics use its first retained start.

          viewer_id: Exact supplied viewer ID. Missing/null viewer IDs do not match.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            TimeseriesResponse,
            self._get(
                "/v1/timeseries",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "from_": from_,
                            "interval": interval,
                            "to": to,
                            "browser_name": browser_name,
                            "city": city,
                            "continent": continent,
                            "country": country,
                            "device_type": device_type,
                            "kind": kind,
                            "os_name": os_name,
                            "page_origin": page_origin,
                            "page_path": page_path,
                            "video_id": video_id,
                            "view_id": view_id,
                            "viewer_id": viewer_id,
                        },
                        timesery_retrieve_params.TimeseryRetrieveParams,
                    ),
                    security={"secret_key": True},
                ),
                cast_to=cast(
                    Any, TimeseriesResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncTimeseriesResource(AsyncAPIResource):
    """Private retained-event and view-cohort queries."""

    @cached_property
    def with_raw_response(self) -> AsyncTimeseriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTimeseriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTimeseriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#with_streaming_response
        """
        return AsyncTimeseriesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        from_: Union[str, datetime],
        interval: Literal["hour", "day"],
        to: Union[str, datetime],
        browser_name: str | Omit = omit,
        city: str | Omit = omit,
        continent: Literal["AF", "AN", "AS", "EU", "NA", "OC", "SA"] | Omit = omit,
        country: str | Omit = omit,
        device_type: Literal["desktop", "mobile", "tablet", "unknown"] | Omit = omit,
        kind: Literal["summary", "quality", "engagement"] | Omit = omit,
        os_name: str | Omit = omit,
        page_origin: str | Omit = omit,
        page_path: str | Omit = omit,
        video_id: str | Omit = omit,
        view_id: str | Omit = omit,
        viewer_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeseriesResponse:
        """Supply from, to and interval=hour|day.

        kind defaults to summary and also accepts
        quality or engagement. Every bucket selects first retained starts in its UTC
        interval and includes each selected view's whole retained measurement and
        errors, even after to. Empty buckets have zero counts and null unavailable
        measurements or ratios. At most 1000 buckets. Unique viewer counts are not
        additive.

        Args:
          from_: Inclusive view-start time in RFC3339 format with a timezone.

          interval: UTC hour or day. The requested range can contain at most 1000 buckets.

          to: Exclusive view-start time in RFC3339 format with a timezone. Must be later than
              from.

          browser_name: Exact browser name, such as Chrome. Missing values do not match.

          city: Exact, case-sensitive city name from the local lookup, with 1 to 256 Unicode
              characters. Use country alongside city to distinguish places with the same name.
              Missing locations do not match.

          continent: Exact continent code from the local lookup. Missing locations do not match.

          country: Exact uppercase ISO 3166-1 alpha-2 country code, such as GB. Missing locations
              do not match.

          device_type: Exact device class. unknown matches an explicit unknown value.

          kind: Metric set for every time bucket. Uses the same calculations and sample counts
              as the corresponding totals route.

          os_name: Exact operating-system name, such as macOS. Missing values do not match.

          page_origin: Exact, case-sensitive page origin captured by the player, such as
              https://example.com. Metrics use the first retained view start; raw events use
              each event context. Missing values do not match.

          page_path: Exact, case-sensitive page path captured by the player, such as /watch/video.
              Filter by page_origin as well to distinguish identical paths on different sites.
              Metrics use the first retained view start; raw events use each event context.
              Missing values do not match.

          video_id: Exact video ID. Combined with all other filters using AND.

          view_id: Filter one playback attempt by view ID. Metrics use its first retained start.

          viewer_id: Exact supplied viewer ID. Missing/null viewer IDs do not match.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            TimeseriesResponse,
            await self._get(
                "/v1/timeseries",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "from_": from_,
                            "interval": interval,
                            "to": to,
                            "browser_name": browser_name,
                            "city": city,
                            "continent": continent,
                            "country": country,
                            "device_type": device_type,
                            "kind": kind,
                            "os_name": os_name,
                            "page_origin": page_origin,
                            "page_path": page_path,
                            "video_id": video_id,
                            "view_id": view_id,
                            "viewer_id": viewer_id,
                        },
                        timesery_retrieve_params.TimeseryRetrieveParams,
                    ),
                    security={"secret_key": True},
                ),
                cast_to=cast(
                    Any, TimeseriesResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class TimeseriesResourceWithRawResponse:
    def __init__(self, timeseries: TimeseriesResource) -> None:
        self._timeseries = timeseries

        self.retrieve = to_raw_response_wrapper(
            timeseries.retrieve,
        )


class AsyncTimeseriesResourceWithRawResponse:
    def __init__(self, timeseries: AsyncTimeseriesResource) -> None:
        self._timeseries = timeseries

        self.retrieve = async_to_raw_response_wrapper(
            timeseries.retrieve,
        )


class TimeseriesResourceWithStreamingResponse:
    def __init__(self, timeseries: TimeseriesResource) -> None:
        self._timeseries = timeseries

        self.retrieve = to_streamed_response_wrapper(
            timeseries.retrieve,
        )


class AsyncTimeseriesResourceWithStreamingResponse:
    def __init__(self, timeseries: AsyncTimeseriesResource) -> None:
        self._timeseries = timeseries

        self.retrieve = async_to_streamed_response_wrapper(
            timeseries.retrieve,
        )
