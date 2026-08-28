from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Recommendation(SdkBaseModel):
    """Media Recommendation"""

    id: str
    """Media ID"""


class RecommendationDict(TypedDict):
    id: str
