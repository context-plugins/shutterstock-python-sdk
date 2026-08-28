from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class InstrumentList(SdkBaseModel):
    """List of instruments"""

    data: list[str]
    """List of instruments"""


class InstrumentListDict(TypedDict):
    data: list[str]
