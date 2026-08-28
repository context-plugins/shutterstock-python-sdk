from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class VideoPreviewUrl(SdkBaseModel):
    """Video preview information"""

    url: str
    """Direct URL to the image"""


class VideoPreviewUrlDict(TypedDict):
    url: str
