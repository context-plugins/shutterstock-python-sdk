from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .allotment import Allotment, AllotmentDict
from .license_format import LicenseFormat, LicenseFormatDict
from .price import Price, PriceDict


class Subscription(SdkBaseModel):
    """Subscription information"""

    allotment: Optional[Allotment] = UNSET
    """An allotment of credits as part of a subscription"""

    description: Optional[str] = UNSET
    """Description of the subscription"""

    expiration_time: Optional[RFC3339DateTime] = UNSET
    """Date the subscription ends"""

    formats: Optional[list[LicenseFormat]] = UNSET
    """List of formats that are licensable for the subscription"""

    id: str
    """Unique internal identifier for the subscription"""

    license: Optional[str] = UNSET
    """Internal identifier for the type of subscription"""

    asset_type: Optional[str] = UNSET
    """Identifier for the type of assets associated with this subscription (images, videos, audio, editorial)"""

    metadata: Optional[Any] = UNSET
    """Subscription metadata; different for each customer"""

    price_per_download: Optional[Price] = UNSET
    """Price"""


class SubscriptionDict(TypedDict):
    allotment: NotRequired[Allotment | AllotmentDict]
    description: NotRequired[str]
    expiration_time: NotRequired[RFC3339DateTime]
    formats: NotRequired[list[LicenseFormat | LicenseFormatDict]]
    id: str
    license: NotRequired[str]
    asset_type: NotRequired[str]
    metadata: NotRequired[Any]
    price_per_download: NotRequired[Price | PriceDict]
