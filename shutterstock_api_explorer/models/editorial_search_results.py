from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .editorial_content import EditorialContent, EditorialContentDict


class EditorialSearchResults(SdkBaseModel):
    """Editorial search results"""

    data: list[EditorialContent]
    """Editorial items"""

    message: Optional[str] = UNSET
    """Optional error message"""

    next: Optional[str] = UNSET
    """Cursor value that represents the next page of results"""

    page: Optional[int] = UNSET
    """Current page of the response"""

    per_page: Optional[int] = UNSET
    """Number of results per page"""

    prev: Optional[str] = UNSET
    """Cursor value that represents the previous page of results"""

    search_id: Optional[str] = UNSET
    """Unique identifier for the search request"""

    total_count: int
    """Total count of all results"""


class EditorialSearchResultsDict(TypedDict):
    data: list[EditorialContent | EditorialContentDict]
    message: NotRequired[str]
    next: NotRequired[str]
    page: NotRequired[int]
    per_page: NotRequired[int]
    prev: NotRequired[str]
    search_id: NotRequired[str]
    total_count: int
