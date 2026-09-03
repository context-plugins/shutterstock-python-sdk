from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ImageCreateRequest(SdkBaseModel):
    """Request to upload an image"""

    base64_image: str
    """A Base 64 encoded jpeg or png; images can be no larger than 10mb and can be no larger than 10,000 pixels in width
    or height"""


class ImageCreateRequestDict(TypedDict):
    base64_image: str
