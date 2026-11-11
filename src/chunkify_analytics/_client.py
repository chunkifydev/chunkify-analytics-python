# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._models import SecurityOptions
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        admin,
        views,
        errors,
        events,
        health,
        videos,
        exports,
        project,
        quality,
        summary,
        retention,
        subtitles,
        dimensions,
        engagement,
        renditions,
        timeseries,
        playback_rates,
    )
    from .resources.views import ViewsResource, AsyncViewsResource
    from .resources.errors import ErrorsResource, AsyncErrorsResource
    from .resources.events import EventsResource, AsyncEventsResource
    from .resources.health import HealthResource, AsyncHealthResource
    from .resources.videos import VideosResource, AsyncVideosResource
    from .resources.exports import ExportsResource, AsyncExportsResource
    from .resources.quality import QualityResource, AsyncQualityResource
    from .resources.summary import SummaryResource, AsyncSummaryResource
    from .resources.retention import RetentionResource, AsyncRetentionResource
    from .resources.subtitles import SubtitlesResource, AsyncSubtitlesResource
    from .resources.dimensions import DimensionsResource, AsyncDimensionsResource
    from .resources.engagement import EngagementResource, AsyncEngagementResource
    from .resources.renditions import RenditionsResource, AsyncRenditionsResource
    from .resources.timeseries import TimeseriesResource, AsyncTimeseriesResource
    from .resources.admin.admin import AdminResource, AsyncAdminResource
    from .resources.playback_rates import PlaybackRatesResource, AsyncPlaybackRatesResource
    from .resources.project.project import ProjectResource, AsyncProjectResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "ChunkifyAnalytics",
    "AsyncChunkifyAnalytics",
    "Client",
    "AsyncClient",
]


class ChunkifyAnalytics(SyncAPIClient):
    # client options
    public_key: str | None
    secret_key: str | None
    admin_key: str | None

    def __init__(
        self,
        *,
        public_key: str | None = None,
        secret_key: str | None = None,
        admin_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous ChunkifyAnalytics client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `public_key` from `CHUNKIFY_ANALYTICS_PUBLIC_KEY`
        - `secret_key` from `CHUNKIFY_ANALYTICS_SECRET_KEY`
        - `admin_key` from `CHUNKIFY_ANALYTICS_ADMIN_KEY`
        """
        if public_key is None:
            public_key = os.environ.get("CHUNKIFY_ANALYTICS_PUBLIC_KEY")
        self.public_key = public_key

        if secret_key is None:
            secret_key = os.environ.get("CHUNKIFY_ANALYTICS_SECRET_KEY")
        self.secret_key = secret_key

        if admin_key is None:
            admin_key = os.environ.get("CHUNKIFY_ANALYTICS_ADMIN_KEY")
        self.admin_key = admin_key

        if base_url is None:
            base_url = os.environ.get("CHUNKIFY_ANALYTICS_BASE_URL")
        if base_url is None:
            base_url = f"https://analytics.chunkify.dev"

        custom_headers_env = os.environ.get("CHUNKIFY_ANALYTICS_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def health(self) -> HealthResource:
        """Health and private ingestion status."""
        from .resources.health import HealthResource

        return HealthResource(self)

    @cached_property
    def events(self) -> EventsResource:
        from .resources.events import EventsResource

        return EventsResource(self)

    @cached_property
    def summary(self) -> SummaryResource:
        """Private retained-event and view-cohort queries."""
        from .resources.summary import SummaryResource

        return SummaryResource(self)

    @cached_property
    def videos(self) -> VideosResource:
        """Private retained-event and view-cohort queries."""
        from .resources.videos import VideosResource

        return VideosResource(self)

    @cached_property
    def timeseries(self) -> TimeseriesResource:
        """Private retained-event and view-cohort queries."""
        from .resources.timeseries import TimeseriesResource

        return TimeseriesResource(self)

    @cached_property
    def quality(self) -> QualityResource:
        """Private retained-event and view-cohort queries."""
        from .resources.quality import QualityResource

        return QualityResource(self)

    @cached_property
    def engagement(self) -> EngagementResource:
        """Private retained-event and view-cohort queries."""
        from .resources.engagement import EngagementResource

        return EngagementResource(self)

    @cached_property
    def project(self) -> ProjectResource:
        """Project origins and keys."""
        from .resources.project import ProjectResource

        return ProjectResource(self)

    @cached_property
    def admin(self) -> AdminResource:
        """Project origins and keys."""
        from .resources.admin import AdminResource

        return AdminResource(self)

    @cached_property
    def views(self) -> ViewsResource:
        """Private retained-event and view-cohort queries."""
        from .resources.views import ViewsResource

        return ViewsResource(self)

    @cached_property
    def errors(self) -> ErrorsResource:
        """Private retained-event and view-cohort queries."""
        from .resources.errors import ErrorsResource

        return ErrorsResource(self)

    @cached_property
    def dimensions(self) -> DimensionsResource:
        """Private retained-event and view-cohort queries."""
        from .resources.dimensions import DimensionsResource

        return DimensionsResource(self)

    @cached_property
    def exports(self) -> ExportsResource:
        from .resources.exports import ExportsResource

        return ExportsResource(self)

    @cached_property
    def retention(self) -> RetentionResource:
        """Private retained-event and view-cohort queries."""
        from .resources.retention import RetentionResource

        return RetentionResource(self)

    @cached_property
    def renditions(self) -> RenditionsResource:
        """Private retained-event and view-cohort queries."""
        from .resources.renditions import RenditionsResource

        return RenditionsResource(self)

    @cached_property
    def subtitles(self) -> SubtitlesResource:
        """Private retained-event and view-cohort queries."""
        from .resources.subtitles import SubtitlesResource

        return SubtitlesResource(self)

    @cached_property
    def playback_rates(self) -> PlaybackRatesResource:
        """Private retained-event and view-cohort queries."""
        from .resources.playback_rates import PlaybackRatesResource

        return PlaybackRatesResource(self)

    @cached_property
    def with_raw_response(self) -> ChunkifyAnalyticsWithRawResponse:
        return ChunkifyAnalyticsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChunkifyAnalyticsWithStreamedResponse:
        return ChunkifyAnalyticsWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="repeat")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        headers: dict[str, str] = {}
        if security.get("public_key", False):
            for key, value in self._public_key.items():
                headers.setdefault(key, value)
        if security.get("secret_key", False):
            for key, value in self._secret_key.items():
                headers.setdefault(key, value)
        if security.get("admin_key", False):
            for key, value in self._admin_key.items():
                headers.setdefault(key, value)
        return headers

    @property
    def _public_key(self) -> dict[str, str]:
        public_key = self.public_key
        if public_key is None:
            return {}
        return {"X-Chunkify-Ingest-Key": public_key}

    @property
    def _secret_key(self) -> dict[str, str]:
        secret_key = self.secret_key
        if secret_key is None:
            return {}
        return {"Authorization": f"Bearer {secret_key}"}

    @property
    def _admin_key(self) -> dict[str, str]:
        admin_key = self.admin_key
        if admin_key is None:
            return {}
        return {"Authorization": f"Bearer {admin_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        public_key: str | None = None,
        secret_key: str | None = None,
        admin_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            public_key=public_key or self.public_key,
            secret_key=secret_key or self.secret_key,
            admin_key=admin_key or self.admin_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncChunkifyAnalytics(AsyncAPIClient):
    # client options
    public_key: str | None
    secret_key: str | None
    admin_key: str | None

    def __init__(
        self,
        *,
        public_key: str | None = None,
        secret_key: str | None = None,
        admin_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncChunkifyAnalytics client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `public_key` from `CHUNKIFY_ANALYTICS_PUBLIC_KEY`
        - `secret_key` from `CHUNKIFY_ANALYTICS_SECRET_KEY`
        - `admin_key` from `CHUNKIFY_ANALYTICS_ADMIN_KEY`
        """
        if public_key is None:
            public_key = os.environ.get("CHUNKIFY_ANALYTICS_PUBLIC_KEY")
        self.public_key = public_key

        if secret_key is None:
            secret_key = os.environ.get("CHUNKIFY_ANALYTICS_SECRET_KEY")
        self.secret_key = secret_key

        if admin_key is None:
            admin_key = os.environ.get("CHUNKIFY_ANALYTICS_ADMIN_KEY")
        self.admin_key = admin_key

        if base_url is None:
            base_url = os.environ.get("CHUNKIFY_ANALYTICS_BASE_URL")
        if base_url is None:
            base_url = f"https://analytics.chunkify.dev"

        custom_headers_env = os.environ.get("CHUNKIFY_ANALYTICS_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def health(self) -> AsyncHealthResource:
        """Health and private ingestion status."""
        from .resources.health import AsyncHealthResource

        return AsyncHealthResource(self)

    @cached_property
    def events(self) -> AsyncEventsResource:
        from .resources.events import AsyncEventsResource

        return AsyncEventsResource(self)

    @cached_property
    def summary(self) -> AsyncSummaryResource:
        """Private retained-event and view-cohort queries."""
        from .resources.summary import AsyncSummaryResource

        return AsyncSummaryResource(self)

    @cached_property
    def videos(self) -> AsyncVideosResource:
        """Private retained-event and view-cohort queries."""
        from .resources.videos import AsyncVideosResource

        return AsyncVideosResource(self)

    @cached_property
    def timeseries(self) -> AsyncTimeseriesResource:
        """Private retained-event and view-cohort queries."""
        from .resources.timeseries import AsyncTimeseriesResource

        return AsyncTimeseriesResource(self)

    @cached_property
    def quality(self) -> AsyncQualityResource:
        """Private retained-event and view-cohort queries."""
        from .resources.quality import AsyncQualityResource

        return AsyncQualityResource(self)

    @cached_property
    def engagement(self) -> AsyncEngagementResource:
        """Private retained-event and view-cohort queries."""
        from .resources.engagement import AsyncEngagementResource

        return AsyncEngagementResource(self)

    @cached_property
    def project(self) -> AsyncProjectResource:
        """Project origins and keys."""
        from .resources.project import AsyncProjectResource

        return AsyncProjectResource(self)

    @cached_property
    def admin(self) -> AsyncAdminResource:
        """Project origins and keys."""
        from .resources.admin import AsyncAdminResource

        return AsyncAdminResource(self)

    @cached_property
    def views(self) -> AsyncViewsResource:
        """Private retained-event and view-cohort queries."""
        from .resources.views import AsyncViewsResource

        return AsyncViewsResource(self)

    @cached_property
    def errors(self) -> AsyncErrorsResource:
        """Private retained-event and view-cohort queries."""
        from .resources.errors import AsyncErrorsResource

        return AsyncErrorsResource(self)

    @cached_property
    def dimensions(self) -> AsyncDimensionsResource:
        """Private retained-event and view-cohort queries."""
        from .resources.dimensions import AsyncDimensionsResource

        return AsyncDimensionsResource(self)

    @cached_property
    def exports(self) -> AsyncExportsResource:
        from .resources.exports import AsyncExportsResource

        return AsyncExportsResource(self)

    @cached_property
    def retention(self) -> AsyncRetentionResource:
        """Private retained-event and view-cohort queries."""
        from .resources.retention import AsyncRetentionResource

        return AsyncRetentionResource(self)

    @cached_property
    def renditions(self) -> AsyncRenditionsResource:
        """Private retained-event and view-cohort queries."""
        from .resources.renditions import AsyncRenditionsResource

        return AsyncRenditionsResource(self)

    @cached_property
    def subtitles(self) -> AsyncSubtitlesResource:
        """Private retained-event and view-cohort queries."""
        from .resources.subtitles import AsyncSubtitlesResource

        return AsyncSubtitlesResource(self)

    @cached_property
    def playback_rates(self) -> AsyncPlaybackRatesResource:
        """Private retained-event and view-cohort queries."""
        from .resources.playback_rates import AsyncPlaybackRatesResource

        return AsyncPlaybackRatesResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncChunkifyAnalyticsWithRawResponse:
        return AsyncChunkifyAnalyticsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChunkifyAnalyticsWithStreamedResponse:
        return AsyncChunkifyAnalyticsWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="repeat")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        headers: dict[str, str] = {}
        if security.get("public_key", False):
            for key, value in self._public_key.items():
                headers.setdefault(key, value)
        if security.get("secret_key", False):
            for key, value in self._secret_key.items():
                headers.setdefault(key, value)
        if security.get("admin_key", False):
            for key, value in self._admin_key.items():
                headers.setdefault(key, value)
        return headers

    @property
    def _public_key(self) -> dict[str, str]:
        public_key = self.public_key
        if public_key is None:
            return {}
        return {"X-Chunkify-Ingest-Key": public_key}

    @property
    def _secret_key(self) -> dict[str, str]:
        secret_key = self.secret_key
        if secret_key is None:
            return {}
        return {"Authorization": f"Bearer {secret_key}"}

    @property
    def _admin_key(self) -> dict[str, str]:
        admin_key = self.admin_key
        if admin_key is None:
            return {}
        return {"Authorization": f"Bearer {admin_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        public_key: str | None = None,
        secret_key: str | None = None,
        admin_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            public_key=public_key or self.public_key,
            secret_key=secret_key or self.secret_key,
            admin_key=admin_key or self.admin_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class ChunkifyAnalyticsWithRawResponse:
    _client: ChunkifyAnalytics

    def __init__(self, client: ChunkifyAnalytics) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.HealthResourceWithRawResponse:
        """Health and private ingestion status."""
        from .resources.health import HealthResourceWithRawResponse

        return HealthResourceWithRawResponse(self._client.health)

    @cached_property
    def events(self) -> events.EventsResourceWithRawResponse:
        from .resources.events import EventsResourceWithRawResponse

        return EventsResourceWithRawResponse(self._client.events)

    @cached_property
    def summary(self) -> summary.SummaryResourceWithRawResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.summary import SummaryResourceWithRawResponse

        return SummaryResourceWithRawResponse(self._client.summary)

    @cached_property
    def videos(self) -> videos.VideosResourceWithRawResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.videos import VideosResourceWithRawResponse

        return VideosResourceWithRawResponse(self._client.videos)

    @cached_property
    def timeseries(self) -> timeseries.TimeseriesResourceWithRawResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.timeseries import TimeseriesResourceWithRawResponse

        return TimeseriesResourceWithRawResponse(self._client.timeseries)

    @cached_property
    def quality(self) -> quality.QualityResourceWithRawResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.quality import QualityResourceWithRawResponse

        return QualityResourceWithRawResponse(self._client.quality)

    @cached_property
    def engagement(self) -> engagement.EngagementResourceWithRawResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.engagement import EngagementResourceWithRawResponse

        return EngagementResourceWithRawResponse(self._client.engagement)

    @cached_property
    def project(self) -> project.ProjectResourceWithRawResponse:
        """Project origins and keys."""
        from .resources.project import ProjectResourceWithRawResponse

        return ProjectResourceWithRawResponse(self._client.project)

    @cached_property
    def admin(self) -> admin.AdminResourceWithRawResponse:
        """Project origins and keys."""
        from .resources.admin import AdminResourceWithRawResponse

        return AdminResourceWithRawResponse(self._client.admin)

    @cached_property
    def views(self) -> views.ViewsResourceWithRawResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.views import ViewsResourceWithRawResponse

        return ViewsResourceWithRawResponse(self._client.views)

    @cached_property
    def errors(self) -> errors.ErrorsResourceWithRawResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.errors import ErrorsResourceWithRawResponse

        return ErrorsResourceWithRawResponse(self._client.errors)

    @cached_property
    def dimensions(self) -> dimensions.DimensionsResourceWithRawResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.dimensions import DimensionsResourceWithRawResponse

        return DimensionsResourceWithRawResponse(self._client.dimensions)

    @cached_property
    def exports(self) -> exports.ExportsResourceWithRawResponse:
        from .resources.exports import ExportsResourceWithRawResponse

        return ExportsResourceWithRawResponse(self._client.exports)

    @cached_property
    def retention(self) -> retention.RetentionResourceWithRawResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.retention import RetentionResourceWithRawResponse

        return RetentionResourceWithRawResponse(self._client.retention)

    @cached_property
    def renditions(self) -> renditions.RenditionsResourceWithRawResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.renditions import RenditionsResourceWithRawResponse

        return RenditionsResourceWithRawResponse(self._client.renditions)

    @cached_property
    def subtitles(self) -> subtitles.SubtitlesResourceWithRawResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.subtitles import SubtitlesResourceWithRawResponse

        return SubtitlesResourceWithRawResponse(self._client.subtitles)

    @cached_property
    def playback_rates(self) -> playback_rates.PlaybackRatesResourceWithRawResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.playback_rates import PlaybackRatesResourceWithRawResponse

        return PlaybackRatesResourceWithRawResponse(self._client.playback_rates)


class AsyncChunkifyAnalyticsWithRawResponse:
    _client: AsyncChunkifyAnalytics

    def __init__(self, client: AsyncChunkifyAnalytics) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.AsyncHealthResourceWithRawResponse:
        """Health and private ingestion status."""
        from .resources.health import AsyncHealthResourceWithRawResponse

        return AsyncHealthResourceWithRawResponse(self._client.health)

    @cached_property
    def events(self) -> events.AsyncEventsResourceWithRawResponse:
        from .resources.events import AsyncEventsResourceWithRawResponse

        return AsyncEventsResourceWithRawResponse(self._client.events)

    @cached_property
    def summary(self) -> summary.AsyncSummaryResourceWithRawResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.summary import AsyncSummaryResourceWithRawResponse

        return AsyncSummaryResourceWithRawResponse(self._client.summary)

    @cached_property
    def videos(self) -> videos.AsyncVideosResourceWithRawResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.videos import AsyncVideosResourceWithRawResponse

        return AsyncVideosResourceWithRawResponse(self._client.videos)

    @cached_property
    def timeseries(self) -> timeseries.AsyncTimeseriesResourceWithRawResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.timeseries import AsyncTimeseriesResourceWithRawResponse

        return AsyncTimeseriesResourceWithRawResponse(self._client.timeseries)

    @cached_property
    def quality(self) -> quality.AsyncQualityResourceWithRawResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.quality import AsyncQualityResourceWithRawResponse

        return AsyncQualityResourceWithRawResponse(self._client.quality)

    @cached_property
    def engagement(self) -> engagement.AsyncEngagementResourceWithRawResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.engagement import AsyncEngagementResourceWithRawResponse

        return AsyncEngagementResourceWithRawResponse(self._client.engagement)

    @cached_property
    def project(self) -> project.AsyncProjectResourceWithRawResponse:
        """Project origins and keys."""
        from .resources.project import AsyncProjectResourceWithRawResponse

        return AsyncProjectResourceWithRawResponse(self._client.project)

    @cached_property
    def admin(self) -> admin.AsyncAdminResourceWithRawResponse:
        """Project origins and keys."""
        from .resources.admin import AsyncAdminResourceWithRawResponse

        return AsyncAdminResourceWithRawResponse(self._client.admin)

    @cached_property
    def views(self) -> views.AsyncViewsResourceWithRawResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.views import AsyncViewsResourceWithRawResponse

        return AsyncViewsResourceWithRawResponse(self._client.views)

    @cached_property
    def errors(self) -> errors.AsyncErrorsResourceWithRawResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.errors import AsyncErrorsResourceWithRawResponse

        return AsyncErrorsResourceWithRawResponse(self._client.errors)

    @cached_property
    def dimensions(self) -> dimensions.AsyncDimensionsResourceWithRawResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.dimensions import AsyncDimensionsResourceWithRawResponse

        return AsyncDimensionsResourceWithRawResponse(self._client.dimensions)

    @cached_property
    def exports(self) -> exports.AsyncExportsResourceWithRawResponse:
        from .resources.exports import AsyncExportsResourceWithRawResponse

        return AsyncExportsResourceWithRawResponse(self._client.exports)

    @cached_property
    def retention(self) -> retention.AsyncRetentionResourceWithRawResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.retention import AsyncRetentionResourceWithRawResponse

        return AsyncRetentionResourceWithRawResponse(self._client.retention)

    @cached_property
    def renditions(self) -> renditions.AsyncRenditionsResourceWithRawResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.renditions import AsyncRenditionsResourceWithRawResponse

        return AsyncRenditionsResourceWithRawResponse(self._client.renditions)

    @cached_property
    def subtitles(self) -> subtitles.AsyncSubtitlesResourceWithRawResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.subtitles import AsyncSubtitlesResourceWithRawResponse

        return AsyncSubtitlesResourceWithRawResponse(self._client.subtitles)

    @cached_property
    def playback_rates(self) -> playback_rates.AsyncPlaybackRatesResourceWithRawResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.playback_rates import AsyncPlaybackRatesResourceWithRawResponse

        return AsyncPlaybackRatesResourceWithRawResponse(self._client.playback_rates)


class ChunkifyAnalyticsWithStreamedResponse:
    _client: ChunkifyAnalytics

    def __init__(self, client: ChunkifyAnalytics) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.HealthResourceWithStreamingResponse:
        """Health and private ingestion status."""
        from .resources.health import HealthResourceWithStreamingResponse

        return HealthResourceWithStreamingResponse(self._client.health)

    @cached_property
    def events(self) -> events.EventsResourceWithStreamingResponse:
        from .resources.events import EventsResourceWithStreamingResponse

        return EventsResourceWithStreamingResponse(self._client.events)

    @cached_property
    def summary(self) -> summary.SummaryResourceWithStreamingResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.summary import SummaryResourceWithStreamingResponse

        return SummaryResourceWithStreamingResponse(self._client.summary)

    @cached_property
    def videos(self) -> videos.VideosResourceWithStreamingResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.videos import VideosResourceWithStreamingResponse

        return VideosResourceWithStreamingResponse(self._client.videos)

    @cached_property
    def timeseries(self) -> timeseries.TimeseriesResourceWithStreamingResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.timeseries import TimeseriesResourceWithStreamingResponse

        return TimeseriesResourceWithStreamingResponse(self._client.timeseries)

    @cached_property
    def quality(self) -> quality.QualityResourceWithStreamingResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.quality import QualityResourceWithStreamingResponse

        return QualityResourceWithStreamingResponse(self._client.quality)

    @cached_property
    def engagement(self) -> engagement.EngagementResourceWithStreamingResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.engagement import EngagementResourceWithStreamingResponse

        return EngagementResourceWithStreamingResponse(self._client.engagement)

    @cached_property
    def project(self) -> project.ProjectResourceWithStreamingResponse:
        """Project origins and keys."""
        from .resources.project import ProjectResourceWithStreamingResponse

        return ProjectResourceWithStreamingResponse(self._client.project)

    @cached_property
    def admin(self) -> admin.AdminResourceWithStreamingResponse:
        """Project origins and keys."""
        from .resources.admin import AdminResourceWithStreamingResponse

        return AdminResourceWithStreamingResponse(self._client.admin)

    @cached_property
    def views(self) -> views.ViewsResourceWithStreamingResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.views import ViewsResourceWithStreamingResponse

        return ViewsResourceWithStreamingResponse(self._client.views)

    @cached_property
    def errors(self) -> errors.ErrorsResourceWithStreamingResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.errors import ErrorsResourceWithStreamingResponse

        return ErrorsResourceWithStreamingResponse(self._client.errors)

    @cached_property
    def dimensions(self) -> dimensions.DimensionsResourceWithStreamingResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.dimensions import DimensionsResourceWithStreamingResponse

        return DimensionsResourceWithStreamingResponse(self._client.dimensions)

    @cached_property
    def exports(self) -> exports.ExportsResourceWithStreamingResponse:
        from .resources.exports import ExportsResourceWithStreamingResponse

        return ExportsResourceWithStreamingResponse(self._client.exports)

    @cached_property
    def retention(self) -> retention.RetentionResourceWithStreamingResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.retention import RetentionResourceWithStreamingResponse

        return RetentionResourceWithStreamingResponse(self._client.retention)

    @cached_property
    def renditions(self) -> renditions.RenditionsResourceWithStreamingResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.renditions import RenditionsResourceWithStreamingResponse

        return RenditionsResourceWithStreamingResponse(self._client.renditions)

    @cached_property
    def subtitles(self) -> subtitles.SubtitlesResourceWithStreamingResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.subtitles import SubtitlesResourceWithStreamingResponse

        return SubtitlesResourceWithStreamingResponse(self._client.subtitles)

    @cached_property
    def playback_rates(self) -> playback_rates.PlaybackRatesResourceWithStreamingResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.playback_rates import PlaybackRatesResourceWithStreamingResponse

        return PlaybackRatesResourceWithStreamingResponse(self._client.playback_rates)


class AsyncChunkifyAnalyticsWithStreamedResponse:
    _client: AsyncChunkifyAnalytics

    def __init__(self, client: AsyncChunkifyAnalytics) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.AsyncHealthResourceWithStreamingResponse:
        """Health and private ingestion status."""
        from .resources.health import AsyncHealthResourceWithStreamingResponse

        return AsyncHealthResourceWithStreamingResponse(self._client.health)

    @cached_property
    def events(self) -> events.AsyncEventsResourceWithStreamingResponse:
        from .resources.events import AsyncEventsResourceWithStreamingResponse

        return AsyncEventsResourceWithStreamingResponse(self._client.events)

    @cached_property
    def summary(self) -> summary.AsyncSummaryResourceWithStreamingResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.summary import AsyncSummaryResourceWithStreamingResponse

        return AsyncSummaryResourceWithStreamingResponse(self._client.summary)

    @cached_property
    def videos(self) -> videos.AsyncVideosResourceWithStreamingResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.videos import AsyncVideosResourceWithStreamingResponse

        return AsyncVideosResourceWithStreamingResponse(self._client.videos)

    @cached_property
    def timeseries(self) -> timeseries.AsyncTimeseriesResourceWithStreamingResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.timeseries import AsyncTimeseriesResourceWithStreamingResponse

        return AsyncTimeseriesResourceWithStreamingResponse(self._client.timeseries)

    @cached_property
    def quality(self) -> quality.AsyncQualityResourceWithStreamingResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.quality import AsyncQualityResourceWithStreamingResponse

        return AsyncQualityResourceWithStreamingResponse(self._client.quality)

    @cached_property
    def engagement(self) -> engagement.AsyncEngagementResourceWithStreamingResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.engagement import AsyncEngagementResourceWithStreamingResponse

        return AsyncEngagementResourceWithStreamingResponse(self._client.engagement)

    @cached_property
    def project(self) -> project.AsyncProjectResourceWithStreamingResponse:
        """Project origins and keys."""
        from .resources.project import AsyncProjectResourceWithStreamingResponse

        return AsyncProjectResourceWithStreamingResponse(self._client.project)

    @cached_property
    def admin(self) -> admin.AsyncAdminResourceWithStreamingResponse:
        """Project origins and keys."""
        from .resources.admin import AsyncAdminResourceWithStreamingResponse

        return AsyncAdminResourceWithStreamingResponse(self._client.admin)

    @cached_property
    def views(self) -> views.AsyncViewsResourceWithStreamingResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.views import AsyncViewsResourceWithStreamingResponse

        return AsyncViewsResourceWithStreamingResponse(self._client.views)

    @cached_property
    def errors(self) -> errors.AsyncErrorsResourceWithStreamingResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.errors import AsyncErrorsResourceWithStreamingResponse

        return AsyncErrorsResourceWithStreamingResponse(self._client.errors)

    @cached_property
    def dimensions(self) -> dimensions.AsyncDimensionsResourceWithStreamingResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.dimensions import AsyncDimensionsResourceWithStreamingResponse

        return AsyncDimensionsResourceWithStreamingResponse(self._client.dimensions)

    @cached_property
    def exports(self) -> exports.AsyncExportsResourceWithStreamingResponse:
        from .resources.exports import AsyncExportsResourceWithStreamingResponse

        return AsyncExportsResourceWithStreamingResponse(self._client.exports)

    @cached_property
    def retention(self) -> retention.AsyncRetentionResourceWithStreamingResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.retention import AsyncRetentionResourceWithStreamingResponse

        return AsyncRetentionResourceWithStreamingResponse(self._client.retention)

    @cached_property
    def renditions(self) -> renditions.AsyncRenditionsResourceWithStreamingResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.renditions import AsyncRenditionsResourceWithStreamingResponse

        return AsyncRenditionsResourceWithStreamingResponse(self._client.renditions)

    @cached_property
    def subtitles(self) -> subtitles.AsyncSubtitlesResourceWithStreamingResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.subtitles import AsyncSubtitlesResourceWithStreamingResponse

        return AsyncSubtitlesResourceWithStreamingResponse(self._client.subtitles)

    @cached_property
    def playback_rates(self) -> playback_rates.AsyncPlaybackRatesResourceWithStreamingResponse:
        """Private retained-event and view-cohort queries."""
        from .resources.playback_rates import AsyncPlaybackRatesResourceWithStreamingResponse

        return AsyncPlaybackRatesResourceWithStreamingResponse(self._client.playback_rates)


Client = ChunkifyAnalytics

AsyncClient = AsyncChunkifyAnalytics
