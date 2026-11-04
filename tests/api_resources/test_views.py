# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from chunkify_analytics import ChunkifyAnalytics, AsyncChunkifyAnalytics
from chunkify_analytics.types import View, ViewDetail
from chunkify_analytics._utils import parse_datetime
from chunkify_analytics.pagination import SyncViewsPage, AsyncViewsPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestViews:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: ChunkifyAnalytics) -> None:
        view = client.views.retrieve(
            view_id="x",
        )
        assert_matches_type(ViewDetail, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: ChunkifyAnalytics) -> None:
        view = client.views.retrieve(
            view_id="x",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(ViewDetail, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: ChunkifyAnalytics) -> None:
        response = client.views.with_raw_response.retrieve(
            view_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = response.parse()
        assert_matches_type(ViewDetail, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: ChunkifyAnalytics) -> None:
        with client.views.with_streaming_response.retrieve(
            view_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = response.parse()
            assert_matches_type(ViewDetail, view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: ChunkifyAnalytics) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            client.views.with_raw_response.retrieve(
                view_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: ChunkifyAnalytics) -> None:
        view = client.views.list()
        assert_matches_type(SyncViewsPage[View], view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: ChunkifyAnalytics) -> None:
        view = client.views.list(
            browser_name="x",
            city="x",
            continent="AF",
            country="SE",
            cursor="cursor",
            device_type="desktop",
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            has_fatal_error=True,
            limit=1,
            order="asc",
            os_name="x",
            page_origin="x",
            page_path="x",
            sort_by="started_at",
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
            video_id="video_id",
            view_id="x",
            viewer_id="viewer_id",
        )
        assert_matches_type(SyncViewsPage[View], view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: ChunkifyAnalytics) -> None:
        response = client.views.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = response.parse()
        assert_matches_type(SyncViewsPage[View], view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: ChunkifyAnalytics) -> None:
        with client.views.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = response.parse()
            assert_matches_type(SyncViewsPage[View], view, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncViews:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncChunkifyAnalytics) -> None:
        view = await async_client.views.retrieve(
            view_id="x",
        )
        assert_matches_type(ViewDetail, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncChunkifyAnalytics) -> None:
        view = await async_client.views.retrieve(
            view_id="x",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(ViewDetail, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncChunkifyAnalytics) -> None:
        response = await async_client.views.with_raw_response.retrieve(
            view_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = await response.parse()
        assert_matches_type(ViewDetail, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncChunkifyAnalytics) -> None:
        async with async_client.views.with_streaming_response.retrieve(
            view_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = await response.parse()
            assert_matches_type(ViewDetail, view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncChunkifyAnalytics) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            await async_client.views.with_raw_response.retrieve(
                view_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncChunkifyAnalytics) -> None:
        view = await async_client.views.list()
        assert_matches_type(AsyncViewsPage[View], view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncChunkifyAnalytics) -> None:
        view = await async_client.views.list(
            browser_name="x",
            city="x",
            continent="AF",
            country="SE",
            cursor="cursor",
            device_type="desktop",
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            has_fatal_error=True,
            limit=1,
            order="asc",
            os_name="x",
            page_origin="x",
            page_path="x",
            sort_by="started_at",
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
            video_id="video_id",
            view_id="x",
            viewer_id="viewer_id",
        )
        assert_matches_type(AsyncViewsPage[View], view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncChunkifyAnalytics) -> None:
        response = await async_client.views.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = await response.parse()
        assert_matches_type(AsyncViewsPage[View], view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncChunkifyAnalytics) -> None:
        async with async_client.views.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = await response.parse()
            assert_matches_type(AsyncViewsPage[View], view, path=["response"])

        assert cast(Any, response.is_closed) is True
