from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Artist(SdkBaseModel):
    """Metadata about the artist that created the media"""

    name: str
    """The artist's name"""


class ArtistDict(TypedDict):
    name: str
