from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .collection_item import CollectionItem, CollectionItemDict


class Collection(SdkBaseModel):
    """Metadata about a collection of assets"""

    cover_item: Optional[CollectionItem] = UNSET
    """Metadata about an item that is part of a collection"""

    created_time: Optional[RFC3339DateTime] = UNSET
    """When the collection was created"""

    id: str
    """The collection ID"""

    items_updated_time: Optional[RFC3339DateTime] = UNSET
    """The last time this collection's items were updated"""

    name: str
    """The name of the collection"""

    share_code: Optional[str] = UNSET
    """A code that can be used to share the collection (optional)"""

    share_url: Optional[str] = UNSET
    """The browser URL that can be used to share the collection (optional)"""

    total_item_count: int
    """The number of items in the collection"""

    updated_time: Optional[RFC3339DateTime] = UNSET
    """The last time the collection was update (other than changes to the items in it)"""


class CollectionDict(TypedDict):
    cover_item: NotRequired[CollectionItem | CollectionItemDict]
    created_time: NotRequired[RFC3339DateTime]
    id: str
    items_updated_time: NotRequired[RFC3339DateTime]
    name: str
    share_code: NotRequired[str]
    share_url: NotRequired[str]
    total_item_count: int
    updated_time: NotRequired[RFC3339DateTime]
