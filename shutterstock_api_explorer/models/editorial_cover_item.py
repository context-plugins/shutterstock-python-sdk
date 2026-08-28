from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class EditorialCoverItem(SdkBaseModel):
    """Cover image for editorial livefeed"""

    height: Optional[int] = UNSET
    id: str
    url: str
    width: Optional[int] = UNSET


class EditorialCoverItemDict(TypedDict):
    height: NotRequired[int]
    id: str
    url: str
    width: NotRequired[int]
