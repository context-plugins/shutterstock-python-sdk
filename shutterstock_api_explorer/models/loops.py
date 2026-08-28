from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Loops(SdkBaseModel):
    url: Optional[str] = UNSET


class LoopsDict(TypedDict):
    url: NotRequired[str]
