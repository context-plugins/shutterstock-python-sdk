from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .image import Image, ImageDict


class ImageSearchResults(SdkBaseModel):
    """Image search results"""

    data: list[Image]
    """List of images"""

    message: Optional[str] = UNSET
    """Server-generated message, if any"""

    page: Optional[int] = UNSET
    """Current page that is returned"""

    per_page: Optional[int] = UNSET
    """Number of results per page"""

    search_id: str
    """Unique identifier for the search request"""

    spellcheck_info: Optional[Any] = UNSET
    """Returns information if search phrase has potentially been mistyped or another query would lead to better search
    results"""

    total_count: int
    """Total count of all results across all pages"""


class ImageSearchResultsDict(TypedDict):
    data: list[Image | ImageDict]
    message: NotRequired[str]
    page: NotRequired[int]
    per_page: NotRequired[int]
    search_id: str
    spellcheck_info: NotRequired[Any]
    total_count: int
