from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sfx import Sfx, SfxDict


class SfxdataList(SdkBaseModel):
    """List of sound effects"""

    data: Optional[list[Sfx]] = UNSET
    """Sound Effects"""


class SfxdataListDict(TypedDict):
    data: NotRequired[list[Sfx | SfxDict]]
