# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .keys import (
    KeysResource,
    AsyncKeysResource,
    KeysResourceWithRawResponse,
    AsyncKeysResourceWithRawResponse,
    KeysResourceWithStreamingResponse,
    AsyncKeysResourceWithStreamingResponse,
)
from ...types import admin_create_project_params
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.created_project import CreatedProject

__all__ = ["AdminResource", "AsyncAdminResource"]


class AdminResource(SyncAPIResource):
    """Project origins and keys."""

    @cached_property
    def keys(self) -> KeysResource:
        """Project origins and keys."""
        return KeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> AdminResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AdminResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdminResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#with_streaming_response
        """
        return AdminResourceWithStreamingResponse(self)

    def create_project(
        self,
        *,
        name: str,
        allowed_origins: SequenceNotStr[str] | Omit = omit,
        retention_seconds: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreatedProject:
        """Generate a project ID and initial keys, optionally setting retention.

        Requires
        the installation admin key. The project and its retention are active before
        success is returned.

        Args:
          name: Project display name.

          allowed_origins: Additional project origins. Shared TOML origins are always included.

          retention_seconds: Retention by server receipt time, in seconds. 0 disables expiration; null
              inherits the installation default. Omission also inherits the default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/projects",
            body=maybe_transform(
                {
                    "name": name,
                    "allowed_origins": allowed_origins,
                    "retention_seconds": retention_seconds,
                },
                admin_create_project_params.AdminCreateProjectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"admin_key": True},
            ),
            cast_to=CreatedProject,
        )


class AsyncAdminResource(AsyncAPIResource):
    """Project origins and keys."""

    @cached_property
    def keys(self) -> AsyncKeysResource:
        """Project origins and keys."""
        return AsyncKeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAdminResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAdminResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdminResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#with_streaming_response
        """
        return AsyncAdminResourceWithStreamingResponse(self)

    async def create_project(
        self,
        *,
        name: str,
        allowed_origins: SequenceNotStr[str] | Omit = omit,
        retention_seconds: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreatedProject:
        """Generate a project ID and initial keys, optionally setting retention.

        Requires
        the installation admin key. The project and its retention are active before
        success is returned.

        Args:
          name: Project display name.

          allowed_origins: Additional project origins. Shared TOML origins are always included.

          retention_seconds: Retention by server receipt time, in seconds. 0 disables expiration; null
              inherits the installation default. Omission also inherits the default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/projects",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "allowed_origins": allowed_origins,
                    "retention_seconds": retention_seconds,
                },
                admin_create_project_params.AdminCreateProjectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"admin_key": True},
            ),
            cast_to=CreatedProject,
        )


class AdminResourceWithRawResponse:
    def __init__(self, admin: AdminResource) -> None:
        self._admin = admin

        self.create_project = to_raw_response_wrapper(
            admin.create_project,
        )

    @cached_property
    def keys(self) -> KeysResourceWithRawResponse:
        """Project origins and keys."""
        return KeysResourceWithRawResponse(self._admin.keys)


class AsyncAdminResourceWithRawResponse:
    def __init__(self, admin: AsyncAdminResource) -> None:
        self._admin = admin

        self.create_project = async_to_raw_response_wrapper(
            admin.create_project,
        )

    @cached_property
    def keys(self) -> AsyncKeysResourceWithRawResponse:
        """Project origins and keys."""
        return AsyncKeysResourceWithRawResponse(self._admin.keys)


class AdminResourceWithStreamingResponse:
    def __init__(self, admin: AdminResource) -> None:
        self._admin = admin

        self.create_project = to_streamed_response_wrapper(
            admin.create_project,
        )

    @cached_property
    def keys(self) -> KeysResourceWithStreamingResponse:
        """Project origins and keys."""
        return KeysResourceWithStreamingResponse(self._admin.keys)


class AsyncAdminResourceWithStreamingResponse:
    def __init__(self, admin: AsyncAdminResource) -> None:
        self._admin = admin

        self.create_project = async_to_streamed_response_wrapper(
            admin.create_project,
        )

    @cached_property
    def keys(self) -> AsyncKeysResourceWithStreamingResponse:
        """Project origins and keys."""
        return AsyncKeysResourceWithStreamingResponse(self._admin.keys)
