from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AuthCookie6(SdkBaseModel):
    """(Deprecated)"""

    name: str
    """The name of the cookie"""

    value: str
    """The value of the cookie"""


class AuthCookie6Dict(TypedDict):
    name: str
    value: str
