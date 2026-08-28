from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .cookie import Cookie, CookieDict
from .enums.format9 import Format9OrStr
from .enums.size6 import Size6OrStr


class LicenseImageVector(SdkBaseModel):
    """Data required to license an image"""

    auth_cookie: Optional[Cookie] = UNSET
    """Cookie object"""

    editorial_acknowledgement: Optional[bool] = UNSET
    """Set to true to acknowledge the editorial agreement"""

    format: Optional[Format9OrStr] = UNSET
    """(Deprecated) Image format to download"""

    image_id: str
    """Image ID"""

    metadata: Optional[Any] = UNSET
    """Additional information for license requests for enterprise accounts and API subscriptions, 4 fields maximum;
    which fields are required is set by the account holder"""

    price: Optional[float] = UNSET
    """For revenue-sharing transactions, the final cost to the end customer as a floating-point number in the
    transaction currency, such as 12.34"""

    search_id: Optional[str] = UNSET
    """ID of the search that led to this licensing transaction"""

    show_modal: Optional[bool] = UNSET
    """(Deprecated)"""

    size: Optional[Size6OrStr] = UNSET
    """Image size to download"""

    subscription_id: Optional[str] = UNSET
    """ID of the subscription to use for the download."""

    verification_code: Optional[str] = UNSET
    """(Deprecated)"""


class LicenseImageVectorDict(TypedDict):
    auth_cookie: NotRequired[Cookie | CookieDict]
    editorial_acknowledgement: NotRequired[bool]
    format: NotRequired[Format9OrStr]
    image_id: str
    metadata: NotRequired[Any]
    price: NotRequired[float]
    search_id: NotRequired[str]
    show_modal: NotRequired[bool]
    size: NotRequired[Size6OrStr]
    subscription_id: NotRequired[str]
    verification_code: NotRequired[str]
