from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .catalog_collection_item import CatalogCollectionItem, CatalogCollectionItemDict
from .catalog_collection_role_assignments import CatalogCollectionRoleAssignments, CatalogCollectionRoleAssignmentsDict
from .enums.visibility import VisibilityOrStr


class CatalogCollection(SdkBaseModel):
    """Catalog collection"""

    id: str
    name: str
    cover_asset: Optional[CatalogCollectionItem] = UNSET
    """Metadata about an item that is part of a collection"""

    total_item_count: float
    created_time: RFC3339DateTime
    updated_time: RFC3339DateTime
    visibility: VisibilityOrStr
    role_assignments: CatalogCollectionRoleAssignments
    """List of role assignments for a catalog collection"""


class CatalogCollectionDict(TypedDict):
    id: str
    name: str
    cover_asset: NotRequired[CatalogCollectionItem | CatalogCollectionItemDict]
    total_item_count: float
    created_time: RFC3339DateTime
    updated_time: RFC3339DateTime
    visibility: VisibilityOrStr
    role_assignments: CatalogCollectionRoleAssignments | CatalogCollectionRoleAssignmentsDict
