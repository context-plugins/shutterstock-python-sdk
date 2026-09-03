from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .unions.image3 import Image3, Image3Dict


class LicenseImageRequest(SdkBaseModel):
    """Image license request data"""

    images: list[Image3]
    """Images to create licenses for"""


class LicenseImageRequestDict(TypedDict):
    images: list[Image3 | Image3Dict]
