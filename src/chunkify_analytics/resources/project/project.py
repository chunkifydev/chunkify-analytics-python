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
from ...types import project_update_params
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
from ...types.deleted_project import DeletedProject
from ...types.project.project import Project

__all__ = ["ProjectResource", "AsyncProjectResource"]


class ProjectResource(SyncAPIResource):
    """Project origins and keys."""

    @cached_property
    def keys(self) -> KeysResource:
        """Project origins and keys."""
        return KeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProjectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#accessing-raw-response-data-eg-headers
        """
        return ProjectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProjectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#with_streaming_response
        """
        return ProjectResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        allowed_origins: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        retention_seconds: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Project:
        """Update the name, additional origins or retention of your project.

        Omitted fields
        stay unchanged. Set retention_seconds to null to inherit the installation
        default, or 0 to disable expiration. Changes apply to existing and new events
        without a restart. Requires a full-access private key; read-only keys
        receive 403.

        Args:
          allowed_origins: Additional project origins. Shared TOML origins are always included.

          retention_seconds: Retention by server receipt time, in seconds. 0 disables expiration; null
              inherits the installation default. Omission leaves the current setting
              unchanged. Applies to existing and new events; removed data cannot be recovered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/v1/project",
            body=maybe_transform(
                {
                    "allowed_origins": allowed_origins,
                    "name": name,
                    "retention_seconds": retention_seconds,
                },
                project_update_params.ProjectUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"secret_key": True},
            ),
            cast_to=Project,
        )

    def delete(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeletedProject:
        """Revoke all project keys.

        Stored events remain until their retention expires.
        Requires a full-access private key; read-only keys receive 403.
        """
        return self._delete(
            "/v1/project",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"secret_key": True},
            ),
            cast_to=DeletedProject,
        )


class AsyncProjectResource(AsyncAPIResource):
    """Project origins and keys."""

    @cached_property
    def keys(self) -> AsyncKeysResource:
        """Project origins and keys."""
        return AsyncKeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProjectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProjectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProjectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#with_streaming_response
        """
        return AsyncProjectResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        allowed_origins: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        retention_seconds: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Project:
        """Update the name, additional origins or retention of your project.

        Omitted fields
        stay unchanged. Set retention_seconds to null to inherit the installation
        default, or 0 to disable expiration. Changes apply to existing and new events
        without a restart. Requires a full-access private key; read-only keys
        receive 403.

        Args:
          allowed_origins: Additional project origins. Shared TOML origins are always included.

          retention_seconds: Retention by server receipt time, in seconds. 0 disables expiration; null
              inherits the installation default. Omission leaves the current setting
              unchanged. Applies to existing and new events; removed data cannot be recovered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/v1/project",
            body=await async_maybe_transform(
                {
                    "allowed_origins": allowed_origins,
                    "name": name,
                    "retention_seconds": retention_seconds,
                },
                project_update_params.ProjectUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"secret_key": True},
            ),
            cast_to=Project,
        )

    async def delete(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeletedProject:
        """Revoke all project keys.

        Stored events remain until their retention expires.
        Requires a full-access private key; read-only keys receive 403.
        """
        return await self._delete(
            "/v1/project",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"secret_key": True},
            ),
            cast_to=DeletedProject,
        )


class ProjectResourceWithRawResponse:
    def __init__(self, project: ProjectResource) -> None:
        self._project = project

        self.update = to_raw_response_wrapper(
            project.update,
        )
        self.delete = to_raw_response_wrapper(
            project.delete,
        )

    @cached_property
    def keys(self) -> KeysResourceWithRawResponse:
        """Project origins and keys."""
        return KeysResourceWithRawResponse(self._project.keys)


class AsyncProjectResourceWithRawResponse:
    def __init__(self, project: AsyncProjectResource) -> None:
        self._project = project

        self.update = async_to_raw_response_wrapper(
            project.update,
        )
        self.delete = async_to_raw_response_wrapper(
            project.delete,
        )

    @cached_property
    def keys(self) -> AsyncKeysResourceWithRawResponse:
        """Project origins and keys."""
        return AsyncKeysResourceWithRawResponse(self._project.keys)


class ProjectResourceWithStreamingResponse:
    def __init__(self, project: ProjectResource) -> None:
        self._project = project

        self.update = to_streamed_response_wrapper(
            project.update,
        )
        self.delete = to_streamed_response_wrapper(
            project.delete,
        )

    @cached_property
    def keys(self) -> KeysResourceWithStreamingResponse:
        """Project origins and keys."""
        return KeysResourceWithStreamingResponse(self._project.keys)


class AsyncProjectResourceWithStreamingResponse:
    def __init__(self, project: AsyncProjectResource) -> None:
        self._project = project

        self.update = async_to_streamed_response_wrapper(
            project.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            project.delete,
        )

    @cached_property
    def keys(self) -> AsyncKeysResourceWithStreamingResponse:
        """Project origins and keys."""
        return AsyncKeysResourceWithStreamingResponse(self._project.keys)
