from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .license_sfx import LicenseSfx, LicenseSfxDict


class LicenseSfxrequest(SdkBaseModel):
    """License sounds effect asset request body"""

    sound_effects: list[LicenseSfx]
    """Sound effects to license for"""


class LicenseSfxrequestDict(TypedDict):
    sound_effects: list[LicenseSfx | LicenseSfxDict]
