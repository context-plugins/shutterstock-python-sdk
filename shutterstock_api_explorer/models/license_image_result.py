from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .download2 import Download2, Download2Dict
from .price1 import Price1, Price1Dict


class LicenseImageResult(SdkBaseModel):
    """The response to a licensing request for an image"""

    allotment_charge: Optional[int] = UNSET
    """Number of credits that this licensing event used"""

    download: Optional[Download2] = UNSET
    """Information that is needed to download the image"""

    error: Optional[str] = UNSET
    """Error message, appears only if there was an error"""

    image_id: str
    """Image ID that was licensed"""

    license_id: Optional[str] = UNSET
    """ID of the license event"""

    price: Optional[Price1] = UNSET
    """Wholesale price information; only for rev-share partners"""


class LicenseImageResultDict(TypedDict):
    allotment_charge: NotRequired[int]
    download: NotRequired[Download2 | Download2Dict]
    error: NotRequired[str]
    image_id: str
    license_id: NotRequired[str]
    price: NotRequired[Price1 | Price1Dict]
