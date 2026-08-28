from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .download_history import DownloadHistory, DownloadHistoryDict
from .error import Error, ErrorDict


class DownloadHistoryDataList(SdkBaseModel):
    """List of download events"""

    data: Optional[list[DownloadHistory]] = UNSET
    """Download events"""

    errors: Optional[list[Error]] = UNSET
    """Error list; appears only if there was an error"""

    message: Optional[str] = UNSET
    """Server-generated message, if any"""

    page: Optional[int] = UNSET
    """The current page of results"""

    per_page: Optional[int] = UNSET
    """The number of results per page"""

    total_count: Optional[int] = UNSET
    """The total number of results across all pages"""


class DownloadHistoryDataListDict(TypedDict):
    data: NotRequired[list[DownloadHistory | DownloadHistoryDict]]
    errors: NotRequired[list[Error | ErrorDict]]
    message: NotRequired[str]
    page: NotRequired[int]
    per_page: NotRequired[int]
    total_count: NotRequired[int]
