# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.project import key_create_params
from ...types.project_keys import ProjectKeys
from ...types.created_project_key import CreatedProjectKey
from ...types.rotated_project_key import RotatedProjectKey

__all__ = ["KeysResource", "AsyncKeysResource"]


class KeysResource(SyncAPIResource):
    """Project origins and keys."""

    @cached_property
    def with_raw_response(self) -> KeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#accessing-raw-response-data-eg-headers
        """
        return KeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#with_streaming_response
        """
        return KeysResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        permission: Literal["public", "secret"],
        read_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreatedProjectKey:
        """
        Create a named public ingestion key or secret key in the authenticated project.
        Secret keys default to full project access; set read_only to true for analytics
        reads and exports only. Requires a full-access project secret key. Read-only
        keys receive 403 and the installation admin key is not accepted. The key is
        active immediately and its value is returned once; store it before leaving this
        response. Each project supports at most 64 active keys, including its initial
        keys.

        Args:
          name: Key display name, up to 128 UTF-8 bytes. Whitespace-only names are rejected.

          read_only: Only secret keys can be read-only. False grants full project management access
              to secret keys; public keys only ingest events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/project/keys",
            body=maybe_transform(
                {
                    "name": name,
                    "permission": permission,
                    "read_only": read_only,
                },
                key_create_params.KeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"secret_key": True},
            ),
            cast_to=CreatedProjectKey,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectKeys:
        """List key IDs, names, and types.

        Key values are not returned. Requires a
        full-access private key; read-only keys receive 403.
        """
        return self._get(
            "/v1/project/keys",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"secret_key": True},
            ),
            cast_to=ProjectKeys,
        )

    def rotate(
        self,
        key_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RotatedProjectKey:
        """Replace a key in this project.

        The old value stops working immediately. Save the
        returned replacement. Requires a full-access private key; read-only keys
        receive 403. Only the selected key is rotated. If its replacement is lost, a
        trusted backend can rotate it again through the installation admin API.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        return self._post(
            path_template("/v1/project/keys/{key_id}/rotate", key_id=key_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"secret_key": True},
            ),
            cast_to=RotatedProjectKey,
        )


class AsyncKeysResource(AsyncAPIResource):
    """Project origins and keys."""

    @cached_property
    def with_raw_response(self) -> AsyncKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-analytics-python#with_streaming_response
        """
        return AsyncKeysResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        permission: Literal["public", "secret"],
        read_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreatedProjectKey:
        """
        Create a named public ingestion key or secret key in the authenticated project.
        Secret keys default to full project access; set read_only to true for analytics
        reads and exports only. Requires a full-access project secret key. Read-only
        keys receive 403 and the installation admin key is not accepted. The key is
        active immediately and its value is returned once; store it before leaving this
        response. Each project supports at most 64 active keys, including its initial
        keys.

        Args:
          name: Key display name, up to 128 UTF-8 bytes. Whitespace-only names are rejected.

          read_only: Only secret keys can be read-only. False grants full project management access
              to secret keys; public keys only ingest events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/project/keys",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "permission": permission,
                    "read_only": read_only,
                },
                key_create_params.KeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"secret_key": True},
            ),
            cast_to=CreatedProjectKey,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectKeys:
        """List key IDs, names, and types.

        Key values are not returned. Requires a
        full-access private key; read-only keys receive 403.
        """
        return await self._get(
            "/v1/project/keys",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"secret_key": True},
            ),
            cast_to=ProjectKeys,
        )

    async def rotate(
        self,
        key_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RotatedProjectKey:
        """Replace a key in this project.

        The old value stops working immediately. Save the
        returned replacement. Requires a full-access private key; read-only keys
        receive 403. Only the selected key is rotated. If its replacement is lost, a
        trusted backend can rotate it again through the installation admin API.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        return await self._post(
            path_template("/v1/project/keys/{key_id}/rotate", key_id=key_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"secret_key": True},
            ),
            cast_to=RotatedProjectKey,
        )


class KeysResourceWithRawResponse:
    def __init__(self, keys: KeysResource) -> None:
        self._keys = keys

        self.create = to_raw_response_wrapper(
            keys.create,
        )
        self.list = to_raw_response_wrapper(
            keys.list,
        )
        self.rotate = to_raw_response_wrapper(
            keys.rotate,
        )


class AsyncKeysResourceWithRawResponse:
    def __init__(self, keys: AsyncKeysResource) -> None:
        self._keys = keys

        self.create = async_to_raw_response_wrapper(
            keys.create,
        )
        self.list = async_to_raw_response_wrapper(
            keys.list,
        )
        self.rotate = async_to_raw_response_wrapper(
            keys.rotate,
        )


class KeysResourceWithStreamingResponse:
    def __init__(self, keys: KeysResource) -> None:
        self._keys = keys

        self.create = to_streamed_response_wrapper(
            keys.create,
        )
        self.list = to_streamed_response_wrapper(
            keys.list,
        )
        self.rotate = to_streamed_response_wrapper(
            keys.rotate,
        )


class AsyncKeysResourceWithStreamingResponse:
    def __init__(self, keys: AsyncKeysResource) -> None:
        self._keys = keys

        self.create = async_to_streamed_response_wrapper(
            keys.create,
        )
        self.list = async_to_streamed_response_wrapper(
            keys.list,
        )
        self.rotate = async_to_streamed_response_wrapper(
            keys.rotate,
        )
