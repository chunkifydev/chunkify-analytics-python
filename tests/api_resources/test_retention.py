# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from chunkify_analytics import ChunkifyAnalytics, AsyncChunkifyAnalytics
from chunkify_analytics.types import RetentionReport
from chunkify_analytics._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRetention:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: ChunkifyAnalytics) -> None:
        retention = client.retention.retrieve(
            video_id="video_id",
        )
        assert_matches_type(RetentionReport, retention, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: ChunkifyAnalytics) -> None:
        retention = client.retention.retrieve(
            video_id="video_id",
            browser_name="x",
            city="x",
            continent="AF",
            country="SE",
            device_type="desktop",
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            os_name="x",
            page_origin="x",
            page_path="x",
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
            view_id="x",
            viewer_id="viewer_id",
        )
        assert_matches_type(RetentionReport, retention, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: ChunkifyAnalytics) -> None:
        response = client.retention.with_raw_response.retrieve(
            video_id="video_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retention = response.parse()
        assert_matches_type(RetentionReport, retention, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: ChunkifyAnalytics) -> None:
        with client.retention.with_streaming_response.retrieve(
            video_id="video_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retention = response.parse()
            assert_matches_type(RetentionReport, retention, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRetention:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncChunkifyAnalytics) -> None:
        retention = await async_client.retention.retrieve(
            video_id="video_id",
        )
        assert_matches_type(RetentionReport, retention, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncChunkifyAnalytics) -> None:
        retention = await async_client.retention.retrieve(
            video_id="video_id",
            browser_name="x",
            city="x",
            continent="AF",
            country="SE",
            device_type="desktop",
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            os_name="x",
            page_origin="x",
            page_path="x",
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
            view_id="x",
            viewer_id="viewer_id",
        )
        assert_matches_type(RetentionReport, retention, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncChunkifyAnalytics) -> None:
        response = await async_client.retention.with_raw_response.retrieve(
            video_id="video_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retention = await response.parse()
        assert_matches_type(RetentionReport, retention, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncChunkifyAnalytics) -> None:
        async with async_client.retention.with_streaming_response.retrieve(
            video_id="video_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retention = await response.parse()
            assert_matches_type(RetentionReport, retention, path=["response"])

        assert cast(Any, response.is_closed) is True
