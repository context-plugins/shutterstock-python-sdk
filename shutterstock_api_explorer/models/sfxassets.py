from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sfxasset_details import SfxassetDetails, SfxassetDetailsDict


class Sfxassets(SdkBaseModel):
    """Files that are available as part of an sound effect asset"""

    preview_mp3: Optional[SfxassetDetails] = UNSET
    """Information about a file that is part of an sound effect asset"""

    waveform: Optional[SfxassetDetails] = UNSET
    """Information about a file that is part of an sound effect asset"""


class SfxassetsDict(TypedDict):
    preview_mp3: NotRequired[SfxassetDetails | SfxassetDetailsDict]
    waveform: NotRequired[SfxassetDetails | SfxassetDetailsDict]
