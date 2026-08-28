from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Query(SdkBaseModel):
    """Query as included in the request"""

    id: int
    """Integer ID that was passed in the request"""

    tag: Optional[list[str]] = UNSET
    """List of tags that were passed in the request"""


class QueryDict(TypedDict):
    id: int
    tag: NotRequired[list[str]]
