from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SearchEntitiesResponse(SdkBaseModel):
    """The response to a request for keyword analysis"""

    keywords: Optional[list[str]] = UNSET
    """The top keywords from the submitted text"""


class SearchEntitiesResponseDict(TypedDict):
    keywords: NotRequired[list[str]]
