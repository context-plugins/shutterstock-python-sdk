from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .collection import Collection, CollectionDict
from .error import Error, ErrorDict


class CollectionDataList(SdkBaseModel):
    """List of collections"""

    data: Optional[list[Collection]] = UNSET
    """Collections"""

    errors: Optional[list[Error]] = UNSET
    """Error list; appears only if there was an error"""

    message: Optional[str] = UNSET
    """Server-generated message, if any"""

    page: Optional[int] = UNSET
    """The current page of results"""

    per_page: Optional[int] = UNSET
    """The number of results per page"""

    total_count: Optional[int] = UNSET
    """The total number of results across all pages"""


class CollectionDataListDict(TypedDict):
    data: NotRequired[list[Collection | CollectionDict]]
    errors: NotRequired[list[Error | ErrorDict]]
    message: NotRequired[str]
    page: NotRequired[int]
    per_page: NotRequired[int]
    total_count: NotRequired[int]
