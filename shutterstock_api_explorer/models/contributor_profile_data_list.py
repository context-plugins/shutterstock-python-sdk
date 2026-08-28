from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .contributor_profile import ContributorProfile, ContributorProfileDict
from .error import Error, ErrorDict


class ContributorProfileDataList(SdkBaseModel):
    """List of contributor profiles"""

    data: Optional[list[ContributorProfile]] = UNSET
    """Conributor profiles"""

    errors: Optional[list[Error]] = UNSET
    """Error list; appears only if there was an error"""

    message: Optional[str] = UNSET
    """Error message"""

    page: Optional[int] = UNSET
    """Page of response"""

    per_page: Optional[int] = UNSET
    """Number of contributors per page"""

    total_count: Optional[int] = UNSET
    """Total count of contributors for this request"""


class ContributorProfileDataListDict(TypedDict):
    data: NotRequired[list[ContributorProfile | ContributorProfileDict]]
    errors: NotRequired[list[Error | ErrorDict]]
    message: NotRequired[str]
    page: NotRequired[int]
    per_page: NotRequired[int]
    total_count: NotRequired[int]
