from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .cookie import Cookie, CookieDict
from .custom_size_dimensions import CustomSizeDimensions, CustomSizeDimensionsDict
from .enums.format7 import Format7OrStr
from .enums.size4 import Size4OrStr


class LicenseImage(SdkBaseModel):
    """Data required to license an image"""

    auth_cookie: Optional[Cookie] = UNSET
    """Cookie object"""

    editorial_acknowledgement: Optional[bool] = UNSET
    """Set to true to acknowledge the editorial agreement"""

    format: Optional[Format7OrStr] = UNSET
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

    size: Optional[Size4OrStr] = UNSET
    """Image size to download"""

    custom_dimensions: Optional[CustomSizeDimensions] = UNSET
    """A custom height or a custom width to resize the image to, but not both (experimental)"""

    subscription_id: Optional[str] = UNSET
    """ID of the subscription to use for the download."""

    verification_code: Optional[str] = UNSET
    """(Deprecated)"""


class LicenseImageDict(TypedDict):
    auth_cookie: NotRequired[Cookie | CookieDict]
    editorial_acknowledgement: NotRequired[bool]
    format: NotRequired[Format7OrStr]
    image_id: str
    metadata: NotRequired[Any]
    price: NotRequired[float]
    search_id: NotRequired[str]
    show_modal: NotRequired[bool]
    size: NotRequired[Size4OrStr]
    custom_dimensions: NotRequired[CustomSizeDimensions | CustomSizeDimensionsDict]
    subscription_id: NotRequired[str]
    verification_code: NotRequired[str]
