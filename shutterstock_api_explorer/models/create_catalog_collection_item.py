from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .asset4 import Asset4, Asset4Dict


class CreateCatalogCollectionItem(SdkBaseModel):
    asset: Asset4


class CreateCatalogCollectionItemDict(TypedDict):
    asset: Asset4 | Asset4Dict
