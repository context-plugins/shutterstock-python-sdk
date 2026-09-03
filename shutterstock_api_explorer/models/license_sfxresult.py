from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .download6 import Download6, Download6Dict


class LicenseSfxresult(SdkBaseModel):
    """The response to a licensing request for an sound effects"""

    allotment_charge: Optional[int] = UNSET
    """Number of credits that this licensing event used"""

    download: Optional[Download6] = UNSET
    """Information that is needed to download the sound effects"""

    error: Optional[str] = UNSET
    """Error message, appears only if there was an error"""

    sfx_id: str
    """Sound effects ID that was licensed"""

    license_id: Optional[str] = UNSET
    """ID of the license event"""


class LicenseSfxresultDict(TypedDict):
    allotment_charge: NotRequired[int]
    download: NotRequired[Download6 | Download6Dict]
    error: NotRequired[str]
    sfx_id: str
    license_id: NotRequired[str]
