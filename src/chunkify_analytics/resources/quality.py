# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import quality_retrieve_params
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
from ..types.quality_response import QualityResponse

__all__ = ["QualityResource", "AsyncQualityResource"]


class QualityResource(SyncAPIResource):
    """Private retained-event and view-cohort queries."""

    @cached_property
    def with_raw_response(self) -> QualityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#accessing-raw-response-data-eg-headers
        """
        return QualityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QualityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#with_streaming_response
        """
        return QualityResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        browser_name: str | Omit = omit,
        city: str | Omit = omit,
        continent: Literal["AF", "AN", "AS", "EU", "NA", "OC", "SA"] | Omit = omit,
        country: str | Omit = omit,
        cursor: str | Omit = omit,
        device_type: Literal["desktop", "mobile", "tablet", "unknown"] | Omit = omit,
        from_: Union[str, datetime] | Omit = omit,
        group_by: Union[
            Literal[
                "browser_name",
                "os_name",
                "device_type",
                "continent",
                "country",
                "city",
                "page_origin",
                "page_path",
                "subtitle_language",
                "playback_rate",
                "video_title",
                "user_id",
            ],
            str,
        ]
        | Omit = omit,
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
    ) -> QualityResponse:
        """
        Get startup time, buffering, and observed fatal errors for matching playback
        attempts. Null means unavailable. Optionally group the full filtered view-start
        cohort with group_by=browser_name, os_name, device_type, continent, country or
        city. Without group_by the totals response is unchanged. With group_by, return
        paginated groups sorted by views descending. Equal view counts sort by value
        ascending, null first. Context comes from the first retained start; missing,
        null and nonstring values form a null group. Keep group_by and filters unchanged
        with each cursor. Unique viewers must not be summed across groups. Includes
        mutually exclusive startup outcomes; unknown outcomes remain explicit.

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

          group_by: Optional on summary, quality and engagement. Group views by this field on their
              first retained start. Missing, null and nonstring context forms a null group;
              the literal device type unknown stays separate. Groups sort by views descending,
              then value ascending with null first for ties. Pagination is available only with
              group_by. Location uses the first retained start too. City groups use the stored
              name; filter by country to avoid combining names shared by different countries.
              Page groups use the first retained start even if playback continues after
              navigation. Filter by page_origin when grouping page_path to distinguish
              identical paths on different sites. video_title groups by the title on each
              view's first retained start, so a renamed video counts each view under the title
              it started with. user_id groups by the user ID on each view's first retained
              start. Use custom.<key>, such as custom.plan, to group by a custom dimension;
              views without the key form the null group.

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
        return cast(
            QualityResponse,
            self._get(
                "/v1/quality",
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
                            "group_by": group_by,
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
                        quality_retrieve_params.QualityRetrieveParams,
                    ),
                    security={"secret_key": True},
                ),
                cast_to=cast(Any, QualityResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncQualityResource(AsyncAPIResource):
    """Private retained-event and view-cohort queries."""

    @cached_property
    def with_raw_response(self) -> AsyncQualityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQualityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQualityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#with_streaming_response
        """
        return AsyncQualityResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        browser_name: str | Omit = omit,
        city: str | Omit = omit,
        continent: Literal["AF", "AN", "AS", "EU", "NA", "OC", "SA"] | Omit = omit,
        country: str | Omit = omit,
        cursor: str | Omit = omit,
        device_type: Literal["desktop", "mobile", "tablet", "unknown"] | Omit = omit,
        from_: Union[str, datetime] | Omit = omit,
        group_by: Union[
            Literal[
                "browser_name",
                "os_name",
                "device_type",
                "continent",
                "country",
                "city",
                "page_origin",
                "page_path",
                "subtitle_language",
                "playback_rate",
                "video_title",
                "user_id",
            ],
            str,
        ]
        | Omit = omit,
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
    ) -> QualityResponse:
        """
        Get startup time, buffering, and observed fatal errors for matching playback
        attempts. Null means unavailable. Optionally group the full filtered view-start
        cohort with group_by=browser_name, os_name, device_type, continent, country or
        city. Without group_by the totals response is unchanged. With group_by, return
        paginated groups sorted by views descending. Equal view counts sort by value
        ascending, null first. Context comes from the first retained start; missing,
        null and nonstring values form a null group. Keep group_by and filters unchanged
        with each cursor. Unique viewers must not be summed across groups. Includes
        mutually exclusive startup outcomes; unknown outcomes remain explicit.

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

          group_by: Optional on summary, quality and engagement. Group views by this field on their
              first retained start. Missing, null and nonstring context forms a null group;
              the literal device type unknown stays separate. Groups sort by views descending,
              then value ascending with null first for ties. Pagination is available only with
              group_by. Location uses the first retained start too. City groups use the stored
              name; filter by country to avoid combining names shared by different countries.
              Page groups use the first retained start even if playback continues after
              navigation. Filter by page_origin when grouping page_path to distinguish
              identical paths on different sites. video_title groups by the title on each
              view's first retained start, so a renamed video counts each view under the title
              it started with. user_id groups by the user ID on each view's first retained
              start. Use custom.<key>, such as custom.plan, to group by a custom dimension;
              views without the key form the null group.

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
        return cast(
            QualityResponse,
            await self._get(
                "/v1/quality",
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
                            "cursor": cursor,
                            "device_type": device_type,
                            "from_": from_,
                            "group_by": group_by,
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
                        quality_retrieve_params.QualityRetrieveParams,
                    ),
                    security={"secret_key": True},
                ),
                cast_to=cast(Any, QualityResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class QualityResourceWithRawResponse:
    def __init__(self, quality: QualityResource) -> None:
        self._quality = quality

        self.retrieve = to_raw_response_wrapper(
            quality.retrieve,
        )


class AsyncQualityResourceWithRawResponse:
    def __init__(self, quality: AsyncQualityResource) -> None:
        self._quality = quality

        self.retrieve = async_to_raw_response_wrapper(
            quality.retrieve,
        )


class QualityResourceWithStreamingResponse:
    def __init__(self, quality: QualityResource) -> None:
        self._quality = quality

        self.retrieve = to_streamed_response_wrapper(
            quality.retrieve,
        )


class AsyncQualityResourceWithStreamingResponse:
    def __init__(self, quality: AsyncQualityResource) -> None:
        self._quality = quality

        self.retrieve = async_to_streamed_response_wrapper(
            quality.retrieve,
        )
