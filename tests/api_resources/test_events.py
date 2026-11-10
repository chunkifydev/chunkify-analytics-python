# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from chunkify_analytics import ChunkifyAnalytics, AsyncChunkifyAnalytics
from chunkify_analytics.types import (
    StoredEvent,
    EventIngestResponse,
)
from chunkify_analytics._utils import parse_datetime
from chunkify_analytics.pagination import SyncEventsPage, AsyncEventsPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: ChunkifyAnalytics) -> None:
        event = client.events.list()
        assert_matches_type(SyncEventsPage[StoredEvent], event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: ChunkifyAnalytics) -> None:
        event = client.events.list(
            browser_name="x",
            city="x",
            continent="AF",
            country="SE",
            cursor="cursor",
            device_type="desktop",
            event_name="chunkify.video.view_started",
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            order="asc",
            os_name="x",
            page_origin="x",
            page_path="x",
            playback_rate="269125115713",
            subtitle_language="P",
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
            user_id="x",
            video_id="P",
            video_title="x",
            view_id="x",
            viewer_id="x",
        )
        assert_matches_type(SyncEventsPage[StoredEvent], event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: ChunkifyAnalytics) -> None:
        response = client.events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(SyncEventsPage[StoredEvent], event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: ChunkifyAnalytics) -> None:
        with client.events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(SyncEventsPage[StoredEvent], event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_ingest(self, client: ChunkifyAnalytics) -> None:
        event = client.events.ingest(
            event={
                "connector_name": "html-media",
                "connector_version": None,
                "delivery_hostname": None,
                "delivery_request_count": None,
                "delivery_throughput_bps": None,
                "delivery_transferred_bytes": None,
                "dropped_video_frames": None,
                "environment": None,
                "error_category": None,
                "error_code": "string",
                "error_fatal": None,
                "error_playhead_seconds": None,
                "event_id": "35c9ab04-7c09-4c09-ae70-a214f4a637c0",
                "event_name": "chunkify.video.view_started",
                "first_video_frame_time_ms": None,
                "furthest_progress_ratio": None,
                "maximum_playhead_seconds": 0,
                "media_duration_seconds": None,
                "media_height_px": None,
                "media_width_px": None,
                "occurred_at": parse_datetime("2026-10-19T12:00:00.000Z"),
                "player_height_px": None,
                "player_name": None,
                "player_version": None,
                "player_width_px": None,
                "playing_time_ms": 0,
                "reason": None,
                "rebuffer_count": 0,
                "rebuffer_duration_ms": 0,
                "rebuffer_ratio": None,
                "rendition_playing_time": [
                    {
                        "bitrate_bps": 0,
                        "codec": "codec",
                        "frame_rate": 0,
                        "height": 0,
                        "playing_time_ms": 0,
                        "width": 0,
                    }
                ],
                "rendition_switch_count": None,
                "schema_version": 1,
                "sdk_name": "@chunkify/player-analytics",
                "sdk_version": "0.3.0",
                "seek_count": 0,
                "seek_duration_ms": 0,
                "selected_rendition_bitrate_bps": None,
                "selected_rendition_codec": None,
                "selected_rendition_height": None,
                "selected_rendition_width": None,
                "sequence": 1,
                "startup_outcome": None,
                "startup_time_ms": None,
                "total_video_frames": None,
                "video_id": "demo-video",
                "view_id": "616992d2-6db6-4578-8361-3f8813e963be",
                "viewer_id": None,
            },
        )
        assert_matches_type(EventIngestResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_ingest_with_all_params(self, client: ChunkifyAnalytics) -> None:
        event = client.events.ingest(
            event={
                "connector_name": "html-media",
                "connector_version": None,
                "delivery_hostname": None,
                "delivery_request_count": None,
                "delivery_throughput_bps": None,
                "delivery_transferred_bytes": None,
                "dropped_video_frames": None,
                "environment": None,
                "error_category": None,
                "error_code": "string",
                "error_fatal": None,
                "error_playhead_seconds": None,
                "event_id": "35c9ab04-7c09-4c09-ae70-a214f4a637c0",
                "event_name": "chunkify.video.view_started",
                "first_video_frame_time_ms": None,
                "furthest_progress_ratio": None,
                "maximum_playhead_seconds": 0,
                "media_duration_seconds": None,
                "media_height_px": None,
                "media_width_px": None,
                "occurred_at": parse_datetime("2026-10-19T12:00:00.000Z"),
                "player_height_px": None,
                "player_name": None,
                "player_version": None,
                "player_width_px": None,
                "playing_time_ms": 0,
                "reason": None,
                "rebuffer_count": 0,
                "rebuffer_duration_ms": 0,
                "rebuffer_ratio": None,
                "rendition_playing_time": [
                    {
                        "bitrate_bps": 0,
                        "codec": "codec",
                        "frame_rate": 0,
                        "height": 0,
                        "playing_time_ms": 0,
                        "width": 0,
                    }
                ],
                "rendition_switch_count": None,
                "schema_version": 1,
                "sdk_name": "@chunkify/player-analytics",
                "sdk_version": "0.3.0",
                "seek_count": 0,
                "seek_duration_ms": 0,
                "selected_rendition_bitrate_bps": None,
                "selected_rendition_codec": None,
                "selected_rendition_height": None,
                "selected_rendition_width": None,
                "sequence": 1,
                "startup_outcome": None,
                "startup_time_ms": None,
                "total_video_frames": None,
                "video_id": "demo-video",
                "view_id": "616992d2-6db6-4578-8361-3f8813e963be",
                "viewer_id": None,
                "browser_context": {},
                "custom": {
                    "plan": "premium",
                    "ab_test": "B",
                    "seats": 5,
                    "trial": False,
                },
                "playback_rate": 0.01,
                "playback_rate_playing_time": [
                    {
                        "playing_time_ms": 0,
                        "rate": 0.01,
                    }
                ],
                "played_ranges": [
                    {
                        "end_seconds": 0,
                        "start_seconds": 0,
                    }
                ],
                "playhead_seconds": 0,
                "subtitle_language": "P",
                "subtitle_playing_time": [
                    {
                        "language": "P",
                        "playing_time_ms": 0,
                    }
                ],
                "user_id": "x",
                "video_title": "x",
                "visibility_state": "visible",
            },
            content_encoding="identity",
            origin="Origin",
        )
        assert_matches_type(EventIngestResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_ingest(self, client: ChunkifyAnalytics) -> None:
        response = client.events.with_raw_response.ingest(
            event={
                "connector_name": "html-media",
                "connector_version": None,
                "delivery_hostname": None,
                "delivery_request_count": None,
                "delivery_throughput_bps": None,
                "delivery_transferred_bytes": None,
                "dropped_video_frames": None,
                "environment": None,
                "error_category": None,
                "error_code": "string",
                "error_fatal": None,
                "error_playhead_seconds": None,
                "event_id": "35c9ab04-7c09-4c09-ae70-a214f4a637c0",
                "event_name": "chunkify.video.view_started",
                "first_video_frame_time_ms": None,
                "furthest_progress_ratio": None,
                "maximum_playhead_seconds": 0,
                "media_duration_seconds": None,
                "media_height_px": None,
                "media_width_px": None,
                "occurred_at": parse_datetime("2026-10-19T12:00:00.000Z"),
                "player_height_px": None,
                "player_name": None,
                "player_version": None,
                "player_width_px": None,
                "playing_time_ms": 0,
                "reason": None,
                "rebuffer_count": 0,
                "rebuffer_duration_ms": 0,
                "rebuffer_ratio": None,
                "rendition_playing_time": [
                    {
                        "bitrate_bps": 0,
                        "codec": "codec",
                        "frame_rate": 0,
                        "height": 0,
                        "playing_time_ms": 0,
                        "width": 0,
                    }
                ],
                "rendition_switch_count": None,
                "schema_version": 1,
                "sdk_name": "@chunkify/player-analytics",
                "sdk_version": "0.3.0",
                "seek_count": 0,
                "seek_duration_ms": 0,
                "selected_rendition_bitrate_bps": None,
                "selected_rendition_codec": None,
                "selected_rendition_height": None,
                "selected_rendition_width": None,
                "sequence": 1,
                "startup_outcome": None,
                "startup_time_ms": None,
                "total_video_frames": None,
                "video_id": "demo-video",
                "view_id": "616992d2-6db6-4578-8361-3f8813e963be",
                "viewer_id": None,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventIngestResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_ingest(self, client: ChunkifyAnalytics) -> None:
        with client.events.with_streaming_response.ingest(
            event={
                "connector_name": "html-media",
                "connector_version": None,
                "delivery_hostname": None,
                "delivery_request_count": None,
                "delivery_throughput_bps": None,
                "delivery_transferred_bytes": None,
                "dropped_video_frames": None,
                "environment": None,
                "error_category": None,
                "error_code": "string",
                "error_fatal": None,
                "error_playhead_seconds": None,
                "event_id": "35c9ab04-7c09-4c09-ae70-a214f4a637c0",
                "event_name": "chunkify.video.view_started",
                "first_video_frame_time_ms": None,
                "furthest_progress_ratio": None,
                "maximum_playhead_seconds": 0,
                "media_duration_seconds": None,
                "media_height_px": None,
                "media_width_px": None,
                "occurred_at": parse_datetime("2026-10-19T12:00:00.000Z"),
                "player_height_px": None,
                "player_name": None,
                "player_version": None,
                "player_width_px": None,
                "playing_time_ms": 0,
                "reason": None,
                "rebuffer_count": 0,
                "rebuffer_duration_ms": 0,
                "rebuffer_ratio": None,
                "rendition_playing_time": [
                    {
                        "bitrate_bps": 0,
                        "codec": "codec",
                        "frame_rate": 0,
                        "height": 0,
                        "playing_time_ms": 0,
                        "width": 0,
                    }
                ],
                "rendition_switch_count": None,
                "schema_version": 1,
                "sdk_name": "@chunkify/player-analytics",
                "sdk_version": "0.3.0",
                "seek_count": 0,
                "seek_duration_ms": 0,
                "selected_rendition_bitrate_bps": None,
                "selected_rendition_codec": None,
                "selected_rendition_height": None,
                "selected_rendition_width": None,
                "sequence": 1,
                "startup_outcome": None,
                "startup_time_ms": None,
                "total_video_frames": None,
                "video_id": "demo-video",
                "view_id": "616992d2-6db6-4578-8361-3f8813e963be",
                "viewer_id": None,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(EventIngestResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEvents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncChunkifyAnalytics) -> None:
        event = await async_client.events.list()
        assert_matches_type(AsyncEventsPage[StoredEvent], event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncChunkifyAnalytics) -> None:
        event = await async_client.events.list(
            browser_name="x",
            city="x",
            continent="AF",
            country="SE",
            cursor="cursor",
            device_type="desktop",
            event_name="chunkify.video.view_started",
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            order="asc",
            os_name="x",
            page_origin="x",
            page_path="x",
            playback_rate="269125115713",
            subtitle_language="P",
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
            user_id="x",
            video_id="P",
            video_title="x",
            view_id="x",
            viewer_id="x",
        )
        assert_matches_type(AsyncEventsPage[StoredEvent], event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncChunkifyAnalytics) -> None:
        response = await async_client.events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(AsyncEventsPage[StoredEvent], event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncChunkifyAnalytics) -> None:
        async with async_client.events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(AsyncEventsPage[StoredEvent], event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_ingest(self, async_client: AsyncChunkifyAnalytics) -> None:
        event = await async_client.events.ingest(
            event={
                "connector_name": "html-media",
                "connector_version": None,
                "delivery_hostname": None,
                "delivery_request_count": None,
                "delivery_throughput_bps": None,
                "delivery_transferred_bytes": None,
                "dropped_video_frames": None,
                "environment": None,
                "error_category": None,
                "error_code": "string",
                "error_fatal": None,
                "error_playhead_seconds": None,
                "event_id": "35c9ab04-7c09-4c09-ae70-a214f4a637c0",
                "event_name": "chunkify.video.view_started",
                "first_video_frame_time_ms": None,
                "furthest_progress_ratio": None,
                "maximum_playhead_seconds": 0,
                "media_duration_seconds": None,
                "media_height_px": None,
                "media_width_px": None,
                "occurred_at": parse_datetime("2026-10-19T12:00:00.000Z"),
                "player_height_px": None,
                "player_name": None,
                "player_version": None,
                "player_width_px": None,
                "playing_time_ms": 0,
                "reason": None,
                "rebuffer_count": 0,
                "rebuffer_duration_ms": 0,
                "rebuffer_ratio": None,
                "rendition_playing_time": [
                    {
                        "bitrate_bps": 0,
                        "codec": "codec",
                        "frame_rate": 0,
                        "height": 0,
                        "playing_time_ms": 0,
                        "width": 0,
                    }
                ],
                "rendition_switch_count": None,
                "schema_version": 1,
                "sdk_name": "@chunkify/player-analytics",
                "sdk_version": "0.3.0",
                "seek_count": 0,
                "seek_duration_ms": 0,
                "selected_rendition_bitrate_bps": None,
                "selected_rendition_codec": None,
                "selected_rendition_height": None,
                "selected_rendition_width": None,
                "sequence": 1,
                "startup_outcome": None,
                "startup_time_ms": None,
                "total_video_frames": None,
                "video_id": "demo-video",
                "view_id": "616992d2-6db6-4578-8361-3f8813e963be",
                "viewer_id": None,
            },
        )
        assert_matches_type(EventIngestResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_ingest_with_all_params(self, async_client: AsyncChunkifyAnalytics) -> None:
        event = await async_client.events.ingest(
            event={
                "connector_name": "html-media",
                "connector_version": None,
                "delivery_hostname": None,
                "delivery_request_count": None,
                "delivery_throughput_bps": None,
                "delivery_transferred_bytes": None,
                "dropped_video_frames": None,
                "environment": None,
                "error_category": None,
                "error_code": "string",
                "error_fatal": None,
                "error_playhead_seconds": None,
                "event_id": "35c9ab04-7c09-4c09-ae70-a214f4a637c0",
                "event_name": "chunkify.video.view_started",
                "first_video_frame_time_ms": None,
                "furthest_progress_ratio": None,
                "maximum_playhead_seconds": 0,
                "media_duration_seconds": None,
                "media_height_px": None,
                "media_width_px": None,
                "occurred_at": parse_datetime("2026-10-19T12:00:00.000Z"),
                "player_height_px": None,
                "player_name": None,
                "player_version": None,
                "player_width_px": None,
                "playing_time_ms": 0,
                "reason": None,
                "rebuffer_count": 0,
                "rebuffer_duration_ms": 0,
                "rebuffer_ratio": None,
                "rendition_playing_time": [
                    {
                        "bitrate_bps": 0,
                        "codec": "codec",
                        "frame_rate": 0,
                        "height": 0,
                        "playing_time_ms": 0,
                        "width": 0,
                    }
                ],
                "rendition_switch_count": None,
                "schema_version": 1,
                "sdk_name": "@chunkify/player-analytics",
                "sdk_version": "0.3.0",
                "seek_count": 0,
                "seek_duration_ms": 0,
                "selected_rendition_bitrate_bps": None,
                "selected_rendition_codec": None,
                "selected_rendition_height": None,
                "selected_rendition_width": None,
                "sequence": 1,
                "startup_outcome": None,
                "startup_time_ms": None,
                "total_video_frames": None,
                "video_id": "demo-video",
                "view_id": "616992d2-6db6-4578-8361-3f8813e963be",
                "viewer_id": None,
                "browser_context": {},
                "custom": {
                    "plan": "premium",
                    "ab_test": "B",
                    "seats": 5,
                    "trial": False,
                },
                "playback_rate": 0.01,
                "playback_rate_playing_time": [
                    {
                        "playing_time_ms": 0,
                        "rate": 0.01,
                    }
                ],
                "played_ranges": [
                    {
                        "end_seconds": 0,
                        "start_seconds": 0,
                    }
                ],
                "playhead_seconds": 0,
                "subtitle_language": "P",
                "subtitle_playing_time": [
                    {
                        "language": "P",
                        "playing_time_ms": 0,
                    }
                ],
                "user_id": "x",
                "video_title": "x",
                "visibility_state": "visible",
            },
            content_encoding="identity",
            origin="Origin",
        )
        assert_matches_type(EventIngestResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_ingest(self, async_client: AsyncChunkifyAnalytics) -> None:
        response = await async_client.events.with_raw_response.ingest(
            event={
                "connector_name": "html-media",
                "connector_version": None,
                "delivery_hostname": None,
                "delivery_request_count": None,
                "delivery_throughput_bps": None,
                "delivery_transferred_bytes": None,
                "dropped_video_frames": None,
                "environment": None,
                "error_category": None,
                "error_code": "string",
                "error_fatal": None,
                "error_playhead_seconds": None,
                "event_id": "35c9ab04-7c09-4c09-ae70-a214f4a637c0",
                "event_name": "chunkify.video.view_started",
                "first_video_frame_time_ms": None,
                "furthest_progress_ratio": None,
                "maximum_playhead_seconds": 0,
                "media_duration_seconds": None,
                "media_height_px": None,
                "media_width_px": None,
                "occurred_at": parse_datetime("2026-10-19T12:00:00.000Z"),
                "player_height_px": None,
                "player_name": None,
                "player_version": None,
                "player_width_px": None,
                "playing_time_ms": 0,
                "reason": None,
                "rebuffer_count": 0,
                "rebuffer_duration_ms": 0,
                "rebuffer_ratio": None,
                "rendition_playing_time": [
                    {
                        "bitrate_bps": 0,
                        "codec": "codec",
                        "frame_rate": 0,
                        "height": 0,
                        "playing_time_ms": 0,
                        "width": 0,
                    }
                ],
                "rendition_switch_count": None,
                "schema_version": 1,
                "sdk_name": "@chunkify/player-analytics",
                "sdk_version": "0.3.0",
                "seek_count": 0,
                "seek_duration_ms": 0,
                "selected_rendition_bitrate_bps": None,
                "selected_rendition_codec": None,
                "selected_rendition_height": None,
                "selected_rendition_width": None,
                "sequence": 1,
                "startup_outcome": None,
                "startup_time_ms": None,
                "total_video_frames": None,
                "video_id": "demo-video",
                "view_id": "616992d2-6db6-4578-8361-3f8813e963be",
                "viewer_id": None,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(EventIngestResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_ingest(self, async_client: AsyncChunkifyAnalytics) -> None:
        async with async_client.events.with_streaming_response.ingest(
            event={
                "connector_name": "html-media",
                "connector_version": None,
                "delivery_hostname": None,
                "delivery_request_count": None,
                "delivery_throughput_bps": None,
                "delivery_transferred_bytes": None,
                "dropped_video_frames": None,
                "environment": None,
                "error_category": None,
                "error_code": "string",
                "error_fatal": None,
                "error_playhead_seconds": None,
                "event_id": "35c9ab04-7c09-4c09-ae70-a214f4a637c0",
                "event_name": "chunkify.video.view_started",
                "first_video_frame_time_ms": None,
                "furthest_progress_ratio": None,
                "maximum_playhead_seconds": 0,
                "media_duration_seconds": None,
                "media_height_px": None,
                "media_width_px": None,
                "occurred_at": parse_datetime("2026-10-19T12:00:00.000Z"),
                "player_height_px": None,
                "player_name": None,
                "player_version": None,
                "player_width_px": None,
                "playing_time_ms": 0,
                "reason": None,
                "rebuffer_count": 0,
                "rebuffer_duration_ms": 0,
                "rebuffer_ratio": None,
                "rendition_playing_time": [
                    {
                        "bitrate_bps": 0,
                        "codec": "codec",
                        "frame_rate": 0,
                        "height": 0,
                        "playing_time_ms": 0,
                        "width": 0,
                    }
                ],
                "rendition_switch_count": None,
                "schema_version": 1,
                "sdk_name": "@chunkify/player-analytics",
                "sdk_version": "0.3.0",
                "seek_count": 0,
                "seek_duration_ms": 0,
                "selected_rendition_bitrate_bps": None,
                "selected_rendition_codec": None,
                "selected_rendition_height": None,
                "selected_rendition_width": None,
                "sequence": 1,
                "startup_outcome": None,
                "startup_time_ms": None,
                "total_video_frames": None,
                "video_id": "demo-video",
                "view_id": "616992d2-6db6-4578-8361-3f8813e963be",
                "viewer_id": None,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(EventIngestResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True
