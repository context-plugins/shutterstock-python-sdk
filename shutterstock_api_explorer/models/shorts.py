from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Shorts(SdkBaseModel):
    url: Optional[str] = UNSET


class ShortsDict(TypedDict):
    url: NotRequired[str]
