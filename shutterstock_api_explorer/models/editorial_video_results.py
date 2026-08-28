from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .editorial_video_content import EditorialVideoContent, EditorialVideoContentDict


class EditorialVideoResults(SdkBaseModel):
    """List of editorial videos"""

    data: Optional[list[EditorialVideoContent]] = UNSET
    search_id: Optional[str] = UNSET
    total_count: Optional[int] = UNSET


class EditorialVideoResultsDict(TypedDict):
    data: NotRequired[list[EditorialVideoContent | EditorialVideoContentDict]]
    search_id: NotRequired[str]
    total_count: NotRequired[int]
