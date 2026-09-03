from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.license1 import License1OrStr


class LicenseAudio(SdkBaseModel):
    """An audio track in a licensing request"""

    audio_id: str
    """ID of the track being licensed"""

    license: Optional[License1OrStr] = UNSET
    """Type of license"""

    search_id: Optional[str] = UNSET
    """ID of the search that led to this licensing event"""


class LicenseAudioDict(TypedDict):
    audio_id: str
    license: NotRequired[License1OrStr]
    search_id: NotRequired[str]
