# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import playback_rate_retrieve_params
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
from ..types.playback_rate_report import PlaybackRateReport

__all__ = ["PlaybackRatesResource", "AsyncPlaybackRatesResource"]


class PlaybackRatesResource(SyncAPIResource):
    """Private retained-event and view-cohort queries."""

    @cached_property
    def with_raw_response(self) -> PlaybackRatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#accessing-raw-response-data-eg-headers
        """
        return PlaybackRatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PlaybackRatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#with_streaming_response
        """
        return PlaybackRatesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        browser_name: str | Omit = omit,
        city: str | Omit = omit,
        continent: Literal["AF", "AN", "AS", "EU", "NA", "OC", "SA"] | Omit = omit,
        country: str | Omit = omit,
        device_type: Literal["desktop", "mobile", "tablet", "unknown"] | Omit = omit,
        from_: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        os_name: str | Omit = omit,
        page_origin: str | Omit = omit,
        page_path: str | Omit = omit,
        playback_rate: str | Omit = omit,
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
    ) -> PlaybackRateReport:
        """Summarize watch time per playback rate.

        Expand each view's cumulative
        playback_rate_playing_time array once; rates are rounded to two decimals.
        Playing time is wall-clock time, so a minute at 2 covers about two minutes of
        media. Use only the selected final event, or latest snapshot when no final
        exists, for the filtered view-start cohort. Missing or empty measurements
        contribute no time; older SDKs send none. Rank by playing time descending, then
        value ascending with null first; limit bounds returned rows only, while totals
        cover every matching row. Views can contribute to several rows and must not be
        summed. No cursor, group_by, sort_by or order. Export resource=playback_rates
        includes all matching rows.

        Args:
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

          playback_rate: Playback rate from 0.01 to 16 with at most two decimals, such as 1, 1.5 or 2;
              2.0 and 2 are the same rate. Metrics use the rate on the first retained view
              start; raw events use each event's value.

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
        return self._get(
            "/v1/playback-rates",
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
                        "device_type": device_type,
                        "from_": from_,
                        "limit": limit,
                        "os_name": os_name,
                        "page_origin": page_origin,
                        "page_path": page_path,
                        "playback_rate": playback_rate,
                        "subtitle_language": subtitle_language,
                        "to": to,
                        "user_id": user_id,
                        "video_id": video_id,
                        "video_title": video_title,
                        "view_id": view_id,
                        "viewer_id": viewer_id,
                    },
                    playback_rate_retrieve_params.PlaybackRateRetrieveParams,
                ),
                security={"secret_key": True},
            ),
            cast_to=PlaybackRateReport,
        )


class AsyncPlaybackRatesResource(AsyncAPIResource):
    """Private retained-event and view-cohort queries."""

    @cached_property
    def with_raw_response(self) -> AsyncPlaybackRatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPlaybackRatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPlaybackRatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#with_streaming_response
        """
        return AsyncPlaybackRatesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        browser_name: str | Omit = omit,
        city: str | Omit = omit,
        continent: Literal["AF", "AN", "AS", "EU", "NA", "OC", "SA"] | Omit = omit,
        country: str | Omit = omit,
        device_type: Literal["desktop", "mobile", "tablet", "unknown"] | Omit = omit,
        from_: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        os_name: str | Omit = omit,
        page_origin: str | Omit = omit,
        page_path: str | Omit = omit,
        playback_rate: str | Omit = omit,
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
    ) -> PlaybackRateReport:
        """Summarize watch time per playback rate.

        Expand each view's cumulative
        playback_rate_playing_time array once; rates are rounded to two decimals.
        Playing time is wall-clock time, so a minute at 2 covers about two minutes of
        media. Use only the selected final event, or latest snapshot when no final
        exists, for the filtered view-start cohort. Missing or empty measurements
        contribute no time; older SDKs send none. Rank by playing time descending, then
        value ascending with null first; limit bounds returned rows only, while totals
        cover every matching row. Views can contribute to several rows and must not be
        summed. No cursor, group_by, sort_by or order. Export resource=playback_rates
        includes all matching rows.

        Args:
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

          playback_rate: Playback rate from 0.01 to 16 with at most two decimals, such as 1, 1.5 or 2;
              2.0 and 2 are the same rate. Metrics use the rate on the first retained view
              start; raw events use each event's value.

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
        return await self._get(
            "/v1/playback-rates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "browser_name": browser_name,
                        "city": city,
                        "continent": continent,
                        "country": country,
                        "device_type": device_type,
                        "from_": from_,
                        "limit": limit,
                        "os_name": os_name,
                        "page_origin": page_origin,
                        "page_path": page_path,
                        "playback_rate": playback_rate,
                        "subtitle_language": subtitle_language,
                        "to": to,
                        "user_id": user_id,
                        "video_id": video_id,
                        "video_title": video_title,
                        "view_id": view_id,
                        "viewer_id": viewer_id,
                    },
                    playback_rate_retrieve_params.PlaybackRateRetrieveParams,
                ),
                security={"secret_key": True},
            ),
            cast_to=PlaybackRateReport,
        )


class PlaybackRatesResourceWithRawResponse:
    def __init__(self, playback_rates: PlaybackRatesResource) -> None:
        self._playback_rates = playback_rates

        self.retrieve = to_raw_response_wrapper(
            playback_rates.retrieve,
        )


class AsyncPlaybackRatesResourceWithRawResponse:
    def __init__(self, playback_rates: AsyncPlaybackRatesResource) -> None:
        self._playback_rates = playback_rates

        self.retrieve = async_to_raw_response_wrapper(
            playback_rates.retrieve,
        )


class PlaybackRatesResourceWithStreamingResponse:
    def __init__(self, playback_rates: PlaybackRatesResource) -> None:
        self._playback_rates = playback_rates

        self.retrieve = to_streamed_response_wrapper(
            playback_rates.retrieve,
        )


class AsyncPlaybackRatesResourceWithStreamingResponse:
    def __init__(self, playback_rates: AsyncPlaybackRatesResource) -> None:
        self._playback_rates = playback_rates

        self.retrieve = async_to_streamed_response_wrapper(
            playback_rates.retrieve,
        )
