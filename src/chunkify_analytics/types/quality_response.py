# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .quality import Quality
from .quality_breakdown_page import QualityBreakdownPage

__all__ = ["QualityResponse"]

QualityResponse: TypeAlias = Union[Quality, QualityBreakdownPage]
