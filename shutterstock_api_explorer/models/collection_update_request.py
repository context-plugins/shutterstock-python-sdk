from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CollectionUpdateRequest(SdkBaseModel):
    """Collection update request"""

    name: str
    """The new name of the collection"""


class CollectionUpdateRequestDict(TypedDict):
    name: str
