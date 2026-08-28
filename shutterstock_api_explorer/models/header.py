from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Header(SdkBaseModel):
    """Headers as included in the request"""

    user_agent: Optional[str] = Field(default=UNSET, alias="user-agent")
    """User agent to expect in the response"""


class HeaderDict(TypedDict):
    user_agent: NotRequired[str]
