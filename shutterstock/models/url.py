from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Url(SdkBaseModel):
    """URL object"""

    url: str
    """URL that can be used to download the unwatermarked, licensed asset"""


class UrlDict(TypedDict):
    url: str
