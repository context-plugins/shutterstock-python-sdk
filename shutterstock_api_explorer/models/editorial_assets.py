from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .image_size_details import ImageSizeDetails, ImageSizeDetailsDict
from .thumbnail import Thumbnail, ThumbnailDict


class EditorialAssets(SdkBaseModel):
    """Asset information, including size and thumbnail URLs"""

    original: Optional[ImageSizeDetails] = UNSET
    """Image size information"""

    thumb_170: Optional[Thumbnail] = UNSET
    """Image thumbnail information"""

    thumb_220: Optional[Thumbnail] = UNSET
    """Image thumbnail information"""

    watermark_450: Optional[Thumbnail] = UNSET
    """Image thumbnail information"""

    watermark_1500: Optional[Thumbnail] = UNSET
    """Image thumbnail information"""

    small_jpg: Optional[ImageSizeDetails] = UNSET
    """Image size information"""

    medium_jpg: Optional[ImageSizeDetails] = UNSET
    """Image size information"""


class EditorialAssetsDict(TypedDict):
    original: NotRequired[ImageSizeDetails | ImageSizeDetailsDict]
    thumb_170: NotRequired[Thumbnail | ThumbnailDict]
    thumb_220: NotRequired[Thumbnail | ThumbnailDict]
    watermark_450: NotRequired[Thumbnail | ThumbnailDict]
    watermark_1500: NotRequired[Thumbnail | ThumbnailDict]
    small_jpg: NotRequired[ImageSizeDetails | ImageSizeDetailsDict]
    medium_jpg: NotRequired[ImageSizeDetails | ImageSizeDetailsDict]
