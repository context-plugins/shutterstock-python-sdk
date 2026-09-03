from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.media_type import MediaTypeOrStr


class LicenseFormat(SdkBaseModel):
    """Description of a license"""

    description: Optional[str] = UNSET
    """Description of the license"""

    format: Optional[str] = UNSET
    """Format or extension of the media, such as mpeg for videos or jpeg for images"""

    media_type: Optional[MediaTypeOrStr] = UNSET
    """Media type of the license"""

    min_resolution: Optional[int] = UNSET
    """Width of the media, in pixels, allowed by this license"""

    size: Optional[str] = UNSET
    """Keyword that details the size of the media, such as hd or sd for video, huge or vector for images"""


class LicenseFormatDict(TypedDict):
    description: NotRequired[str]
    format: NotRequired[str]
    media_type: NotRequired[MediaTypeOrStr]
    min_resolution: NotRequired[int]
    size: NotRequired[str]
