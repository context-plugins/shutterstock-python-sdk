from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .price2 import Price2, Price2Dict
from .url import Url, UrlDict


class LicenseVideoResult(SdkBaseModel):
    """The response to a licensing request for a video"""

    allotment_charge: Optional[int] = UNSET
    """Number of credits that this licensing event used"""

    download: Optional[Url] = UNSET
    """URL object"""

    license_id: Optional[str] = UNSET
    """ID of the license event"""

    error: Optional[str] = UNSET
    """Potential error that occurred during licensing"""

    price: Optional[Price2] = UNSET
    """Wholesale price information; only for rev-share partners only"""

    video_id: str
    """ID of the video that was licensed"""


class LicenseVideoResultDict(TypedDict):
    allotment_charge: NotRequired[int]
    download: NotRequired[Url | UrlDict]
    license_id: NotRequired[str]
    error: NotRequired[str]
    price: NotRequired[Price2 | Price2Dict]
    video_id: str
