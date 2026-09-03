from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DownloadHistoryFormatDetails(SdkBaseModel):
    """Information about the format of a download"""

    format: Optional[str] = UNSET
    """The format of the downloaded media"""

    size: Optional[str] = UNSET
    """The size of the downloaded media"""


class DownloadHistoryFormatDetailsDict(TypedDict):
    format: NotRequired[str]
    size: NotRequired[str]
