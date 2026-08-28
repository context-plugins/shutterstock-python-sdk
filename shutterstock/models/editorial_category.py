from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class EditorialCategory(SdkBaseModel):
    """Name of an editorial category"""

    name: Optional[str] = UNSET


class EditorialCategoryDict(TypedDict):
    name: NotRequired[str]
