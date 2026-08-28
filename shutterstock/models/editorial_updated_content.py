from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, RFC3339DateTime, SdkBaseModel
from .commercial_status import CommercialStatus, CommercialStatusDict
from .editorial_assets import EditorialAssets, EditorialAssetsDict
from .editorial_category import EditorialCategory, EditorialCategoryDict
from .rights import Rights, RightsDict


class EditorialUpdatedContent(SdkBaseModel):
    """Metadata about updated editorial content"""

    commercial_status: Optional[CommercialStatus] = UNSET
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
    title: Optional[str] = UNSET
    updated_time: Optional[RFC3339DateTime] = UNSET
    created_time: Optional[RFC3339DateTime] = UNSET
    rights: Optional[Rights] = UNSET
    updates: Optional[list[str]] = UNSET
    supplier_code: Optional[str] = UNSET
    special_instructions: Optional[str] = UNSET


class EditorialUpdatedContentDict(TypedDict):
    commercial_status: NotRequired[CommercialStatus | CommercialStatusDict]
    aspect: NotRequired[float]
    assets: NotRequired[EditorialAssets | EditorialAssetsDict]
    byline: NotRequired[str]
    caption: NotRequired[str]
    categories: NotRequired[list[EditorialCategory | EditorialCategoryDict]]
    date_taken: NotRequired[Date]
    description: NotRequired[str]
    id: str
    keywords: NotRequired[list[str]]
    title: NotRequired[str]
    updated_time: NotRequired[RFC3339DateTime]
    created_time: NotRequired[RFC3339DateTime]
    rights: NotRequired[Rights | RightsDict]
    updates: NotRequired[list[str]]
    supplier_code: NotRequired[str]
    special_instructions: NotRequired[str]
