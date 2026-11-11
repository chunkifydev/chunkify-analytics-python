# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import shared, event_page, view_detail, stored_event
from .. import _compat
from .view import View as View
from .export import Export as Export
from .health import Health as Health
from .shared import (
    Error as Error,
    OtlpScope as OtlpScope,
    PlayedRange as PlayedRange,
    ViewMetrics as ViewMetrics,
    EventContext as EventContext,
    OtlpAnyValue as OtlpAnyValue,
    OtlpResource as OtlpResource,
    EventEnvelope as EventEnvelope,
    OtlpAttribute as OtlpAttribute,
    OtlpLogRecord as OtlpLogRecord,
    PlaybackScore as PlaybackScore,
    BrowserContext as BrowserContext,
    ProgressReached as ProgressReached,
    StartupOutcomes as StartupOutcomes,
    CustomDimensions as CustomDimensions,
    MetricCountRatio as MetricCountRatio,
    StoredOtlpContext as StoredOtlpContext,
    OtlpAttributeValue as OtlpAttributeValue,
    SubtitlePlayingTime as SubtitlePlayingTime,
    OtlpContextAttribute as OtlpContextAttribute,
    RenditionPlayingTime as RenditionPlayingTime,
    WatchTimeDistribution as WatchTimeDistribution,
    PlaybackRatePlayingTime as PlaybackRatePlayingTime,
)
from .metrics import Metrics as Metrics
from .project import Project as Project
from .quality import Quality as Quality
from .view_page import ViewPage as ViewPage
from .engagement import Engagement as Engagement
from .error_page import ErrorPage as ErrorPage
from .event_page import EventPage as EventPage
from .timeseries import Timeseries as Timeseries
from .video_page import VideoPage as VideoPage
from .view_ended import ViewEnded as ViewEnded
from .error_group import ErrorGroup as ErrorGroup
from .project_key import ProjectKey as ProjectKey
from .time_bucket import TimeBucket as TimeBucket
from .view_detail import ViewDetail as ViewDetail
from .project_keys import ProjectKeys as ProjectKeys
from .stored_event import StoredEvent as StoredEvent
from .view_started import ViewStarted as ViewStarted
from .video_metrics import VideoMetrics as VideoMetrics
from .view_snapshot import ViewSnapshot as ViewSnapshot
from .export_columns import ExportColumns as ExportColumns
from .native_created import NativeCreated as NativeCreated
from .playback_error import PlaybackError as PlaybackError
from .seek_completed import SeekCompleted as SeekCompleted
from .analytics_event import AnalyticsEvent as AnalyticsEvent
from .created_project import CreatedProject as CreatedProject
from .deleted_project import DeletedProject as DeletedProject
from .subtitle_metric import SubtitleMetric as SubtitleMetric
from .subtitle_report import SubtitleReport as SubtitleReport
from .dimension_values import DimensionValues as DimensionValues
from .metrics_response import MetricsResponse as MetricsResponse
from .native_duplicate import NativeDuplicate as NativeDuplicate
from .quality_response import QualityResponse as QualityResponse
from .rendition_metric import RenditionMetric as RenditionMetric
from .rendition_report import RenditionReport as RenditionReport
from .retention_bucket import RetentionBucket as RetentionBucket
from .retention_report import RetentionReport as RetentionReport
from .subtitle_changed import SubtitleChanged as SubtitleChanged
from .view_ended_param import ViewEndedParam as ViewEndedParam
from .view_list_params import ViewListParams as ViewListParams
from .error_list_params import ErrorListParams as ErrorListParams
from .event_list_params import EventListParams as EventListParams
from .rendition_changed import RenditionChanged as RenditionChanged
from .video_list_params import VideoListParams as VideoListParams
from .export_query_param import ExportQueryParam as ExportQueryParam
from .quality_timeseries import QualityTimeseries as QualityTimeseries
from .view_started_param import ViewStartedParam as ViewStartedParam
from .created_project_key import CreatedProjectKey as CreatedProjectKey
from .engagement_response import EngagementResponse as EngagementResponse
from .event_ingest_params import EventIngestParams as EventIngestParams
from .rotated_project_key import RotatedProjectKey as RotatedProjectKey
from .timeseries_response import TimeseriesResponse as TimeseriesResponse
from .view_snapshot_param import ViewSnapshotParam as ViewSnapshotParam
from .export_create_params import ExportCreateParams as ExportCreateParams
from .playback_error_param import PlaybackErrorParam as PlaybackErrorParam
from .playback_rate_metric import PlaybackRateMetric as PlaybackRateMetric
from .playback_rate_report import PlaybackRateReport as PlaybackRateReport
from .seek_completed_param import SeekCompletedParam as SeekCompletedParam
from .view_retrieve_params import ViewRetrieveParams as ViewRetrieveParams
from .analytics_event_param import AnalyticsEventParam as AnalyticsEventParam
from .engagement_timeseries import EngagementTimeseries as EngagementTimeseries
from .event_ingest_response import EventIngestResponse as EventIngestResponse
from .playback_rate_changed import PlaybackRateChanged as PlaybackRateChanged
from .project_update_params import ProjectUpdateParams as ProjectUpdateParams
from .metrics_breakdown_page import MetricsBreakdownPage as MetricsBreakdownPage
from .playback_state_changed import PlaybackStateChanged as PlaybackStateChanged
from .quality_breakdown_page import QualityBreakdownPage as QualityBreakdownPage
from .subtitle_changed_param import SubtitleChangedParam as SubtitleChangedParam
from .quality_retrieve_params import QualityRetrieveParams as QualityRetrieveParams
from .rendition_changed_param import RenditionChangedParam as RenditionChangedParam
from .summary_retrieve_params import SummaryRetrieveParams as SummaryRetrieveParams
from .export_download_response import ExportDownloadResponse as ExportDownloadResponse
from .subtitle_retrieve_params import SubtitleRetrieveParams as SubtitleRetrieveParams
from .timesery_retrieve_params import TimeseryRetrieveParams as TimeseryRetrieveParams
from .engagement_breakdown_page import EngagementBreakdownPage as EngagementBreakdownPage
from .quality_timeseries_bucket import QualityTimeseriesBucket as QualityTimeseriesBucket
from .rendition_retrieve_params import RenditionRetrieveParams as RenditionRetrieveParams
from .retention_retrieve_params import RetentionRetrieveParams as RetentionRetrieveParams
from .engagement_retrieve_params import EngagementRetrieveParams as EngagementRetrieveParams
from .export_list_columns_params import ExportListColumnsParams as ExportListColumnsParams
from .admin_create_project_params import AdminCreateProjectParams as AdminCreateProjectParams
from .playback_rate_changed_param import PlaybackRateChangedParam as PlaybackRateChangedParam
from .dimension_list_values_params import DimensionListValuesParams as DimensionListValuesParams
from .engagement_timeseries_bucket import EngagementTimeseriesBucket as EngagementTimeseriesBucket
from .playback_state_changed_param import PlaybackStateChangedParam as PlaybackStateChangedParam
from .playback_rate_retrieve_params import PlaybackRateRetrieveParams as PlaybackRateRetrieveParams

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V1:
    event_page.EventPage.update_forward_refs()  # type: ignore
    stored_event.StoredEvent.update_forward_refs()  # type: ignore
    view_detail.ViewDetail.update_forward_refs()  # type: ignore
    shared.otlp_any_value.OtlpAnyValue.update_forward_refs()  # type: ignore
    shared.otlp_attribute.OtlpAttribute.update_forward_refs()  # type: ignore
    shared.otlp_context_attribute.OtlpContextAttribute.update_forward_refs()  # type: ignore
    shared.otlp_log_record.OtlpLogRecord.update_forward_refs()  # type: ignore
    shared.otlp_resource.OtlpResource.update_forward_refs()  # type: ignore
    shared.otlp_scope.OtlpScope.update_forward_refs()  # type: ignore
    shared.stored_otlp_context.StoredOtlpContext.update_forward_refs()  # type: ignore
else:
    event_page.EventPage.model_rebuild(_parent_namespace_depth=0)
    stored_event.StoredEvent.model_rebuild(_parent_namespace_depth=0)
    view_detail.ViewDetail.model_rebuild(_parent_namespace_depth=0)
    shared.otlp_any_value.OtlpAnyValue.model_rebuild(_parent_namespace_depth=0)
    shared.otlp_attribute.OtlpAttribute.model_rebuild(_parent_namespace_depth=0)
    shared.otlp_context_attribute.OtlpContextAttribute.model_rebuild(_parent_namespace_depth=0)
    shared.otlp_log_record.OtlpLogRecord.model_rebuild(_parent_namespace_depth=0)
    shared.otlp_resource.OtlpResource.model_rebuild(_parent_namespace_depth=0)
    shared.otlp_scope.OtlpScope.model_rebuild(_parent_namespace_depth=0)
    shared.stored_otlp_context.StoredOtlpContext.model_rebuild(_parent_namespace_depth=0)
