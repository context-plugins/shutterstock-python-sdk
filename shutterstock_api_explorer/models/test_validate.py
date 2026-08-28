from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .header import Header, HeaderDict
from .query import Query, QueryDict


class TestValidate(SdkBaseModel):
    """Validation results"""

    header: Optional[Header] = UNSET
    """Headers as included in the request"""

    query: Optional[Query] = UNSET
    """Query as included in the request"""


class TestValidateDict(TypedDict):
    header: NotRequired[Header | HeaderDict]
    query: NotRequired[Query | QueryDict]
