# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from chunkify_analytics import ChunkifyAnalytics, AsyncChunkifyAnalytics
from chunkify_analytics.types import (
    Export,
    ExportColumns,
)
from chunkify_analytics._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: ChunkifyAnalytics) -> None:
        export = client.exports.create(
            resource="videos",
        )
        assert_matches_type(Export, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: ChunkifyAnalytics) -> None:
        export = client.exports.create(
            resource="videos",
            columns=["x"],
            query={
                "browser_name": "x",
                "city": "x",
                "continent": "AF",
                "country": "SE",
                "device_type": "desktop",
                "dimension": "browser_name",
                "event_name": "chunkify.video.view_started",
                "from": parse_datetime("2019-12-27T18:11:19.117Z"),
                "group_by": "browser_name",
                "has_fatal_error": True,
                "interval": "hour",
                "kind": "summary",
                "order": "desc",
                "os_name": "x",
                "page_origin": "x",
                "page_path": "x",
                "sort_by": "views",
                "to": parse_datetime("2019-12-27T18:11:19.117Z"),
                "video_id": "video_id",
                "view_id": "x",
                "viewer_id": "viewer_id",
            },
        )
        assert_matches_type(Export, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: ChunkifyAnalytics) -> None:
        response = client.exports.with_raw_response.create(
            resource="videos",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = response.parse()
        assert_matches_type(Export, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: ChunkifyAnalytics) -> None:
        with client.exports.with_streaming_response.create(
            resource="videos",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = response.parse()
            assert_matches_type(Export, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_download(self, client: ChunkifyAnalytics) -> None:
        export = client.exports.download(
            "2e-xAv1b-zE_-N_eC1_0f_sO_-a-i_D--_3f-__c703",
        )
        assert_matches_type(str, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_download(self, client: ChunkifyAnalytics) -> None:
        response = client.exports.with_raw_response.download(
            "2e-xAv1b-zE_-N_eC1_0f_sO_-a-i_D--_3f-__c703",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = response.parse()
        assert_matches_type(str, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_download(self, client: ChunkifyAnalytics) -> None:
        with client.exports.with_streaming_response.download(
            "2e-xAv1b-zE_-N_eC1_0f_sO_-a-i_D--_3f-__c703",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = response.parse()
            assert_matches_type(str, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_download(self, client: ChunkifyAnalytics) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
            client.exports.with_raw_response.download(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_columns(self, client: ChunkifyAnalytics) -> None:
        export = client.exports.list_columns(
            resource="summary",
        )
        assert_matches_type(ExportColumns, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_columns_with_all_params(self, client: ChunkifyAnalytics) -> None:
        export = client.exports.list_columns(
            resource="summary",
            group_by="browser_name",
            kind="summary",
        )
        assert_matches_type(ExportColumns, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_columns(self, client: ChunkifyAnalytics) -> None:
        response = client.exports.with_raw_response.list_columns(
            resource="summary",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = response.parse()
        assert_matches_type(ExportColumns, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_columns(self, client: ChunkifyAnalytics) -> None:
        with client.exports.with_streaming_response.list_columns(
            resource="summary",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = response.parse()
            assert_matches_type(ExportColumns, export, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExports:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncChunkifyAnalytics) -> None:
        export = await async_client.exports.create(
            resource="videos",
        )
        assert_matches_type(Export, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncChunkifyAnalytics) -> None:
        export = await async_client.exports.create(
            resource="videos",
            columns=["x"],
            query={
                "browser_name": "x",
                "city": "x",
                "continent": "AF",
                "country": "SE",
                "device_type": "desktop",
                "dimension": "browser_name",
                "event_name": "chunkify.video.view_started",
                "from": parse_datetime("2019-12-27T18:11:19.117Z"),
                "group_by": "browser_name",
                "has_fatal_error": True,
                "interval": "hour",
                "kind": "summary",
                "order": "desc",
                "os_name": "x",
                "page_origin": "x",
                "page_path": "x",
                "sort_by": "views",
                "to": parse_datetime("2019-12-27T18:11:19.117Z"),
                "video_id": "video_id",
                "view_id": "x",
                "viewer_id": "viewer_id",
            },
        )
        assert_matches_type(Export, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncChunkifyAnalytics) -> None:
        response = await async_client.exports.with_raw_response.create(
            resource="videos",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = await response.parse()
        assert_matches_type(Export, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncChunkifyAnalytics) -> None:
        async with async_client.exports.with_streaming_response.create(
            resource="videos",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = await response.parse()
            assert_matches_type(Export, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_download(self, async_client: AsyncChunkifyAnalytics) -> None:
        export = await async_client.exports.download(
            "2e-xAv1b-zE_-N_eC1_0f_sO_-a-i_D--_3f-__c703",
        )
        assert_matches_type(str, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_download(self, async_client: AsyncChunkifyAnalytics) -> None:
        response = await async_client.exports.with_raw_response.download(
            "2e-xAv1b-zE_-N_eC1_0f_sO_-a-i_D--_3f-__c703",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = await response.parse()
        assert_matches_type(str, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_download(self, async_client: AsyncChunkifyAnalytics) -> None:
        async with async_client.exports.with_streaming_response.download(
            "2e-xAv1b-zE_-N_eC1_0f_sO_-a-i_D--_3f-__c703",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = await response.parse()
            assert_matches_type(str, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_download(self, async_client: AsyncChunkifyAnalytics) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
            await async_client.exports.with_raw_response.download(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_columns(self, async_client: AsyncChunkifyAnalytics) -> None:
        export = await async_client.exports.list_columns(
            resource="summary",
        )
        assert_matches_type(ExportColumns, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_columns_with_all_params(self, async_client: AsyncChunkifyAnalytics) -> None:
        export = await async_client.exports.list_columns(
            resource="summary",
            group_by="browser_name",
            kind="summary",
        )
        assert_matches_type(ExportColumns, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_columns(self, async_client: AsyncChunkifyAnalytics) -> None:
        response = await async_client.exports.with_raw_response.list_columns(
            resource="summary",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = await response.parse()
        assert_matches_type(ExportColumns, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_columns(self, async_client: AsyncChunkifyAnalytics) -> None:
        async with async_client.exports.with_streaming_response.list_columns(
            resource="summary",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = await response.parse()
            assert_matches_type(ExportColumns, export, path=["response"])

        assert cast(Any, response.is_closed) is True
