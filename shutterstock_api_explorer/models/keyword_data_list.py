from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class KeywordDataList(SdkBaseModel):
    """List of keywords"""

    data: Optional[list[str]] = UNSET
    """Keywords"""

    errors: Optional[list[Error]] = UNSET
    """Error list; appears only if there was an error"""

    message: Optional[str] = UNSET
    """Server-generated message, if any"""


class KeywordDataListDict(TypedDict):
    data: NotRequired[list[str]]
    errors: NotRequired[list[Error | ErrorDict]]
    message: NotRequired[str]
