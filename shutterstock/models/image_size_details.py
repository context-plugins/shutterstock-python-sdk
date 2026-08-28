from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ImageSizeDetails(SdkBaseModel):
    """Image size information"""

    display_name: Optional[str] = UNSET
    """Display name of this image size"""

    dpi: Optional[int] = UNSET
    file_size: Optional[int] = UNSET
    """File size (in bytes) of this image size"""

    format: Optional[str] = UNSET
    """Format of this image size"""

    height: Optional[int] = UNSET
    """Height of this image size"""

    is_licensable: Optional[bool] = UNSET
    """Whether or not this image can be licensed in this image size"""

    width: Optional[int] = UNSET
    """Width of this image size"""


class ImageSizeDetailsDict(TypedDict):
    display_name: NotRequired[str]
    dpi: NotRequired[int]
    file_size: NotRequired[int]
    format: NotRequired[str]
    height: NotRequired[int]
    is_licensable: NotRequired[bool]
    width: NotRequired[int]
