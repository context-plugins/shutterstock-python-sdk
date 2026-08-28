from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .subscription import Subscription, SubscriptionDict


class SubscriptionDataList(SdkBaseModel):
    """List of subscriptions"""

    data: Optional[list[Subscription]] = UNSET
    """Subscriptions retrieved from this user"""

    errors: Optional[list[Error]] = UNSET
    """Error list; appears only if there was an error"""

    message: Optional[str] = UNSET
    """Optional error message"""

    page: Optional[int] = UNSET
    """Current page that is being queried"""

    per_page: Optional[int] = UNSET
    """Amount of subscriptions to show per page"""

    total_count: Optional[int] = UNSET
    """Total number of subscriptions for this user"""


class SubscriptionDataListDict(TypedDict):
    data: NotRequired[list[Subscription | SubscriptionDict]]
    errors: NotRequired[list[Error | ErrorDict]]
    message: NotRequired[str]
    page: NotRequired[int]
    per_page: NotRequired[int]
    total_count: NotRequired[int]
