from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .url import Url, UrlDict
from .urls import Urls, UrlsDict
from .video_size_details import VideoSizeDetails, VideoSizeDetailsDict


class VideoAssets(SdkBaseModel):
    """Video asset information"""

    k4: Optional[VideoSizeDetails] = Field(default=UNSET, alias="4k")
    """Video asset information"""

    hd: Optional[VideoSizeDetails] = UNSET
    """Video asset information"""

    preview_jpg: Optional[Url] = UNSET
    """URL object"""

    preview_mp4: Optional[Url] = UNSET
    """URL object"""

    preview_webm: Optional[Url] = UNSET
    """URL object"""

    sd: Optional[VideoSizeDetails] = UNSET
    """Video asset information"""

    thumb_jpg: Optional[Url] = UNSET
    """URL object"""

    thumb_jpgs: Optional[Urls] = UNSET
    """List of URLs"""

    thumb_mp4: Optional[Url] = UNSET
    """URL object"""

    thumb_webm: Optional[Url] = UNSET
    """URL object"""

    web: Optional[VideoSizeDetails] = UNSET
    """Video asset information"""


class VideoAssetsDict(TypedDict):
    k4: NotRequired[VideoSizeDetails | VideoSizeDetailsDict]
    hd: NotRequired[VideoSizeDetails | VideoSizeDetailsDict]
    preview_jpg: NotRequired[Url | UrlDict]
    preview_mp4: NotRequired[Url | UrlDict]
    preview_webm: NotRequired[Url | UrlDict]
    sd: NotRequired[VideoSizeDetails | VideoSizeDetailsDict]
    thumb_jpg: NotRequired[Url | UrlDict]
    thumb_jpgs: NotRequired[Urls | UrlsDict]
    thumb_mp4: NotRequired[Url | UrlDict]
    thumb_webm: NotRequired[Url | UrlDict]
    web: NotRequired[VideoSizeDetails | VideoSizeDetailsDict]
