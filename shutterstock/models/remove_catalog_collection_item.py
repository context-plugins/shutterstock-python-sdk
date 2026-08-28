from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class RemoveCatalogCollectionItem(SdkBaseModel):
    id: str


class RemoveCatalogCollectionItemDict(TypedDict):
    id: str
