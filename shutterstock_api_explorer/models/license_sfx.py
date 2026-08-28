from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.audio_layout import AudioLayoutOrStr
from .enums.format11 import Format11OrStr


class LicenseSfx(SdkBaseModel):
    sfx_id: str
    """ID of the sounds effect being licensed"""

    audio_layout: Optional[AudioLayoutOrStr] = UNSET
    format: Optional[Format11OrStr] = UNSET
    search_id: Optional[str] = UNSET
    """ID of the search that led to this licensing event"""

    subscription_id: str
    """ID of the subscription to use for the download."""


class LicenseSfxDict(TypedDict):
    sfx_id: str
    audio_layout: NotRequired[AudioLayoutOrStr]
    format: NotRequired[Format11OrStr]
    search_id: NotRequired[str]
    subscription_id: str
