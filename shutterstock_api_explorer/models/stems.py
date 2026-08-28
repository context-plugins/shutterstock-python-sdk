from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Stems(SdkBaseModel):
    url: Optional[str] = UNSET


class StemsDict(TypedDict):
    url: NotRequired[str]
