from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DownloadHistoryRevshareDetails(SdkBaseModel):
    """Pricing information for revenue-sharing transactions"""

    purchase_amount: str
    """The amount charged for the license"""

    purchase_currency: str
    """The currency the amount was charged in"""


class DownloadHistoryRevshareDetailsDict(TypedDict):
    purchase_amount: str
    purchase_currency: str
