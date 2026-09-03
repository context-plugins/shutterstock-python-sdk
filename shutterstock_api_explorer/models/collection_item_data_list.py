from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .collection_item import CollectionItem, CollectionItemDict
from .error import Error, ErrorDict


class CollectionItemDataList(SdkBaseModel):
    """List of items in a collection"""

    data: Optional[list[CollectionItem]] = UNSET
    """Assets in the collection"""

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


class CollectionItemDataListDict(TypedDict):
    data: NotRequired[list[CollectionItem | CollectionItemDict]]
    errors: NotRequired[list[Error | ErrorDict]]
    message: NotRequired[str]
    page: NotRequired[int]
    per_page: NotRequired[int]
    total_count: NotRequired[int]
