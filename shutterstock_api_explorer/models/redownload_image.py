from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .auth_cookie6 import AuthCookie6, AuthCookie6Dict
from .enums.size10 import Size10OrStr


class RedownloadImage(SdkBaseModel):
    """Data required to redownload an image"""

    auth_cookie: Optional[AuthCookie6] = UNSET
    """(Deprecated)"""

    show_modal: Optional[bool] = UNSET
    """(Deprecated)"""

    size: Optional[Size10OrStr] = UNSET
    """Size of the image"""

    verification_code: Optional[str] = UNSET
    """(Deprecated)"""


class RedownloadImageDict(TypedDict):
    auth_cookie: NotRequired[AuthCookie6 | AuthCookie6Dict]
    show_modal: NotRequired[bool]
    size: NotRequired[Size10OrStr]
    verification_code: NotRequired[str]
