from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .editorial_category import EditorialCategory, EditorialCategoryDict
from .editorial_video_assets import EditorialVideoAssets, EditorialVideoAssetsDict


class EditorialVideoContent(SdkBaseModel):
    """Metadata about editorial content"""

    aspect: Optional[float] = UNSET
    assets: Optional[EditorialVideoAssets] = UNSET
    """Asset information, including size and thumbnail URLs"""

    byline: Optional[str] = UNSET
    caption: Optional[str] = UNSET
    categories: Optional[list[EditorialCategory]] = UNSET
    """List of categories"""

    date_taken: Optional[Date] = UNSET
    description: Optional[str] = UNSET
    id: str
    keywords: Optional[list[str]] = UNSET
    title: Optional[str] = UNSET


class EditorialVideoContentDict(TypedDict):
    aspect: NotRequired[float]
    assets: NotRequired[EditorialVideoAssets | EditorialVideoAssetsDict]
    byline: NotRequired[str]
    caption: NotRequired[str]
    categories: NotRequired[list[EditorialCategory | EditorialCategoryDict]]
    date_taken: NotRequired[Date]
    description: NotRequired[str]
    id: str
    keywords: NotRequired[list[str]]
    title: NotRequired[str]
