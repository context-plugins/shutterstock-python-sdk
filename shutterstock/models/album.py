from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Album(SdkBaseModel):
    """Album metadata"""

    id: str
    """The album ID"""

    title: str
    """The album title"""


class AlbumDict(TypedDict):
    id: str
    title: str
