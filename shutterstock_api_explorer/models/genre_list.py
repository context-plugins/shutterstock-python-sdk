from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class GenreList(SdkBaseModel):
    """List of audio genres"""

    data: list[str]
    """List of genres"""


class GenreListDict(TypedDict):
    data: list[str]
