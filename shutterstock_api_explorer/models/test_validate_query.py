from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TestValidateQuery(SdkBaseModel):
    """Validation results"""

    id: int
    """Integer ID that was passed in the request"""

    tag: Optional[list[str]] = UNSET
    """List of tags that were passed in the request"""


class TestValidateQueryDict(TypedDict):
    id: int
    tag: NotRequired[list[str]]
