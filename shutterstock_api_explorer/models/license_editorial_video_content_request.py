from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .license_editorial_video_content import LicenseEditorialVideoContent, LicenseEditorialVideoContentDict
from .unions.country2 import Country2, Country2Dict


class LicenseEditorialVideoContentRequest(SdkBaseModel):
    """License editorial video content request"""

    country: Country2
    """Mandatory country code for where the editorial content will be distributed; this value is used for rights
    checks"""

    editorial: list[LicenseEditorialVideoContent]
    """Editorial content to license"""


class LicenseEditorialVideoContentRequestDict(TypedDict):
    country: Country2 | Country2Dict
    editorial: list[LicenseEditorialVideoContent | LicenseEditorialVideoContentDict]
