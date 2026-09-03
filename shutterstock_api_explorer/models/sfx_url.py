from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SfxUrl(SdkBaseModel):
    """Sound effect license URL object"""

    url: str
    """URL that can be used to download the unwatermarked, licensed asset"""


class SfxUrlDict(TypedDict):
    url: str
