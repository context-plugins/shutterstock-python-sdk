from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .loops import Loops, LoopsDict
from .shorts import Shorts, ShortsDict
from .stems import Stems, StemsDict


class ShortsLoopsStems(SdkBaseModel):
    """Links for Shorts, Loops and Stems previews"""

    shorts: Optional[dict[str, Shorts]] = UNSET
    loops: Optional[dict[str, Loops]] = UNSET
    stems: Optional[dict[str, Stems]] = UNSET


class ShortsLoopsStemsDict(TypedDict):
    shorts: NotRequired[dict[str, Shorts | ShortsDict]]
    loops: NotRequired[dict[str, Loops | LoopsDict]]
    stems: NotRequired[dict[str, Stems | StemsDict]]
