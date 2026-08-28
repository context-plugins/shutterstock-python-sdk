from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.size import SizeOrStr


class LicenseEditorialContent(SdkBaseModel):
    """Individual editorial content to license"""

    editorial_id: str
    """Editorial ID"""

    license: str
    """License agreement to use for licensing"""

    metadata: Optional[Any] = UNSET
    """Additional information for license requests for enterprise accounts and API subscriptions, 4 fields maximum;
    which fields are required is set by the account holder"""

    size: Optional[SizeOrStr] = UNSET
    """Asset size to download"""


class LicenseEditorialContentDict(TypedDict):
    editorial_id: str
    license: str
    metadata: NotRequired[Any]
    size: NotRequired[SizeOrStr]
