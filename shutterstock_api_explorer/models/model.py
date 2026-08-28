from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Model(SdkBaseModel):
    """Information about a human model or property that appears in media; used to search for assets that this model is
    in"""

    id: str
    """ID of the model"""


class ModelDict(TypedDict):
    id: str
