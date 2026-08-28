from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .catalog_collection_role import CatalogCollectionRole, CatalogCollectionRoleDict


class Roles(SdkBaseModel):
    owners: Optional[list[CatalogCollectionRole]] = UNSET
    editors: Optional[list[CatalogCollectionRole]] = UNSET
    viewers: Optional[list[CatalogCollectionRole]] = UNSET


class RolesDict(TypedDict):
    owners: NotRequired[list[CatalogCollectionRole | CatalogCollectionRoleDict]]
    editors: NotRequired[list[CatalogCollectionRole | CatalogCollectionRoleDict]]
    viewers: NotRequired[list[CatalogCollectionRole | CatalogCollectionRoleDict]]
