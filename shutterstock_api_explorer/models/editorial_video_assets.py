from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .video_preview_url import VideoPreviewUrl, VideoPreviewUrlDict
from .video_size_details import VideoSizeDetails, VideoSizeDetailsDict


class EditorialVideoAssets(SdkBaseModel):
    """Asset information, including size and thumbnail URLs"""

    original: Optional[VideoSizeDetails] = UNSET
    """Video asset information"""

    preview_mp4: Optional[VideoPreviewUrl] = UNSET
    """Video preview information"""

    preview_webm: Optional[VideoPreviewUrl] = UNSET
    """Video preview information"""

    thumb_jpg: Optional[VideoPreviewUrl] = UNSET
    """Video preview information"""


class EditorialVideoAssetsDict(TypedDict):
    original: NotRequired[VideoSizeDetails | VideoSizeDetailsDict]
    preview_mp4: NotRequired[VideoPreviewUrl | VideoPreviewUrlDict]
    preview_webm: NotRequired[VideoPreviewUrl | VideoPreviewUrlDict]
    thumb_jpg: NotRequired[VideoPreviewUrl | VideoPreviewUrlDict]
