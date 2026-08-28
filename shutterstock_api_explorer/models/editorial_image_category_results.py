from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .editorial_category import EditorialCategory, EditorialCategoryDict


class EditorialImageCategoryResults(SdkBaseModel):
    """List of editorial categories"""

    data: Optional[list[EditorialCategory]] = UNSET


class EditorialImageCategoryResultsDict(TypedDict):
    data: NotRequired[list[EditorialCategory | EditorialCategoryDict]]
