from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class CollectionItem(SdkBaseModel):
    """Metadata about an item that is part of a collection"""

    added_time: Optional[RFC3339DateTime] = UNSET
    """The date the item was added to the collection"""

    id: str
    """ID of the item"""

    media_type: Optional[str] = UNSET
    """The media type of the item, such as image, video, or audio"""


class CollectionItemDict(TypedDict):
    added_time: NotRequired[RFC3339DateTime]
    id: str
    media_type: NotRequired[str]
