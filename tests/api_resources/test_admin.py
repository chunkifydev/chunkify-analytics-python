# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from chunkify_analytics import ChunkifyAnalytics, AsyncChunkifyAnalytics
from chunkify_analytics.types import CreatedProject

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdmin:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_project(self, client: ChunkifyAnalytics) -> None:
        admin = client.admin.create_project(
            name="Customer website",
        )
        assert_matches_type(CreatedProject, admin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_project_with_all_params(self, client: ChunkifyAnalytics) -> None:
        admin = client.admin.create_project(
            name="Customer website",
            allowed_origins=["https://customer.example"],
            retention_seconds=2592000,
        )
        assert_matches_type(CreatedProject, admin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_project(self, client: ChunkifyAnalytics) -> None:
        response = client.admin.with_raw_response.create_project(
            name="Customer website",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(CreatedProject, admin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_project(self, client: ChunkifyAnalytics) -> None:
        with client.admin.with_streaming_response.create_project(
            name="Customer website",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = response.parse()
            assert_matches_type(CreatedProject, admin, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAdmin:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_project(self, async_client: AsyncChunkifyAnalytics) -> None:
        admin = await async_client.admin.create_project(
            name="Customer website",
        )
        assert_matches_type(CreatedProject, admin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_project_with_all_params(self, async_client: AsyncChunkifyAnalytics) -> None:
        admin = await async_client.admin.create_project(
            name="Customer website",
            allowed_origins=["https://customer.example"],
            retention_seconds=2592000,
        )
        assert_matches_type(CreatedProject, admin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_project(self, async_client: AsyncChunkifyAnalytics) -> None:
        response = await async_client.admin.with_raw_response.create_project(
            name="Customer website",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = await response.parse()
        assert_matches_type(CreatedProject, admin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_project(self, async_client: AsyncChunkifyAnalytics) -> None:
        async with async_client.admin.with_streaming_response.create_project(
            name="Customer website",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = await response.parse()
            assert_matches_type(CreatedProject, admin, path=["response"])

        assert cast(Any, response.is_closed) is True
