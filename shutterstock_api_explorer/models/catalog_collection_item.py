from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .asset import Asset, AssetDict


class CatalogCollectionItem(SdkBaseModel):
    """Metadata about an item that is part of a collection"""

    id: str
    asset: Asset
    created_time: RFC3339DateTime
    collection_ids: Optional[list[str]] = UNSET
    """The collection IDs that this asset belongs to"""


class CatalogCollectionItemDict(TypedDict):
    id: str
    asset: Asset | AssetDict
    created_time: RFC3339DateTime
    collection_ids: NotRequired[list[str]]
