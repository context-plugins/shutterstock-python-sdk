from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .video import Video, VideoDict


class VideoSearchResults(SdkBaseModel):
    """Video search results"""

    data: list[Video]
    """List of videos"""

    message: Optional[str] = UNSET
    """Server-generated message, if any"""

    page: Optional[int] = UNSET
    """Current page that is returned"""

    per_page: Optional[int] = UNSET
    """Number of results per page"""

    total_count: int
    """Total count of all results across all pages"""

    search_id: str
    """Unique identifier for the search request"""


class VideoSearchResultsDict(TypedDict):
    data: list[Video | VideoDict]
    message: NotRequired[str]
    page: NotRequired[int]
    per_page: NotRequired[int]
    total_count: int
    search_id: str
