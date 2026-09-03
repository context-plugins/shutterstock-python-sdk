from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.visibility import VisibilityOrStr
from .remove_catalog_collection_item import RemoveCatalogCollectionItem, RemoveCatalogCollectionItemDict


class UpdateCatalogCollection(SdkBaseModel):
    name: Optional[str] = UNSET
    visibility: Optional[VisibilityOrStr] = UNSET
    cover_asset: Optional[RemoveCatalogCollectionItem] = UNSET


class UpdateCatalogCollectionDict(TypedDict):
    name: NotRequired[str]
    visibility: NotRequired[VisibilityOrStr]
    cover_asset: NotRequired[RemoveCatalogCollectionItem | RemoveCatalogCollectionItemDict]
