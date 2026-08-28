from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AudioUrl(SdkBaseModel):
    """Audio License URL object"""

    url: str
    """URL that can be used to download the unwatermarked, licensed asset"""

    shorts_loops_stems: Optional[str] = UNSET
    """URL that can be used to download the .zip file containing shorts, loops, and stems"""


class AudioUrlDict(TypedDict):
    url: str
    shorts_loops_stems: NotRequired[str]
