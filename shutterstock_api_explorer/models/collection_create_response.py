from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CollectionCreateResponse(SdkBaseModel):
    """Collection creation response"""

    id: str
    """ID of the new collection"""


class CollectionCreateResponseDict(TypedDict):
    id: str
