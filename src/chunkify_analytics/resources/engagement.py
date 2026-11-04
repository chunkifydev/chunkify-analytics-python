# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import engagement_retrieve_params
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
from ..types.engagement_response import EngagementResponse

__all__ = ["EngagementResource", "AsyncEngagementResource"]


class EngagementResource(SyncAPIResource):
    """Private retained-event and view-cohort queries."""

    @cached_property
    def with_raw_response(self) -> EngagementResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#accessing-raw-response-data-eg-headers
        """
        return EngagementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EngagementResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#with_streaming_response
        """
        return EngagementResourceWithStreamingResponse(self)

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
        group_by: Literal[
            "browser_name", "os_name", "device_type", "continent", "country", "city", "page_origin", "page_path"
        ]
        | Omit = omit,
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
    ) -> EngagementResponse:
        """Get average watch time per attempt and the observed reached-end rate.

        Reaching
        the end does not prove the whole video was watched. Optionally group the full
        filtered view-start cohort with group_by=browser_name, os_name, device_type,
        continent, country or city. Without group_by the totals response is unchanged.
        With group_by, return paginated groups sorted by views descending. Equal view
        counts sort by value ascending, null first. Context comes from the first
        retained start; missing, null and nonstring values form a null group. Keep
        group_by and filters unchanged with each cursor. Unique viewers must not be
        summed across groups. Includes furthest-progress milestones and measured
        watch-time distribution. Progress can include seeking and is not retention.

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
              identical paths on different sites.

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
        return cast(
            EngagementResponse,
            self._get(
                "/v1/engagement",
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
                            "to": to,
                            "video_id": video_id,
                            "view_id": view_id,
                            "viewer_id": viewer_id,
                        },
                        engagement_retrieve_params.EngagementRetrieveParams,
                    ),
                    security={"secret_key": True},
                ),
                cast_to=cast(
                    Any, EngagementResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncEngagementResource(AsyncAPIResource):
    """Private retained-event and view-cohort queries."""

    @cached_property
    def with_raw_response(self) -> AsyncEngagementResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEngagementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEngagementResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#with_streaming_response
        """
        return AsyncEngagementResourceWithStreamingResponse(self)

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
        group_by: Literal[
            "browser_name", "os_name", "device_type", "continent", "country", "city", "page_origin", "page_path"
        ]
        | Omit = omit,
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
    ) -> EngagementResponse:
        """Get average watch time per attempt and the observed reached-end rate.

        Reaching
        the end does not prove the whole video was watched. Optionally group the full
        filtered view-start cohort with group_by=browser_name, os_name, device_type,
        continent, country or city. Without group_by the totals response is unchanged.
        With group_by, return paginated groups sorted by views descending. Equal view
        counts sort by value ascending, null first. Context comes from the first
        retained start; missing, null and nonstring values form a null group. Keep
        group_by and filters unchanged with each cursor. Unique viewers must not be
        summed across groups. Includes furthest-progress milestones and measured
        watch-time distribution. Progress can include seeking and is not retention.

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
              identical paths on different sites.

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
        return cast(
            EngagementResponse,
            await self._get(
                "/v1/engagement",
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
                            "to": to,
                            "video_id": video_id,
                            "view_id": view_id,
                            "viewer_id": viewer_id,
                        },
                        engagement_retrieve_params.EngagementRetrieveParams,
                    ),
                    security={"secret_key": True},
                ),
                cast_to=cast(
                    Any, EngagementResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class EngagementResourceWithRawResponse:
    def __init__(self, engagement: EngagementResource) -> None:
        self._engagement = engagement

        self.retrieve = to_raw_response_wrapper(
            engagement.retrieve,
        )


class AsyncEngagementResourceWithRawResponse:
    def __init__(self, engagement: AsyncEngagementResource) -> None:
        self._engagement = engagement

        self.retrieve = async_to_raw_response_wrapper(
            engagement.retrieve,
        )


class EngagementResourceWithStreamingResponse:
    def __init__(self, engagement: EngagementResource) -> None:
        self._engagement = engagement

        self.retrieve = to_streamed_response_wrapper(
            engagement.retrieve,
        )


class AsyncEngagementResourceWithStreamingResponse:
    def __init__(self, engagement: AsyncEngagementResource) -> None:
        self._engagement = engagement

        self.retrieve = async_to_streamed_response_wrapper(
            engagement.retrieve,
        )
