from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .image_search_results import ImageSearchResults, ImageSearchResultsDict


class BulkImageSearchResults(SdkBaseModel):
    """List of search results for each given query"""

    results: Optional[list[ImageSearchResults]] = UNSET
    """List of image search results"""

    bulk_search_id: Optional[str] = UNSET
    """Unique identifier for the search request"""


class BulkImageSearchResultsDict(TypedDict):
    results: NotRequired[list[ImageSearchResults | ImageSearchResultsDict]]
    bulk_search_id: NotRequired[str]
