from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .license_audio import LicenseAudio, LicenseAudioDict


class LicenseAudioRequest(SdkBaseModel):
    """Audio license request data"""

    audio: list[LicenseAudio]
    """List of audio tracks to license"""


class LicenseAudioRequestDict(TypedDict):
    audio: list[LicenseAudio | LicenseAudioDict]
