from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .image_size_details import ImageSizeDetails, ImageSizeDetailsDict
from .thumbnail import Thumbnail, ThumbnailDict


class ImageAssets(SdkBaseModel):
    """Information about the assets that are part of an image"""

    huge_jpg: Optional[ImageSizeDetails] = UNSET
    """Image size information"""

    huge_thumb: Optional[Thumbnail] = UNSET
    """Image thumbnail information"""

    large_thumb: Optional[Thumbnail] = UNSET
    """Image thumbnail information"""

    medium_jpg: Optional[ImageSizeDetails] = UNSET
    """Image size information"""

    preview: Optional[Thumbnail] = UNSET
    """Image thumbnail information"""

    preview_1000: Optional[Thumbnail] = UNSET
    """Image thumbnail information"""

    preview_1500: Optional[Thumbnail] = UNSET
    """Image thumbnail information"""

    small_jpg: Optional[ImageSizeDetails] = UNSET
    """Image size information"""

    small_thumb: Optional[Thumbnail] = UNSET
    """Image thumbnail information"""

    supersize_jpg: Optional[ImageSizeDetails] = UNSET
    """Image size information"""

    vector_eps: Optional[ImageSizeDetails] = UNSET
    """Image size information"""

    mosaic: Optional[Thumbnail] = UNSET
    """Image thumbnail information"""


class ImageAssetsDict(TypedDict):
    huge_jpg: NotRequired[ImageSizeDetails | ImageSizeDetailsDict]
    huge_thumb: NotRequired[Thumbnail | ThumbnailDict]
    large_thumb: NotRequired[Thumbnail | ThumbnailDict]
    medium_jpg: NotRequired[ImageSizeDetails | ImageSizeDetailsDict]
    preview: NotRequired[Thumbnail | ThumbnailDict]
    preview_1000: NotRequired[Thumbnail | ThumbnailDict]
    preview_1500: NotRequired[Thumbnail | ThumbnailDict]
    small_jpg: NotRequired[ImageSizeDetails | ImageSizeDetailsDict]
    small_thumb: NotRequired[Thumbnail | ThumbnailDict]
    supersize_jpg: NotRequired[ImageSizeDetails | ImageSizeDetailsDict]
    vector_eps: NotRequired[ImageSizeDetails | ImageSizeDetailsDict]
    mosaic: NotRequired[Thumbnail | ThumbnailDict]
