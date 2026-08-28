from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .license_editorial_content_result import LicenseEditorialContentResult, LicenseEditorialContentResultDict


class LicenseEditorialContentResults(SdkBaseModel):
    """List of editorial license results"""

    data: Optional[list[LicenseEditorialContentResult]] = UNSET
    """License results"""

    errors: Optional[list[Error]] = UNSET
    """Error list; appears only if there was an error"""

    message: Optional[str] = UNSET
    """Optional error message"""

    page: Optional[int] = UNSET
    """Current page of the response"""

    per_page: Optional[int] = UNSET
    """Number of results per page"""

    total_count: Optional[int] = UNSET
    """Total count of all results"""


class LicenseEditorialContentResultsDict(TypedDict):
    data: NotRequired[list[LicenseEditorialContentResult | LicenseEditorialContentResultDict]]
    errors: NotRequired[list[Error | ErrorDict]]
    message: NotRequired[str]
    page: NotRequired[int]
    per_page: NotRequired[int]
    total_count: NotRequired[int]
