from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Thumbnail(SdkBaseModel):
    """Image thumbnail information"""

    height: int
    """Height in pixels of the image thumbnail"""

    url: str
    """Direct URL to the image"""

    width: int
    """Width in pixels of the image thumbnail"""


class ThumbnailDict(TypedDict):
    height: int
    url: str
    width: int
