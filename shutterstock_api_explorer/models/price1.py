from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Price1(SdkBaseModel):
    """Wholesale price information; only for rev-share partners"""

    local_amount: Optional[float] = UNSET
    """Floating-point amount of the calculated rev-share price in the currency local_currency"""

    local_currency: Optional[str] = UNSET
    """Currency of the rev-share price that was calculated"""


class Price1Dict(TypedDict):
    local_amount: NotRequired[float]
    local_currency: NotRequired[str]
