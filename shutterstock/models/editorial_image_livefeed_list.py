from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .editorial_image_livefeed import EditorialImageLivefeed, EditorialImageLivefeedDict


class EditorialImageLivefeedList(SdkBaseModel):
    """List of editorial livefeeds"""

    data: list[EditorialImageLivefeed]
    """Editorial livefeeds"""

    message: Optional[str] = UNSET
    """Optional error message"""

    page: Optional[int] = UNSET
    """Current page of the response"""

    per_page: Optional[int] = UNSET
    """Number of results per page"""

    total_count: int
    """Total count of all results"""


class EditorialImageLivefeedListDict(TypedDict):
    data: list[EditorialImageLivefeed | EditorialImageLivefeedDict]
    message: NotRequired[str]
    page: NotRequired[int]
    per_page: NotRequired[int]
    total_count: int
