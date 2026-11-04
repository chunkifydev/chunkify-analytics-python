# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import video_list_params
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
from ..pagination import SyncVideosPage, AsyncVideosPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.video_metrics import VideoMetrics

__all__ = ["VideosResource", "AsyncVideosResource"]


class VideosResource(SyncAPIResource):
    """Private retained-event and view-cohort queries."""

    @cached_property
    def with_raw_response(self) -> VideosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#accessing-raw-response-data-eg-headers
        """
        return VideosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VideosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#with_streaming_response
        """
        return VideosResourceWithStreamingResponse(self)

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
        order: Literal["asc", "desc"] | Omit = omit,
        os_name: str | Omit = omit,
        page_origin: str | Omit = omit,
        page_path: str | Omit = omit,
        sort_by: Literal["video_id", "views", "unique_viewers", "total_playing_time_ms", "playback_score"]
        | Omit = omit,
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
    ) -> SyncVideosPage[VideoMetrics]:
        """List per-video totals.

        Sort the entire filtered cohort by video_id, views,
        unique_viewers, total_playing_time_ms or playback_score before pagination.
        Defaults to video_id ascending. Missing scores come last; metric ties use
        video_id ascending in both directions. Unique viewer counts cannot be added
        across videos. Keep sort_by, order and filters unchanged with a cursor.

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

          order: Sort direction. Events and videos default to asc; views default to desc. Events
              sort by ingestion sequence. Videos and views sort by sort_by with missing values
              last. View ties use view_id in the requested direction; video metric ties use
              video_id ascending.

          os_name: Exact operating-system name, such as macOS. Missing values do not match.

          page_origin: Exact, case-sensitive page origin captured by the player, such as
              https://example.com. Metrics use the first retained view start; raw events use
              each event context. Missing values do not match.

          page_path: Exact, case-sensitive page path captured by the player, such as /watch/video.
              Filter by page_origin as well to distinguish identical paths on different sites.
              Metrics use the first retained view start; raw events use each event context.
              Missing values do not match.

          sort_by: Rank all matching videos before pagination. Missing scores come last in both
              directions. Metric ties use video_id ascending. Keep sort_by, order and filters
              unchanged with a cursor.

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
            "/v1/videos",
            page=SyncVideosPage[VideoMetrics],
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
                        "order": order,
                        "os_name": os_name,
                        "page_origin": page_origin,
                        "page_path": page_path,
                        "sort_by": sort_by,
                        "to": to,
                        "video_id": video_id,
                        "view_id": view_id,
                        "viewer_id": viewer_id,
                    },
                    video_list_params.VideoListParams,
                ),
                security={"secret_key": True},
            ),
            model=VideoMetrics,
        )


class AsyncVideosResource(AsyncAPIResource):
    """Private retained-event and view-cohort queries."""

    @cached_property
    def with_raw_response(self) -> AsyncVideosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVideosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVideosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#with_streaming_response
        """
        return AsyncVideosResourceWithStreamingResponse(self)

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
        order: Literal["asc", "desc"] | Omit = omit,
        os_name: str | Omit = omit,
        page_origin: str | Omit = omit,
        page_path: str | Omit = omit,
        sort_by: Literal["video_id", "views", "unique_viewers", "total_playing_time_ms", "playback_score"]
        | Omit = omit,
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
    ) -> AsyncPaginator[VideoMetrics, AsyncVideosPage[VideoMetrics]]:
        """List per-video totals.

        Sort the entire filtered cohort by video_id, views,
        unique_viewers, total_playing_time_ms or playback_score before pagination.
        Defaults to video_id ascending. Missing scores come last; metric ties use
        video_id ascending in both directions. Unique viewer counts cannot be added
        across videos. Keep sort_by, order and filters unchanged with a cursor.

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

          order: Sort direction. Events and videos default to asc; views default to desc. Events
              sort by ingestion sequence. Videos and views sort by sort_by with missing values
              last. View ties use view_id in the requested direction; video metric ties use
              video_id ascending.

          os_name: Exact operating-system name, such as macOS. Missing values do not match.

          page_origin: Exact, case-sensitive page origin captured by the player, such as
              https://example.com. Metrics use the first retained view start; raw events use
              each event context. Missing values do not match.

          page_path: Exact, case-sensitive page path captured by the player, such as /watch/video.
              Filter by page_origin as well to distinguish identical paths on different sites.
              Metrics use the first retained view start; raw events use each event context.
              Missing values do not match.

          sort_by: Rank all matching videos before pagination. Missing scores come last in both
              directions. Metric ties use video_id ascending. Keep sort_by, order and filters
              unchanged with a cursor.

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
            "/v1/videos",
            page=AsyncVideosPage[VideoMetrics],
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
                        "order": order,
                        "os_name": os_name,
                        "page_origin": page_origin,
                        "page_path": page_path,
                        "sort_by": sort_by,
                        "to": to,
                        "video_id": video_id,
                        "view_id": view_id,
                        "viewer_id": viewer_id,
                    },
                    video_list_params.VideoListParams,
                ),
                security={"secret_key": True},
            ),
            model=VideoMetrics,
        )


class VideosResourceWithRawResponse:
    def __init__(self, videos: VideosResource) -> None:
        self._videos = videos

        self.list = to_raw_response_wrapper(
            videos.list,
        )


class AsyncVideosResourceWithRawResponse:
    def __init__(self, videos: AsyncVideosResource) -> None:
        self._videos = videos

        self.list = async_to_raw_response_wrapper(
            videos.list,
        )


class VideosResourceWithStreamingResponse:
    def __init__(self, videos: VideosResource) -> None:
        self._videos = videos

        self.list = to_streamed_response_wrapper(
            videos.list,
        )


class AsyncVideosResourceWithStreamingResponse:
    def __init__(self, videos: AsyncVideosResource) -> None:
        self._videos = videos

        self.list = async_to_streamed_response_wrapper(
            videos.list,
        )
