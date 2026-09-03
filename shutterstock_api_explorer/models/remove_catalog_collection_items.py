from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .remove_catalog_collection_item import RemoveCatalogCollectionItem, RemoveCatalogCollectionItemDict


class RemoveCatalogCollectionItems(SdkBaseModel):
    items: list[RemoveCatalogCollectionItem]


class RemoveCatalogCollectionItemsDict(TypedDict):
    items: list[RemoveCatalogCollectionItem | RemoveCatalogCollectionItemDict]
