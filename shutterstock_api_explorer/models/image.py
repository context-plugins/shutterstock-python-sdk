from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .assets3 import Assets3, Assets3Dict
from .category import Category, CategoryDict
from .contributor import Contributor, ContributorDict
from .model import Model, ModelDict
from .model_release import ModelRelease, ModelReleaseDict


class Image(SdkBaseModel):
    """Information about an image"""

    added_date: Optional[Date] = UNSET
    """Date that the image was added by the contributor"""

    affiliate_url: Optional[AnyUrl] = UNSET
    """Affiliate referral link; appears only for registered affiliate partners"""

    aspect: Optional[float] = UNSET
    """Aspect ratio of the image in decimal format, such as 0.6667"""

    assets: Optional[Assets3] = UNSET
    """Image asset information"""

    categories: Optional[list[Category]] = UNSET
    """Categories that this image is a part of"""

    contributor: Contributor
    """Information about a contributor"""

    description: Optional[str] = UNSET
    """Detailed description of the image"""

    has_model_release: Optional[bool] = UNSET
    """Indicates whether there are model releases for the image"""

    has_property_release: Optional[bool] = UNSET
    """Indicates whether there are property releases for the image"""

    id: str
    """Image ID"""

    image_type: Optional[str] = UNSET
    """Type of image"""

    is_adult: Optional[bool] = UNSET
    """Whether or not this image contains adult content"""

    is_editorial: Optional[bool] = UNSET
    """Whether or not this image is editorial content"""

    is_illustration: Optional[bool] = UNSET
    """Whether or not this image is an illustration"""

    keywords: Optional[list[str]] = UNSET
    """Keywords associated with the content of this image"""

    media_type: str
    """Media type of this image, should always be "image"
    """

    model_releases: Optional[list[ModelRelease]] = UNSET
    """List of model releases"""

    models: Optional[list[Model]] = UNSET
    """List of models"""

    releases: Optional[list[str]] = UNSET
    """List of all releases of this image"""

    url: Optional[str] = UNSET
    """Link to image information page; included only for certain accounts"""


class ImageDict(TypedDict):
    added_date: NotRequired[Date]
    affiliate_url: NotRequired[AnyUrl]
    aspect: NotRequired[float]
    assets: NotRequired[Assets3 | Assets3Dict]
    categories: NotRequired[list[Category | CategoryDict]]
    contributor: Contributor | ContributorDict
    description: NotRequired[str]
    has_model_release: NotRequired[bool]
    has_property_release: NotRequired[bool]
    id: str
    image_type: NotRequired[str]
    is_adult: NotRequired[bool]
    is_editorial: NotRequired[bool]
    is_illustration: NotRequired[bool]
    keywords: NotRequired[list[str]]
    media_type: str
    model_releases: NotRequired[list[ModelRelease | ModelReleaseDict]]
    models: NotRequired[list[Model | ModelDict]]
    releases: NotRequired[list[str]]
    url: NotRequired[str]
