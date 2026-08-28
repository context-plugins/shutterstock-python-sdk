from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Suggestions(SdkBaseModel):
    """List of search suggestions"""

    data: Optional[list[str]] = UNSET
    """Search suggestions"""


class SuggestionsDict(TypedDict):
    data: NotRequired[list[str]]
