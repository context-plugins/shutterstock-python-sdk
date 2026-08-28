from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .download2 import Download2, Download2Dict


class LicenseEditorialContentResult(SdkBaseModel):
    """The response to a licensing request for editorial content"""

    allotment_charge: Optional[int] = UNSET
    """For pre-paid plans, how many credits were used for the item license"""

    download: Optional[Download2] = UNSET
    """Information that is needed to download the image"""

    editorial_id: str
    """Editorial ID"""

    error: Optional[str] = UNSET


class LicenseEditorialContentResultDict(TypedDict):
    allotment_charge: NotRequired[int]
    download: NotRequired[Download2 | Download2Dict]
    editorial_id: str
    error: NotRequired[str]
