from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .editorial_assets import EditorialAssets, EditorialAssetsDict
from .editorial_category import EditorialCategory, EditorialCategoryDict


class EditorialContent(SdkBaseModel):
    """Metadata about editorial content"""

    aspect: Optional[float] = UNSET
    assets: Optional[EditorialAssets] = UNSET
    """Asset information, including size and thumbnail URLs"""

    byline: Optional[str] = UNSET
    caption: Optional[str] = UNSET
    categories: Optional[list[EditorialCategory]] = UNSET
    """List of categories"""

    date_taken: Optional[Date] = UNSET
    description: Optional[str] = UNSET
    id: str
    keywords: Optional[list[str]] = UNSET
    special_instructions: Optional[str] = UNSET
    title: Optional[str] = UNSET


class EditorialContentDict(TypedDict):
    aspect: NotRequired[float]
    assets: NotRequired[EditorialAssets | EditorialAssetsDict]
    byline: NotRequired[str]
    caption: NotRequired[str]
    categories: NotRequired[list[EditorialCategory | EditorialCategoryDict]]
    date_taken: NotRequired[Date]
    description: NotRequired[str]
    id: str
    keywords: NotRequired[list[str]]
    special_instructions: NotRequired[str]
    title: NotRequired[str]
