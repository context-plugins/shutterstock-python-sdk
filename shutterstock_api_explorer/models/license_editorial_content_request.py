from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .license_editorial_content import LicenseEditorialContent, LicenseEditorialContentDict
from .unions.country2 import Country2, Country2Dict


class LicenseEditorialContentRequest(SdkBaseModel):
    """License editorial content request"""

    country: Country2
    """Mandatory country code for where the editorial content will be distributed; this value is used for rights
    checks"""

    editorial: list[LicenseEditorialContent]
    """Editorial content to license"""


class LicenseEditorialContentRequestDict(TypedDict):
    country: Country2 | Country2Dict
    editorial: list[LicenseEditorialContent | LicenseEditorialContentDict]
