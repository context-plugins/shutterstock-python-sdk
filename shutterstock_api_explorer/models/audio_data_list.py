from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .audio import Audio, AudioDict
from .error import Error, ErrorDict


class AudioDataList(SdkBaseModel):
    """List of tracks"""

    data: Optional[list[Audio]] = UNSET
    """Tracks"""

    errors: Optional[list[Error]] = UNSET
    """Error list; appears only if there was an error"""

    message: Optional[str] = UNSET
    """Server-generated message, if any"""

    page: Optional[int] = UNSET
    """Current page that is returned"""

    per_page: Optional[int] = UNSET
    """Number of results per page"""

    total_count: Optional[int] = UNSET
    """Total count of all results across all pages"""


class AudioDataListDict(TypedDict):
    data: NotRequired[list[Audio | AudioDict]]
    errors: NotRequired[list[Error | ErrorDict]]
    message: NotRequired[str]
    page: NotRequired[int]
    per_page: NotRequired[int]
    total_count: NotRequired[int]
