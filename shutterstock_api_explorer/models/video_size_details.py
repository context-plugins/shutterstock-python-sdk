from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class VideoSizeDetails(SdkBaseModel):
    """Video asset information"""

    display_name: Optional[str] = UNSET
    """Display name of this video size"""

    file_size: Optional[int] = UNSET
    """File size (in bytes) of this video size"""

    format: Optional[str] = UNSET
    """Format of this video size"""

    fps: Optional[float] = UNSET
    """Frames per second of this video size"""

    height: Optional[int] = UNSET
    """Height of this video size"""

    is_licensable: Optional[bool] = UNSET
    """Whether or not videos can be licensed in this video size"""

    width: Optional[int] = UNSET
    """Width of this video size"""


class VideoSizeDetailsDict(TypedDict):
    display_name: NotRequired[str]
    file_size: NotRequired[int]
    format: NotRequired[str]
    fps: NotRequired[float]
    height: NotRequired[int]
    is_licensable: NotRequired[bool]
    width: NotRequired[int]
