from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .editorial_content import EditorialContent, EditorialContentDict


class EditorialImageResults(SdkBaseModel):
    """List of editorial images"""

    data: Optional[list[EditorialContent]] = UNSET
    search_id: Optional[str] = UNSET
    total_count: Optional[int] = UNSET


class EditorialImageResultsDict(TypedDict):
    data: NotRequired[list[EditorialContent | EditorialContentDict]]
    search_id: NotRequired[str]
    total_count: NotRequired[int]
