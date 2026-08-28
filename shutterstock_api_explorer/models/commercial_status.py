from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CommercialStatus(SdkBaseModel):
    status: Optional[str] = UNSET
    reason: Optional[str] = UNSET


class CommercialStatusDict(TypedDict):
    status: NotRequired[str]
    reason: NotRequired[str]
