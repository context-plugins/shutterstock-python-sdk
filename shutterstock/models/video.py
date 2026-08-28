from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .category import Category, CategoryDict
from .contributor import Contributor, ContributorDict
from .model import Model, ModelDict
from .model_release import ModelRelease, ModelReleaseDict
from .video_assets import VideoAssets, VideoAssetsDict


class Video(SdkBaseModel):
    """Information about a video"""

    added_date: Optional[Date] = UNSET
    """Date this video was added to the Shutterstock library"""

    affiliate_url: Optional[str] = UNSET
    """Affiliate referral link; appears only for registered affiliate partners"""

    aspect: Optional[float] = UNSET
    """Aspect ratio of this video in decimal format, such as 0.6667"""

    aspect_ratio: Optional[str] = UNSET
    """Aspect ratio of the video as a ratio, such as 16:9"""

    assets: Optional[VideoAssets] = UNSET
    """Video asset information"""

    categories: Optional[list[Category]] = UNSET
    """List of categories"""

    contributor: Contributor
    """Information about a contributor"""

    description: Optional[str] = UNSET
    """Description of this video"""

    duration: Optional[float] = UNSET
    """Duration of this video, in seconds"""

    has_model_release: Optional[bool] = UNSET
    """Whether or not this video has been released for use by the model appearing in it"""

    has_property_release: Optional[bool] = UNSET
    """Whether or not this video has received a release to show the landmark or property appearing in it"""

    id: str
    """ID of the video"""

    is_adult: Optional[bool] = UNSET
    """Whether or not this video contains adult content"""

    is_editorial: Optional[bool] = UNSET
    """Whether or not this video is editorial content"""

    is_select: Optional[bool] = UNSET
    """Whether or not this video is part of the select collection"""

    keywords: Optional[list[str]] = UNSET
    """Keywords associated with the content of this video"""

    media_type: str
    """Media type of this video, should always be "video"
    """

    models: Optional[list[Model]] = UNSET
    """List of models in this video"""

    releases: Optional[list[ModelRelease]] = UNSET
    """List of all releases of this video"""

    url: Optional[str] = UNSET
    """Link to video information page; included only for certain accounts"""


class VideoDict(TypedDict):
    added_date: NotRequired[Date]
    affiliate_url: NotRequired[str]
    aspect: NotRequired[float]
    aspect_ratio: NotRequired[str]
    assets: NotRequired[VideoAssets | VideoAssetsDict]
    categories: NotRequired[list[Category | CategoryDict]]
    contributor: Contributor | ContributorDict
    description: NotRequired[str]
    duration: NotRequired[float]
    has_model_release: NotRequired[bool]
    has_property_release: NotRequired[bool]
    id: str
    is_adult: NotRequired[bool]
    is_editorial: NotRequired[bool]
    is_select: NotRequired[bool]
    keywords: NotRequired[list[str]]
    media_type: str
    models: NotRequired[list[Model | ModelDict]]
    releases: NotRequired[list[ModelRelease | ModelReleaseDict]]
    url: NotRequired[str]
