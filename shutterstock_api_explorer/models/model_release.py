from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ModelRelease(SdkBaseModel):
    """Model and property release metadata"""

    id: Optional[str] = UNSET
    """ID of the model or property release"""


class ModelReleaseDict(TypedDict):
    id: NotRequired[str]
