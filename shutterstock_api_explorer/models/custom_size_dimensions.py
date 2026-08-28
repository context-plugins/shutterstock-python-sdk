from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CustomSizeDimensions(SdkBaseModel):
    """A custom height or a custom width to resize the image to, but not both (experimental)"""

    height: Optional[int] = UNSET
    """Custom height to resize the image to"""

    width: Optional[int] = UNSET
    """Custom width to resize the image to"""


class CustomSizeDimensionsDict(TypedDict):
    height: NotRequired[int]
    width: NotRequired[int]
