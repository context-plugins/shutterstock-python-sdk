from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .collection_item import CollectionItem, CollectionItemDict


class CollectionItemRequest(SdkBaseModel):
    """Request to get a list of items in a collection"""

    items: list[CollectionItem]
    """List of items"""


class CollectionItemRequestDict(TypedDict):
    items: list[CollectionItem | CollectionItemDict]
