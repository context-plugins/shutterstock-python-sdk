from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.license3 import License3OrStr
from .enums.size2 import Size2OrStr


class LicenseEditorialVideoContent(SdkBaseModel):
    """Individual editorial video content to license"""

    editorial_id: str
    """Editorial ID"""

    license: License3OrStr
    """License agreement to use for licensing"""

    metadata: Optional[Any] = UNSET
    """Additional information for license requests for enterprise accounts and API subscriptions, 4 fields maximum;
    which fields are required is set by the account holder"""

    size: Optional[Size2OrStr] = UNSET
    """Asset size to download"""


class LicenseEditorialVideoContentDict(TypedDict):
    editorial_id: str
    license: License3OrStr
    metadata: NotRequired[Any]
    size: NotRequired[Size2OrStr]
