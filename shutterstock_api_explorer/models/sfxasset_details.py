from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SfxassetDetails(SdkBaseModel):
    """Information about a file that is part of an sound effect asset"""

    file_size: Optional[int] = UNSET
    """File size of the sound effect"""

    url: Optional[str] = UNSET
    """URL the sound effect is available at"""


class SfxassetDetailsDict(TypedDict):
    file_size: NotRequired[int]
    url: NotRequired[str]
