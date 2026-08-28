from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .editorial_updated_content import EditorialUpdatedContent, EditorialUpdatedContentDict


class EditorialUpdatedResults(SdkBaseModel):
    """Editorial updated results"""

    data: list[EditorialUpdatedContent]
    """Editorial updated items"""

    message: Optional[str] = UNSET
    """Optional error message"""

    next: Optional[str] = UNSET
    """Cursor value that represents the next page of results"""

    per_page: Optional[int] = UNSET
    """Number of results per page"""

    prev: Optional[str] = UNSET
    """Cursor value that represents the previous page of results"""


class EditorialUpdatedResultsDict(TypedDict):
    data: list[EditorialUpdatedContent | EditorialUpdatedContentDict]
    message: NotRequired[str]
    next: NotRequired[str]
    per_page: NotRequired[int]
    prev: NotRequired[str]
