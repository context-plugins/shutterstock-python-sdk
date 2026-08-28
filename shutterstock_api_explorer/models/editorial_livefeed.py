from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .editorial_cover_item import EditorialCoverItem, EditorialCoverItemDict


class EditorialLivefeed(SdkBaseModel):
    """Metadata about editorial livefeed"""

    cover_item: Optional[EditorialCoverItem] = UNSET
    """Cover image for editorial livefeed"""

    created_time: Optional[RFC3339DateTime] = UNSET
    """When the livefeed was initially created"""

    id: str
    """Livefeed ID"""

    name: str
    """Name of the livefeed"""

    total_item_count: int
    """Total count of items in the livefeed"""


class EditorialLivefeedDict(TypedDict):
    cover_item: NotRequired[EditorialCoverItem | EditorialCoverItemDict]
    created_time: NotRequired[RFC3339DateTime]
    id: str
    name: str
    total_item_count: int
