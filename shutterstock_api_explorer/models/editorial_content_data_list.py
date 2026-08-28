from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .editorial_content import EditorialContent, EditorialContentDict
from .error import Error, ErrorDict


class EditorialContentDataList(SdkBaseModel):
    """List of editorial items"""

    data: Optional[list[EditorialContent]] = UNSET
    """Editorial items"""

    errors: Optional[list[Error]] = UNSET
    """Error list; appears only if there was an error"""

    message: Optional[str] = UNSET
    """Optional error message"""

    page: Optional[int] = UNSET
    """Current page of the response"""

    per_page: Optional[int] = UNSET
    """Number of results per page"""

    total_count: Optional[int] = UNSET
    """Total count of all results"""


class EditorialContentDataListDict(TypedDict):
    data: NotRequired[list[EditorialContent | EditorialContentDict]]
    errors: NotRequired[list[Error | ErrorDict]]
    message: NotRequired[str]
    page: NotRequired[int]
    per_page: NotRequired[int]
    total_count: NotRequired[int]
