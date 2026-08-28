from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SearchEntitiesRequest(SdkBaseModel):
    """Search entity request data"""

    text: str
    """Plain text to extract keywords from"""


class SearchEntitiesRequestDict(TypedDict):
    text: str
