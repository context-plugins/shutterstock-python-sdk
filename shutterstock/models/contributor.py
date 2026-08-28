from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Contributor(SdkBaseModel):
    """Information about a contributor"""

    id: str
    """ID of the contributor"""


class ContributorDict(TypedDict):
    id: str
