from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .download_history_format_details import DownloadHistoryFormatDetails, DownloadHistoryFormatDetailsDict


class DownloadHistoryMediaDetails(SdkBaseModel):
    """Information about the downloaded media"""

    format: Optional[DownloadHistoryFormatDetails] = UNSET
    """Information about the format of a download"""

    id: str
    """ID of the download history media details"""


class DownloadHistoryMediaDetailsDict(TypedDict):
    format: NotRequired[DownloadHistoryFormatDetails | DownloadHistoryFormatDetailsDict]
    id: str
