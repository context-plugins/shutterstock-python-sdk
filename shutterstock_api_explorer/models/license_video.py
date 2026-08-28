from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .cookie import Cookie, CookieDict
from .enums.size8 import Size8OrStr


class LicenseVideo(SdkBaseModel):
    """Data required to license a video"""

    auth_cookie: Optional[Cookie] = UNSET
    """Cookie object"""

    editorial_acknowledgement: Optional[bool] = UNSET
    """Whether or not this item is editorial content"""

    metadata: Optional[Any] = UNSET
    """Additional information for license requests for enterprise accounts and API subscriptions, 4 fields maximum;
    which fields are required is set by the account holder"""

    price: Optional[float] = UNSET
    """Retail price amount as a floating-point number in the transaction currency, such as 12.34; only for rev-share
    partners"""

    search_id: Optional[str] = UNSET
    """ID of the search that led to this licensing event"""

    show_modal: Optional[bool] = UNSET
    """(Deprecated)"""

    size: Optional[Size8OrStr] = UNSET
    """Size of the video being licensed"""

    subscription_id: Optional[str] = UNSET
    """ID of the subscription used for this license"""

    video_id: str
    """ID of the video being licensed"""


class LicenseVideoDict(TypedDict):
    auth_cookie: NotRequired[Cookie | CookieDict]
    editorial_acknowledgement: NotRequired[bool]
    metadata: NotRequired[Any]
    price: NotRequired[float]
    search_id: NotRequired[str]
    show_modal: NotRequired[bool]
    size: NotRequired[Size8OrStr]
    subscription_id: NotRequired[str]
    video_id: str
