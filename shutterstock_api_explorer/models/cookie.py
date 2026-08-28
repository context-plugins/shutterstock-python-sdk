from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Cookie(SdkBaseModel):
    """Cookie object"""

    name: str
    """The name of the cookie"""

    value: str
    """The value of the cookie"""


class CookieDict(TypedDict):
    name: str
    value: str
