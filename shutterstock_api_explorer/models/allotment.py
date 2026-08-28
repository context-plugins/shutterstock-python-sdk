from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class Allotment(SdkBaseModel):
    """An allotment of credits as part of a subscription"""

    downloads_left: Optional[int] = UNSET
    """Number of credits remaining in the subscription"""

    downloads_limit: Optional[int] = UNSET
    """Total number of credits available to this subscription"""

    end_time: Optional[RFC3339DateTime] = UNSET
    """Date the subscription ends"""

    start_time: Optional[RFC3339DateTime] = UNSET
    """Date the subscription started"""

    content_tiers: Optional[Any] = UNSET
    """Downloads left and limit values for each content tier in the license"""


class AllotmentDict(TypedDict):
    downloads_left: NotRequired[int]
    downloads_limit: NotRequired[int]
    end_time: NotRequired[RFC3339DateTime]
    start_time: NotRequired[RFC3339DateTime]
    content_tiers: NotRequired[Any]
