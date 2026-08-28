from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .editorial_category import EditorialCategory, EditorialCategoryDict


class EditorialCategoryResults(SdkBaseModel):
    """List of editorial categories"""

    data: Optional[list[EditorialCategory]] = UNSET
    """List of editorial categories"""


class EditorialCategoryResultsDict(TypedDict):
    data: NotRequired[list[EditorialCategory | EditorialCategoryDict]]
