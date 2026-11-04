# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .engagement import Engagement
from .engagement_breakdown_page import EngagementBreakdownPage

__all__ = ["EngagementResponse"]

EngagementResponse: TypeAlias = Union[Engagement, EngagementBreakdownPage]
