# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import view_list_params, view_retrieve_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncViewsPage, AsyncViewsPage
from ..types.view import View
from .._base_client import AsyncPaginator, make_request_options
from ..types.view_detail import ViewDetail

__all__ = ["ViewsResource", "AsyncViewsResource"]


class ViewsResource(SyncAPIResource):
    """Private retained-event and view-cohort queries."""

    @cached_property
    def with_raw_response(self) -> ViewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#accessing-raw-response-data-eg-headers
        """
        return ViewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ViewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#with_streaming_response
        """
        return ViewsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        view_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewDetail:
        """
        Returns start context and selected measurements, plus a paginated history of all
        retained events for that view ID, in ingestion order. SDK sequence and
        occurrence times remain in each event. Follow next_cursor with the same view ID;
        the summary and event pages share the initial ingestion watermark. Orphaned
        events without a retained start remain available through /v1/events?view_id=...
        .

        Args:
          cursor: Use next_cursor from the previous page. Keep the same filters, sort_by and
              order. Video cursors from earlier versions are invalid; start a new pagination
              sequence after upgrading.

          limit: Maximum rows on this page. Events and videos always support pagination; summary,
              quality and engagement support it only with group_by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        return self._get(
            path_template("/v1/views/{view_id}", view_id=view_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    view_retrieve_params.ViewRetrieveParams,
                ),
                security={"secret_key": True},
            ),
            cast_to=ViewDetail,
        )

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
        has_fatal_error: bool | Omit = omit,
        limit: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        os_name: str | Omit = omit,
        page_origin: str | Omit = omit,
        page_path: str | Omit = omit,
        playback_rate: str | Omit = omit,
        sort_by: Literal[
            "started_at",
            "video_id",
            "view_id",
            "device_type",
            "playing_time_ms",
            "startup_time_ms",
            "rebuffer_duration_ms",
            "playback_score",
        ]
        | Omit = omit,
        subtitle_language: str | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        user_id: str | Omit = omit,
        video_id: str | Omit = omit,
        video_title: str | Omit = omit,
        view_id: str | Omit = omit,
        viewer_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncViewsPage[View]:
        """
        One row per first retained start, using the same final/latest measurement
        selection as metrics. Filter by identity, context, dates or has_fatal_error.
        Order by started_at descending by default (newest first), or ascending with
        order=asc. Equal start times use view_id in the same direction. Cursors bind
        filters, order, fatal-error selection, project and ingestion watermark. Missing
        end or error events are not proof of an ongoing or successful playback. Sort the
        entire matching cohort by sort_by before pagination, with missing values last.

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

          has_fatal_error: Select attempts with or without an observed fatal error. Absence of an observed
              error does not prove successful playback.

          limit: Maximum rows on this page. Events and videos always support pagination; summary,
              quality and engagement support it only with group_by.

          order: Sort by started_at and then view_id in this direction. Defaults to newest first.
              Keep the same order with each cursor.

          os_name: Exact operating-system name, such as macOS. Missing values do not match.

          page_origin: Exact, case-sensitive page origin captured by the player, such as
              https://example.com. Metrics use the first retained view start; raw events use
              each event context. Missing values do not match.

          page_path: Exact, case-sensitive page path captured by the player, such as /watch/video.
              Filter by page_origin as well to distinguish identical paths on different sites.
              Metrics use the first retained view start; raw events use each event context.
              Missing values do not match.

          playback_rate: Playback rate from 0.01 to 16 with at most two decimals, such as 1, 1.5 or 2;
              2.0 and 2 are the same rate. Metrics use the rate on the first retained view
              start; raw events use each event's value.

          sort_by: Sort all matching sessions before pagination. Missing values come last in both
              directions. Ties use view_id in the requested direction. Keep sort_by, order and
              filters unchanged with a cursor.

          subtitle_language: Exact, case-sensitive, non-blank subtitle language tag, such as fr or en-US; und
              for a subtitles track without a language. Metrics use the language showing on
              the first retained view start; raw events use each event's value. Views without
              subtitles at start do not match.

          to: Exclusive RFC3339 occurrence-time upper bound, with timezone. Summary/video
              queries apply it to the selected view_started event.

          user_id: Exact integrator-supplied user ID. Selects views by their start event; event
              lists match each event's own value. Missing/null user IDs do not match. Reports
              with this filter read one stored row per view.

          video_id: Exact video ID; must not be blank. Combined with all other filters using AND.

          video_title: Exact, case-sensitive video title. Selects views by the title on their first
              retained start; event lists match each event's own value. Views without a title
              do not match. Reports with this filter read one stored row per view.

          view_id: Filter one playback attempt by view ID. Metrics use its first retained start.

          viewer_id: Exact viewer ID. The Chunkify player SDK generates one per browser; missing/null
              viewer IDs do not match.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/views",
            page=SyncViewsPage[View],
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
                        "has_fatal_error": has_fatal_error,
                        "limit": limit,
                        "order": order,
                        "os_name": os_name,
                        "page_origin": page_origin,
                        "page_path": page_path,
                        "playback_rate": playback_rate,
                        "sort_by": sort_by,
                        "subtitle_language": subtitle_language,
                        "to": to,
                        "user_id": user_id,
                        "video_id": video_id,
                        "video_title": video_title,
                        "view_id": view_id,
                        "viewer_id": viewer_id,
                    },
                    view_list_params.ViewListParams,
                ),
                security={"secret_key": True},
            ),
            model=View,
        )


class AsyncViewsResource(AsyncAPIResource):
    """Private retained-event and view-cohort queries."""

    @cached_property
    def with_raw_response(self) -> AsyncViewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncViewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncViewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#with_streaming_response
        """
        return AsyncViewsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        view_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewDetail:
        """
        Returns start context and selected measurements, plus a paginated history of all
        retained events for that view ID, in ingestion order. SDK sequence and
        occurrence times remain in each event. Follow next_cursor with the same view ID;
        the summary and event pages share the initial ingestion watermark. Orphaned
        events without a retained start remain available through /v1/events?view_id=...
        .

        Args:
          cursor: Use next_cursor from the previous page. Keep the same filters, sort_by and
              order. Video cursors from earlier versions are invalid; start a new pagination
              sequence after upgrading.

          limit: Maximum rows on this page. Events and videos always support pagination; summary,
              quality and engagement support it only with group_by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        return await self._get(
            path_template("/v1/views/{view_id}", view_id=view_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    view_retrieve_params.ViewRetrieveParams,
                ),
                security={"secret_key": True},
            ),
            cast_to=ViewDetail,
        )

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
        has_fatal_error: bool | Omit = omit,
        limit: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        os_name: str | Omit = omit,
        page_origin: str | Omit = omit,
        page_path: str | Omit = omit,
        playback_rate: str | Omit = omit,
        sort_by: Literal[
            "started_at",
            "video_id",
            "view_id",
            "device_type",
            "playing_time_ms",
            "startup_time_ms",
            "rebuffer_duration_ms",
            "playback_score",
        ]
        | Omit = omit,
        subtitle_language: str | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        user_id: str | Omit = omit,
        video_id: str | Omit = omit,
        video_title: str | Omit = omit,
        view_id: str | Omit = omit,
        viewer_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[View, AsyncViewsPage[View]]:
        """
        One row per first retained start, using the same final/latest measurement
        selection as metrics. Filter by identity, context, dates or has_fatal_error.
        Order by started_at descending by default (newest first), or ascending with
        order=asc. Equal start times use view_id in the same direction. Cursors bind
        filters, order, fatal-error selection, project and ingestion watermark. Missing
        end or error events are not proof of an ongoing or successful playback. Sort the
        entire matching cohort by sort_by before pagination, with missing values last.

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

          has_fatal_error: Select attempts with or without an observed fatal error. Absence of an observed
              error does not prove successful playback.

          limit: Maximum rows on this page. Events and videos always support pagination; summary,
              quality and engagement support it only with group_by.

          order: Sort by started_at and then view_id in this direction. Defaults to newest first.
              Keep the same order with each cursor.

          os_name: Exact operating-system name, such as macOS. Missing values do not match.

          page_origin: Exact, case-sensitive page origin captured by the player, such as
              https://example.com. Metrics use the first retained view start; raw events use
              each event context. Missing values do not match.

          page_path: Exact, case-sensitive page path captured by the player, such as /watch/video.
              Filter by page_origin as well to distinguish identical paths on different sites.
              Metrics use the first retained view start; raw events use each event context.
              Missing values do not match.

          playback_rate: Playback rate from 0.01 to 16 with at most two decimals, such as 1, 1.5 or 2;
              2.0 and 2 are the same rate. Metrics use the rate on the first retained view
              start; raw events use each event's value.

          sort_by: Sort all matching sessions before pagination. Missing values come last in both
              directions. Ties use view_id in the requested direction. Keep sort_by, order and
              filters unchanged with a cursor.

          subtitle_language: Exact, case-sensitive, non-blank subtitle language tag, such as fr or en-US; und
              for a subtitles track without a language. Metrics use the language showing on
              the first retained view start; raw events use each event's value. Views without
              subtitles at start do not match.

          to: Exclusive RFC3339 occurrence-time upper bound, with timezone. Summary/video
              queries apply it to the selected view_started event.

          user_id: Exact integrator-supplied user ID. Selects views by their start event; event
              lists match each event's own value. Missing/null user IDs do not match. Reports
              with this filter read one stored row per view.

          video_id: Exact video ID; must not be blank. Combined with all other filters using AND.

          video_title: Exact, case-sensitive video title. Selects views by the title on their first
              retained start; event lists match each event's own value. Views without a title
              do not match. Reports with this filter read one stored row per view.

          view_id: Filter one playback attempt by view ID. Metrics use its first retained start.

          viewer_id: Exact viewer ID. The Chunkify player SDK generates one per browser; missing/null
              viewer IDs do not match.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/views",
            page=AsyncViewsPage[View],
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
                        "has_fatal_error": has_fatal_error,
                        "limit": limit,
                        "order": order,
                        "os_name": os_name,
                        "page_origin": page_origin,
                        "page_path": page_path,
                        "playback_rate": playback_rate,
                        "sort_by": sort_by,
                        "subtitle_language": subtitle_language,
                        "to": to,
                        "user_id": user_id,
                        "video_id": video_id,
                        "video_title": video_title,
                        "view_id": view_id,
                        "viewer_id": viewer_id,
                    },
                    view_list_params.ViewListParams,
                ),
                security={"secret_key": True},
            ),
            model=View,
        )


class ViewsResourceWithRawResponse:
    def __init__(self, views: ViewsResource) -> None:
        self._views = views

        self.retrieve = to_raw_response_wrapper(
            views.retrieve,
        )
        self.list = to_raw_response_wrapper(
            views.list,
        )


class AsyncViewsResourceWithRawResponse:
    def __init__(self, views: AsyncViewsResource) -> None:
        self._views = views

        self.retrieve = async_to_raw_response_wrapper(
            views.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            views.list,
        )


class ViewsResourceWithStreamingResponse:
    def __init__(self, views: ViewsResource) -> None:
        self._views = views

        self.retrieve = to_streamed_response_wrapper(
            views.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            views.list,
        )


class AsyncViewsResourceWithStreamingResponse:
    def __init__(self, views: AsyncViewsResource) -> None:
        self._views = views

        self.retrieve = async_to_streamed_response_wrapper(
            views.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            views.list,
        )
