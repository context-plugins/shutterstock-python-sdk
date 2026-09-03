from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Category(SdkBaseModel):
    """Category information"""

    id: Optional[str] = UNSET
    """Category ID"""

    name: Optional[str] = UNSET
    """Category name"""


class CategoryDict(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
