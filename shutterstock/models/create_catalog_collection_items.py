from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .create_catalog_collection_item import CreateCatalogCollectionItem, CreateCatalogCollectionItemDict


class CreateCatalogCollectionItems(SdkBaseModel):
    items: list[CreateCatalogCollectionItem]


class CreateCatalogCollectionItemsDict(TypedDict):
    items: list[CreateCatalogCollectionItem | CreateCatalogCollectionItemDict]
