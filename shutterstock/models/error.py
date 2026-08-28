from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Error(SdkBaseModel):
    """Error object"""

    code: Optional[str] = UNSET
    """The error code of this error"""

    data: Optional[str] = UNSET
    """Debugging information about the error"""

    items: Optional[list[Any]] = UNSET
    """A list of items that produced the error"""

    message: str
    """Specific details about this error"""

    path: Optional[str] = UNSET
    """Internal code reference to the source of the error"""


class ErrorDict(TypedDict):
    code: NotRequired[str]
    data: NotRequired[str]
    items: NotRequired[list[Any]]
    message: str
    path: NotRequired[str]
