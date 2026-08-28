from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type1 import Type1OrStr


class CatalogCollectionRole(SdkBaseModel):
    """A user that has access to a catalog collection"""

    id: str
    type_: Type1OrStr = Field(alias="type")
    email: str


class CatalogCollectionRoleDict(TypedDict):
    id: str
    type_: Type1OrStr
    email: str
