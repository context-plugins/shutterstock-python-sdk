from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Download2(SdkBaseModel):
    """Information that is needed to download the image"""

    url: str
    """URL that can be used to download the unwatermarked, licensed asset"""


class Download2Dict(TypedDict):
    url: str
