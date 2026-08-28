from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .download_history_media_details import DownloadHistoryMediaDetails, DownloadHistoryMediaDetailsDict
from .download_history_revshare_details import DownloadHistoryRevshareDetails, DownloadHistoryRevshareDetailsDict
from .download_history_user_details import DownloadHistoryUserDetails, DownloadHistoryUserDetailsDict


class DownloadHistory(SdkBaseModel):
    """Information about a downloaded media item. Applicable for all media types, only one of 'audio', 'image' or
    'video' will be in a single DownloadHistory object"""

    audio: Optional[DownloadHistoryMediaDetails] = UNSET
    """Information about the downloaded media"""

    download_time: RFC3339DateTime
    """Date the media was downloaded the first time"""

    id: str
    """ID of the download"""

    image: Optional[DownloadHistoryMediaDetails] = UNSET
    """Information about the downloaded media"""

    is_downloadable: Optional[bool] = UNSET
    """Specifies if the media is downloadable via its respective downloads endpoint"""

    license: str
    """The name of the license of this download"""

    metadata: Optional[Any] = UNSET
    """The metadata that was passed in the original licensing request"""

    subscription_id: Optional[str] = UNSET
    """ID of the subscription used to perform this download"""

    user: Optional[DownloadHistoryUserDetails] = UNSET
    """Information about a user"""

    video: Optional[DownloadHistoryMediaDetails] = UNSET
    """Information about the downloaded media"""

    revshare: Optional[DownloadHistoryRevshareDetails] = UNSET
    """Pricing information for revenue-sharing transactions"""


class DownloadHistoryDict(TypedDict):
    audio: NotRequired[DownloadHistoryMediaDetails | DownloadHistoryMediaDetailsDict]
    download_time: RFC3339DateTime
    id: str
    image: NotRequired[DownloadHistoryMediaDetails | DownloadHistoryMediaDetailsDict]
    is_downloadable: NotRequired[bool]
    license: str
    metadata: NotRequired[Any]
    subscription_id: NotRequired[str]
    user: NotRequired[DownloadHistoryUserDetails | DownloadHistoryUserDetailsDict]
    video: NotRequired[DownloadHistoryMediaDetails | DownloadHistoryMediaDetailsDict]
    revshare: NotRequired[DownloadHistoryRevshareDetails | DownloadHistoryRevshareDetailsDict]
