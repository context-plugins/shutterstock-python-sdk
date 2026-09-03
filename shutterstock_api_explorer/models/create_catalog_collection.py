from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .create_catalog_collection_item import CreateCatalogCollectionItem, CreateCatalogCollectionItemDict
from .enums.visibility import VisibilityOrStr


class CreateCatalogCollection(SdkBaseModel):
    name: str
    visibility: Optional[VisibilityOrStr] = UNSET
    items: Optional[list[CreateCatalogCollectionItem]] = UNSET


class CreateCatalogCollectionDict(TypedDict):
    name: str
    visibility: NotRequired[VisibilityOrStr]
    items: NotRequired[list[CreateCatalogCollectionItem | CreateCatalogCollectionItemDict]]
