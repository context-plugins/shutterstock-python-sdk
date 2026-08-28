from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DownloadHistoryUserDetails(SdkBaseModel):
    """Information about a user"""

    username: str
    """The name of the user who downloaded the item"""


class DownloadHistoryUserDetailsDict(TypedDict):
    username: str
