from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CollectionCreateRequest(SdkBaseModel):
    """Collection creation request"""

    name: str
    """The name of the collection"""


class CollectionCreateRequestDict(TypedDict):
    name: str
