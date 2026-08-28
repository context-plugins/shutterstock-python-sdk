from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .catalog_collection_item import CatalogCollectionItem, CatalogCollectionItemDict


class CatalogCollectionItemDataList(SdkBaseModel):
    """List of catalog collection items"""

    page: float
    per_page: float
    total_count: float
    data: list[CatalogCollectionItem]
    """List of catalog collection items"""


class CatalogCollectionItemDataListDict(TypedDict):
    page: float
    per_page: float
    total_count: float
    data: list[CatalogCollectionItem | CatalogCollectionItemDict]
