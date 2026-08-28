from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .catalog_collection import CatalogCollection, CatalogCollectionDict


class CatalogCollectionDataList(SdkBaseModel):
    """List of catalog collections"""

    page: float
    per_page: float
    total_count: float
    data: list[CatalogCollection]
    """List of catalog collections"""


class CatalogCollectionDataListDict(TypedDict):
    page: float
    per_page: float
    total_count: float
    data: list[CatalogCollection | CatalogCollectionDict]
