from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Urls(SdkBaseModel):
    """List of URLs"""

    urls: list[str]
    """URLs"""


class UrlsDict(TypedDict):
    urls: list[str]
