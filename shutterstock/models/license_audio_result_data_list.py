from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .license_audio_result import LicenseAudioResult, LicenseAudioResultDict


class LicenseAudioResultDataList(SdkBaseModel):
    """List of audio license results"""

    data: Optional[list[LicenseAudioResult]] = UNSET
    """License results"""

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


class LicenseAudioResultDataListDict(TypedDict):
    data: NotRequired[list[LicenseAudioResult | LicenseAudioResultDict]]
    errors: NotRequired[list[Error | ErrorDict]]
    message: NotRequired[str]
    page: NotRequired[int]
    per_page: NotRequired[int]
    total_count: NotRequired[int]
