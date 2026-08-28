from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Download6(SdkBaseModel):
    """Information that is needed to download the sound effects"""

    url: str
    """URL that can be used to download the unwatermarked, licensed asset"""


class Download6Dict(TypedDict):
    url: str
