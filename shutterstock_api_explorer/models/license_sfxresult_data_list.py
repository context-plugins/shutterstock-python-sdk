from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .license_sfxresult import LicenseSfxresult, LicenseSfxresultDict


class LicenseSfxresultDataList(SdkBaseModel):
    """List of information about licensed sound effects"""

    data: Optional[list[LicenseSfxresult]] = UNSET
    """Sound effects license results"""

    errors: Optional[list[Error]] = UNSET
    """Error list; appears only if there was an error"""

    message: Optional[str] = UNSET
    """Server-generated message, if any"""


class LicenseSfxresultDataListDict(TypedDict):
    data: NotRequired[list[LicenseSfxresult | LicenseSfxresultDict]]
    errors: NotRequired[list[Error | ErrorDict]]
    message: NotRequired[str]
