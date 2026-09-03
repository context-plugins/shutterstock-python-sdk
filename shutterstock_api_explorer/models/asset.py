from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type import TypeOrStr


class Asset(SdkBaseModel):
    id: Optional[str] = UNSET
    type_: TypeOrStr = Field(alias="type")
    name: Optional[str] = UNSET


class AssetDict(TypedDict):
    id: NotRequired[str]
    type_: TypeOrStr
    name: NotRequired[str]
