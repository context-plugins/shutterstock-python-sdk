from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .audio_url import AudioUrl, AudioUrlDict


class LicenseAudioResult(SdkBaseModel):
    """The response to a licensing request for an audio track"""

    audio_id: str
    """ID of the track that was licensed"""

    allotment_charge: Optional[float] = UNSET
    """Number of credits that this licensing event used"""

    license_id: Optional[str] = UNSET
    """ID of the license event"""

    download: Optional[AudioUrl] = UNSET
    """Audio License URL object"""

    error: Optional[str] = UNSET
    """Error information if applicable"""


class LicenseAudioResultDict(TypedDict):
    audio_id: str
    allotment_charge: NotRequired[float]
    license_id: NotRequired[str]
    download: NotRequired[AudioUrl | AudioUrlDict]
    error: NotRequired[str]
