# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .native_created import NativeCreated
from .native_duplicate import NativeDuplicate

__all__ = ["EventIngestResponse"]

EventIngestResponse: TypeAlias = Union[NativeCreated, NativeDuplicate]
