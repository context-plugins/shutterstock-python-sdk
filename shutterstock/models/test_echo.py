from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TestEcho(SdkBaseModel):
    """Text to echo in the response"""

    text: Optional[str] = UNSET


class TestEchoDict(TypedDict):
    text: NotRequired[str]
