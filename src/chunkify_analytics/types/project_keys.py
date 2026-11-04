# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .project_key import ProjectKey

__all__ = ["ProjectKeys"]


class ProjectKeys(BaseModel):
    keys: List[ProjectKey]

    project_id: str
