from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Rights(SdkBaseModel):
    countries: Optional[str] = UNSET


class RightsDict(TypedDict):
    countries: NotRequired[str]
