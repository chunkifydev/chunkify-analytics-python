# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "SyncEventsPage",
    "AsyncEventsPage",
    "SyncVideosPage",
    "AsyncVideosPage",
    "SyncViewsPage",
    "AsyncViewsPage",
    "SyncErrorsPage",
    "AsyncErrorsPage",
    "SyncDimensionValuesPage",
    "AsyncDimensionValuesPage",
]

_T = TypeVar("_T")


class SyncEventsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    events: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        events = self.events
        if not events:
            return []
        return events

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class AsyncEventsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    events: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        events = self.events
        if not events:
            return []
        return events

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class SyncVideosPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    videos: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        videos = self.videos
        if not videos:
            return []
        return videos

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class AsyncVideosPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    videos: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        videos = self.videos
        if not videos:
            return []
        return videos

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class SyncViewsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    views: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        views = self.views
        if not views:
            return []
        return views

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class AsyncViewsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    views: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        views = self.views
        if not views:
            return []
        return views

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class SyncErrorsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    errors: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        errors = self.errors
        if not errors:
            return []
        return errors

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class AsyncErrorsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    errors: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        errors = self.errors
        if not errors:
            return []
        return errors

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class SyncDimensionValuesPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    values: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        values = self.values
        if not values:
            return []
        return values

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class AsyncDimensionValuesPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    values: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        values = self.values
        if not values:
            return []
        return values

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})
