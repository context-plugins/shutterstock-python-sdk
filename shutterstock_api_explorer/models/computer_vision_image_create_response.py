from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ComputerVisionImageCreateResponse(SdkBaseModel):
    """Asset upload information"""

    upload_id: str


class ComputerVisionImageCreateResponseDict(TypedDict):
    upload_id: str
