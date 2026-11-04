# Shared Types

```python
from chunkify_analytics.types import (
    BrowserContext,
    Error,
    EventContext,
    EventEnvelope,
    MetricCountRatio,
    OtlpAnyValue,
    OtlpAttribute,
    OtlpAttributeValue,
    OtlpContextAttribute,
    OtlpLogRecord,
    OtlpResource,
    OtlpScope,
    PlaybackScore,
    PlayedRange,
    ProgressReached,
    RenditionPlayingTime,
    StartupOutcomes,
    StoredOtlpContext,
    ViewMetrics,
    WatchTimeDistribution,
)
```

# Health

Types:

```python
from chunkify_analytics.types import Health
```

Methods:

- <code title="get /healthz">client.health.<a href="./src/chunkify_analytics/resources/health.py">retrieve</a>() -> <a href="./src/chunkify_analytics/types/health.py">Health</a></code>

# Events

Types:

```python
from chunkify_analytics.types import (
    AnalyticsEvent,
    EventPage,
    NativeCreated,
    NativeDuplicate,
    PlaybackError,
    PlaybackStateChanged,
    RenditionChanged,
    SeekCompleted,
    StoredEvent,
    ViewEnded,
    ViewSnapshot,
    ViewStarted,
    EventIngestResponse,
)
```

Methods:

- <code title="get /v1/events">client.events.<a href="./src/chunkify_analytics/resources/events.py">list</a>(\*\*<a href="src/chunkify_analytics/types/event_list_params.py">params</a>) -> <a href="./src/chunkify_analytics/types/stored_event.py">SyncEventsPage[StoredEvent]</a></code>
- <code title="post /v1/events">client.events.<a href="./src/chunkify_analytics/resources/events.py">ingest</a>(\*\*<a href="src/chunkify_analytics/types/event_ingest_params.py">params</a>) -> <a href="./src/chunkify_analytics/types/event_ingest_response.py">EventIngestResponse</a></code>

# Summary

Types:

```python
from chunkify_analytics.types import Metrics, MetricsBreakdownPage, MetricsResponse
```

Methods:

- <code title="get /v1/summary">client.summary.<a href="./src/chunkify_analytics/resources/summary.py">retrieve</a>(\*\*<a href="src/chunkify_analytics/types/summary_retrieve_params.py">params</a>) -> <a href="./src/chunkify_analytics/types/metrics_response.py">MetricsResponse</a></code>

# Videos

Types:

```python
from chunkify_analytics.types import VideoMetrics, VideoPage
```

Methods:

- <code title="get /v1/videos">client.videos.<a href="./src/chunkify_analytics/resources/videos.py">list</a>(\*\*<a href="src/chunkify_analytics/types/video_list_params.py">params</a>) -> <a href="./src/chunkify_analytics/types/video_metrics.py">SyncVideosPage[VideoMetrics]</a></code>

# Timeseries

Types:

```python
from chunkify_analytics.types import (
    EngagementTimeseries,
    EngagementTimeseriesBucket,
    QualityTimeseries,
    QualityTimeseriesBucket,
    TimeBucket,
    Timeseries,
    TimeseriesResponse,
)
```

Methods:

- <code title="get /v1/timeseries">client.timeseries.<a href="./src/chunkify_analytics/resources/timeseries.py">retrieve</a>(\*\*<a href="src/chunkify_analytics/types/timesery_retrieve_params.py">params</a>) -> <a href="./src/chunkify_analytics/types/timeseries_response.py">TimeseriesResponse</a></code>

# Quality

Types:

```python
from chunkify_analytics.types import Quality, QualityBreakdownPage, QualityResponse
```

Methods:

- <code title="get /v1/quality">client.quality.<a href="./src/chunkify_analytics/resources/quality.py">retrieve</a>(\*\*<a href="src/chunkify_analytics/types/quality_retrieve_params.py">params</a>) -> <a href="./src/chunkify_analytics/types/quality_response.py">QualityResponse</a></code>

# Engagement

Types:

```python
from chunkify_analytics.types import Engagement, EngagementBreakdownPage, EngagementResponse
```

Methods:

- <code title="get /v1/engagement">client.engagement.<a href="./src/chunkify_analytics/resources/engagement.py">retrieve</a>(\*\*<a href="src/chunkify_analytics/types/engagement_retrieve_params.py">params</a>) -> <a href="./src/chunkify_analytics/types/engagement_response.py">EngagementResponse</a></code>

# Project

Types:

```python
from chunkify_analytics.types import (
    CreateProjectKeyRequest,
    CreatedProjectKey,
    DeletedProject,
    Project,
    ProjectKey,
    ProjectKeys,
    ProjectUpdate,
    RotatedProjectKey,
)
```

Methods:

- <code title="patch /v1/project">client.project.<a href="./src/chunkify_analytics/resources/project/project.py">update</a>(\*\*<a href="src/chunkify_analytics/types/project_update_params.py">params</a>) -> <a href="./src/chunkify_analytics/types/project/project.py">Project</a></code>
- <code title="delete /v1/project">client.project.<a href="./src/chunkify_analytics/resources/project/project.py">delete</a>() -> <a href="./src/chunkify_analytics/types/deleted_project.py">DeletedProject</a></code>

## Keys

Methods:

- <code title="post /v1/project/keys">client.project.keys.<a href="./src/chunkify_analytics/resources/project/keys.py">create</a>(\*\*<a href="src/chunkify_analytics/types/project/key_create_params.py">params</a>) -> <a href="./src/chunkify_analytics/types/created_project_key.py">CreatedProjectKey</a></code>
- <code title="get /v1/project/keys">client.project.keys.<a href="./src/chunkify_analytics/resources/project/keys.py">list</a>() -> <a href="./src/chunkify_analytics/types/project_keys.py">ProjectKeys</a></code>
- <code title="post /v1/project/keys/{key_id}/rotate">client.project.keys.<a href="./src/chunkify_analytics/resources/project/keys.py">rotate</a>(key_id) -> <a href="./src/chunkify_analytics/types/rotated_project_key.py">RotatedProjectKey</a></code>

# Admin

Types:

```python
from chunkify_analytics.types import CreateProjectRequest, CreatedProject
```

Methods:

- <code title="post /v1/projects">client.admin.<a href="./src/chunkify_analytics/resources/admin/admin.py">create_project</a>(\*\*<a href="src/chunkify_analytics/types/admin_create_project_params.py">params</a>) -> <a href="./src/chunkify_analytics/types/created_project.py">CreatedProject</a></code>

## Keys

Methods:

- <code title="get /v1/projects/{project_id}/keys">client.admin.keys.<a href="./src/chunkify_analytics/resources/admin/keys.py">list</a>(project_id) -> <a href="./src/chunkify_analytics/types/project_keys.py">ProjectKeys</a></code>
- <code title="post /v1/projects/{project_id}/keys/{key_id}/rotate">client.admin.keys.<a href="./src/chunkify_analytics/resources/admin/keys.py">rotate</a>(key_id, \*, project_id) -> <a href="./src/chunkify_analytics/types/rotated_project_key.py">RotatedProjectKey</a></code>

# Views

Types:

```python
from chunkify_analytics.types import View, ViewDetail, ViewPage
```

Methods:

- <code title="get /v1/views/{view_id}">client.views.<a href="./src/chunkify_analytics/resources/views.py">retrieve</a>(view_id, \*\*<a href="src/chunkify_analytics/types/view_retrieve_params.py">params</a>) -> <a href="./src/chunkify_analytics/types/view_detail.py">ViewDetail</a></code>
- <code title="get /v1/views">client.views.<a href="./src/chunkify_analytics/resources/views.py">list</a>(\*\*<a href="src/chunkify_analytics/types/view_list_params.py">params</a>) -> <a href="./src/chunkify_analytics/types/view.py">SyncViewsPage[View]</a></code>

# Errors

Types:

```python
from chunkify_analytics.types import ErrorGroup, ErrorPage
```

Methods:

- <code title="get /v1/errors">client.errors.<a href="./src/chunkify_analytics/resources/errors.py">list</a>(\*\*<a href="src/chunkify_analytics/types/error_list_params.py">params</a>) -> <a href="./src/chunkify_analytics/types/error_group.py">SyncErrorsPage[ErrorGroup]</a></code>

# Dimensions

Types:

```python
from chunkify_analytics.types import DimensionValues
```

Methods:

- <code title="get /v1/dimensions/{dimension}">client.dimensions.<a href="./src/chunkify_analytics/resources/dimensions.py">list_values</a>(dimension, \*\*<a href="src/chunkify_analytics/types/dimension_list_values_params.py">params</a>) -> SyncDimensionValuesPage[Value]</code>

# Exports

Types:

```python
from chunkify_analytics.types import (
    Export,
    ExportColumns,
    ExportQuery,
    ExportRequest,
    ExportDownloadResponse,
)
```

Methods:

- <code title="post /v1/exports">client.exports.<a href="./src/chunkify_analytics/resources/exports.py">create</a>(\*\*<a href="src/chunkify_analytics/types/export_create_params.py">params</a>) -> <a href="./src/chunkify_analytics/types/export.py">Export</a></code>
- <code title="get /v1/exports/{token}">client.exports.<a href="./src/chunkify_analytics/resources/exports.py">download</a>(token) -> str</code>
- <code title="get /v1/exports">client.exports.<a href="./src/chunkify_analytics/resources/exports.py">list_columns</a>(\*\*<a href="src/chunkify_analytics/types/export_list_columns_params.py">params</a>) -> <a href="./src/chunkify_analytics/types/export_columns.py">ExportColumns</a></code>

# Retention

Types:

```python
from chunkify_analytics.types import RetentionBucket, RetentionReport
```

Methods:

- <code title="get /v1/retention">client.retention.<a href="./src/chunkify_analytics/resources/retention.py">retrieve</a>(\*\*<a href="src/chunkify_analytics/types/retention_retrieve_params.py">params</a>) -> <a href="./src/chunkify_analytics/types/retention_report.py">RetentionReport</a></code>

# Renditions

Types:

```python
from chunkify_analytics.types import RenditionMetric, RenditionReport
```

Methods:

- <code title="get /v1/renditions">client.renditions.<a href="./src/chunkify_analytics/resources/renditions.py">retrieve</a>(\*\*<a href="src/chunkify_analytics/types/rendition_retrieve_params.py">params</a>) -> <a href="./src/chunkify_analytics/types/rendition_report.py">RenditionReport</a></code>
