from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .license_video import LicenseVideo, LicenseVideoDict


class LicenseVideoRequest(SdkBaseModel):
    """List of videos to license"""

    videos: list[LicenseVideo]
    """Videos to license"""


class LicenseVideoRequestDict(TypedDict):
    videos: list[LicenseVideo | LicenseVideoDict]
