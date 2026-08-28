from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TestValidateHeader(SdkBaseModel):
    """Validation results"""

    user_agent: Optional[str] = Field(default=UNSET, alias="user-agent")
    """User agent to expect in the response"""


class TestValidateHeaderDict(TypedDict):
    user_agent: NotRequired[str]
