from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class MoodList(SdkBaseModel):
    """List of audio moods"""

    data: list[str]
    """List of audio moods"""


class MoodListDict(TypedDict):
    data: list[str]
