from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class UpdatedMedia(SdkBaseModel):
    """Information about a piece of updated media"""

    id: str
    """ID of the media"""

    updated_time: RFC3339DateTime
    """Date that the media was updated"""

    updates: list[str]
    """Types of updates that were made to the piece of media"""


class UpdatedMediaDict(TypedDict):
    id: str
    updated_time: RFC3339DateTime
    updates: list[str]
