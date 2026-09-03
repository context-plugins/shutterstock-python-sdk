from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .auth_cookie6 import AuthCookie6, AuthCookie6Dict
from .enums.size11 import Size11OrStr


class RedownloadVideo(SdkBaseModel):
    """Data required to redownload a video"""

    auth_cookie: Optional[AuthCookie6] = UNSET
    """(Deprecated)"""

    show_modal: Optional[bool] = UNSET
    """(Deprecated)"""

    size: Optional[Size11OrStr] = UNSET
    """Size of the video"""

    verification_code: Optional[str] = UNSET
    """(Deprecated)"""


class RedownloadVideoDict(TypedDict):
    auth_cookie: NotRequired[AuthCookie6 | AuthCookie6Dict]
    show_modal: NotRequired[bool]
    size: NotRequired[Size11OrStr]
    verification_code: NotRequired[str]
