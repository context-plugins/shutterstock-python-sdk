from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Asset4(SdkBaseModel):
    id: Optional[str] = UNSET
    type_: str = Field(alias="type")


class Asset4Dict(TypedDict):
    id: NotRequired[str]
    type_: str
