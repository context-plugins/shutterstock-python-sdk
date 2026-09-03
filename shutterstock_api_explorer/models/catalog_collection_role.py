from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class CatalogCollectionRole(SdkBaseModel):
    """A user that has access to a catalog collection"""

    id: str
    type_: Literal["USER"] = Field(default="USER", alias="type")
    email: str


class CatalogCollectionRoleDict(TypedDict):
    id: str
    type_: NotRequired[Literal["USER"]]
    email: str
