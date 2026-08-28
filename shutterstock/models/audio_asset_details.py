from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AudioAssetDetails(SdkBaseModel):
    """Information about a file that is part of an audio asset"""

    file_size: Optional[int] = UNSET
    """File size of the track"""

    url: Optional[str] = UNSET
    """URL the track is available at"""


class AudioAssetDetailsDict(TypedDict):
    file_size: NotRequired[int]
    url: NotRequired[str]
