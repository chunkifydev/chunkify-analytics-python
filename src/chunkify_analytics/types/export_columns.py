# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["ExportColumns"]


class ExportColumns(BaseModel):
    columns: List[str]
    """Available CSV column names in default output order."""
