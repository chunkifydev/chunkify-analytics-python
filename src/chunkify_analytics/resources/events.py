# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import event_list_params, event_ingest_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import is_given, maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncEventsPage, AsyncEventsPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.stored_event import StoredEvent
from ..types.analytics_event_param import AnalyticsEventParam
from ..types.event_ingest_response import EventIngestResponse

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#accessing-raw-response-data-eg-headers
        """
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#with_streaming_response
        """
        return EventsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        browser_name: str | Omit = omit,
        city: str | Omit = omit,
        continent: Literal["AF", "AN", "AS", "EU", "NA", "OC", "SA"] | Omit = omit,
        country: str | Omit = omit,
        cursor: str | Omit = omit,
        device_type: Literal["desktop", "mobile", "tablet", "unknown"] | Omit = omit,
        event_name: Literal[
            "chunkify.video.view_started",
            "chunkify.video.view_snapshot",
            "chunkify.video.playback_error",
            "chunkify.video.view_ended",
            "chunkify.video.playback_state_changed",
            "chunkify.video.rendition_changed",
            "chunkify.video.seek_completed",
        ]
        | Omit = omit,
        from_: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
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
    ) -> SyncEventsPage[StoredEvent]:
        """List project events with filters and pagination.

        Use order=desc for the newest
        events.

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

          event_name: Raw-event queries only. Summaries and videos reject this parameter.

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
            "/v1/events",
            page=SyncEventsPage[StoredEvent],
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
                        "event_name": event_name,
                        "from_": from_,
                        "limit": limit,
                        "order": order,
                        "os_name": os_name,
                        "page_origin": page_origin,
                        "page_path": page_path,
                        "to": to,
                        "video_id": video_id,
                        "view_id": view_id,
                        "viewer_id": viewer_id,
                    },
                    event_list_params.EventListParams,
                ),
                security={"secret_key": True},
            ),
            model=StoredEvent,
        )

    def ingest(
        self,
        *,
        event: AnalyticsEventParam,
        content_encoding: Literal["identity"] | Omit = omit,
        origin: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventIngestResponse:
        """Send one playback event using a public key.

        Success confirms storage completed.

        Configure the client with a public ingestion key for this method. The SDK sends
        the event you supply; it does not collect playback events automatically. For
        automatic browser player tracking, use `@chunkify/player-analytics`.

        Args:
          event: A schema version 1 playback event. Extra properties are preserved.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Content-Encoding": str(content_encoding) if is_given(content_encoding) else not_given,
                    "Origin": origin,
                }
            ),
            **(extra_headers or {}),
        }
        return cast(
            EventIngestResponse,
            self._post(
                "/v1/events",
                body=maybe_transform(event, event_ingest_params.EventIngestParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    security={"public_key": True},
                ),
                cast_to=cast(
                    Any, EventIngestResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#with_streaming_response
        """
        return AsyncEventsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        browser_name: str | Omit = omit,
        city: str | Omit = omit,
        continent: Literal["AF", "AN", "AS", "EU", "NA", "OC", "SA"] | Omit = omit,
        country: str | Omit = omit,
        cursor: str | Omit = omit,
        device_type: Literal["desktop", "mobile", "tablet", "unknown"] | Omit = omit,
        event_name: Literal[
            "chunkify.video.view_started",
            "chunkify.video.view_snapshot",
            "chunkify.video.playback_error",
            "chunkify.video.view_ended",
            "chunkify.video.playback_state_changed",
            "chunkify.video.rendition_changed",
            "chunkify.video.seek_completed",
        ]
        | Omit = omit,
        from_: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
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
    ) -> AsyncPaginator[StoredEvent, AsyncEventsPage[StoredEvent]]:
        """List project events with filters and pagination.

        Use order=desc for the newest
        events.

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

          event_name: Raw-event queries only. Summaries and videos reject this parameter.

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
            "/v1/events",
            page=AsyncEventsPage[StoredEvent],
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
                        "event_name": event_name,
                        "from_": from_,
                        "limit": limit,
                        "order": order,
                        "os_name": os_name,
                        "page_origin": page_origin,
                        "page_path": page_path,
                        "to": to,
                        "video_id": video_id,
                        "view_id": view_id,
                        "viewer_id": viewer_id,
                    },
                    event_list_params.EventListParams,
                ),
                security={"secret_key": True},
            ),
            model=StoredEvent,
        )

    async def ingest(
        self,
        *,
        event: AnalyticsEventParam,
        content_encoding: Literal["identity"] | Omit = omit,
        origin: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventIngestResponse:
        """Send one playback event using a public key.

        Success confirms storage completed.

        Configure the client with a public ingestion key for this method. The SDK sends
        the event you supply; it does not collect playback events automatically. For
        automatic browser player tracking, use `@chunkify/player-analytics`.

        Args:
          event: A schema version 1 playback event. Extra properties are preserved.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Content-Encoding": str(content_encoding) if is_given(content_encoding) else not_given,
                    "Origin": origin,
                }
            ),
            **(extra_headers or {}),
        }
        return cast(
            EventIngestResponse,
            await self._post(
                "/v1/events",
                body=await async_maybe_transform(event, event_ingest_params.EventIngestParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    security={"public_key": True},
                ),
                cast_to=cast(
                    Any, EventIngestResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.list = to_raw_response_wrapper(
            events.list,
        )
        self.ingest = to_raw_response_wrapper(
            events.ingest,
        )


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.list = async_to_raw_response_wrapper(
            events.list,
        )
        self.ingest = async_to_raw_response_wrapper(
            events.ingest,
        )


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.list = to_streamed_response_wrapper(
            events.list,
        )
        self.ingest = to_streamed_response_wrapper(
            events.ingest,
        )


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.list = async_to_streamed_response_wrapper(
            events.list,
        )
        self.ingest = async_to_streamed_response_wrapper(
            events.ingest,
        )
