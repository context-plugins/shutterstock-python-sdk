from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .roles import Roles, RolesDict


class CatalogCollectionRoleAssignments(SdkBaseModel):
    """List of role assignments for a catalog collection"""

    collection_id: str
    roles: Roles


class CatalogCollectionRoleAssignmentsDict(TypedDict):
    collection_id: str
    roles: Roles | RolesDict
