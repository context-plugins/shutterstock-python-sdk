from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sfx import Sfx, SfxDict


class SfxsearchResults(SdkBaseModel):
    """Sound effects search results"""

    data: list[Sfx]
    """List of tracks"""

    message: Optional[str] = UNSET
    """Server-generated message, if any"""

    page: Optional[int] = UNSET
    """Current page that is returned"""

    per_page: Optional[int] = UNSET
    """Number of results per page"""

    total_count: int
    """Total count of all results across all pages"""

    search_id: str
    """ID of the search"""


class SfxsearchResultsDict(TypedDict):
    data: list[Sfx | SfxDict]
    message: NotRequired[str]
    page: NotRequired[int]
    per_page: NotRequired[int]
    total_count: int
    search_id: str
