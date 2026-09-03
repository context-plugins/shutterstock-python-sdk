from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .enums.image_type import ImageTypeOrStr
from .enums.language2 import Language2OrStr
from .enums.license import LicenseOrStr
from .enums.orientation import OrientationOrStr
from .enums.people_age import PeopleAgeOrStr
from .enums.people_ethnicity import PeopleEthnicityOrStr
from .enums.people_gender import PeopleGenderOrStr
from .enums.sort import SortOrStr
from .enums.view import ViewOrStr
from .unions.contributor_country import ContributorCountry, ContributorCountryDict
from .unions.region import Region, RegionDict


class SearchImage(SdkBaseModel):
    """Data required to search for an image"""

    added_date: Optional[Date] = UNSET
    """Show images added on the specified date"""

    added_date_start: Optional[Date] = UNSET
    """Show images added on or after the specified date"""

    aspect_ratio_min: Optional[float] = UNSET
    """Show images with the specified aspect ratio or higher, using a positive decimal of the width divided by the
    height, such as 1.7778 for a 16:9 image"""

    aspect_ratio_max: Optional[float] = UNSET
    """Show images with the specified aspect ratio or lower, using a positive decimal of the width divided by the
    height, such as 1.7778 for a 16:9 image"""

    aspect_ratio: Optional[float] = UNSET
    """Show images with the specified aspect ratio, using a positive decimal of the width divided by the height, such as
    1.7778 for a 16:9 image"""

    added_date_end: Optional[Date] = UNSET
    """Show images added before the specified date"""

    authentic: Optional[bool] = UNSET
    """Show only authentic images"""

    category: Optional[str] = UNSET
    """Show images with the specified Shutterstock-defined category; specify a category name or ID"""

    color: Optional[str] = UNSET
    """Specify either a hexadecimal color in the format '4F21EA' or 'grayscale'; the API returns images that use similar
    colors"""

    contributor: Optional[list[str]] = UNSET
    """Show images with the specified contributor names or IDs, allows multiple"""

    contributor_country: Optional[ContributorCountry] = UNSET
    """Show images from contributors in one or more specified countries, or start with NOT to exclude a country from the
    search"""

    fields: Optional[str] = UNSET
    """Fields to display in the response; see the documentation for the fields parameter in the overview section"""

    height: Optional[int] = UNSET
    """(Deprecated; use height_from and height_to instead) Show images with the specified height"""

    height_from: Optional[int] = UNSET
    """Show images with the specified height or larger, in pixels"""

    height_to: Optional[int] = UNSET
    """Show images with the specified height or smaller, in pixels"""

    image_type: Optional[list[ImageTypeOrStr]] = UNSET
    """Show images of the specified type"""

    keyword_safe_search: Optional[bool] = UNSET
    """Hide results with potentially unsafe keywords"""

    language: Optional[Language2OrStr] = UNSET
    """Set query and result language (uses Accept-Language header if not set)"""

    license: Optional[list[LicenseOrStr]] = UNSET
    """Show only images with the specified license"""

    model: Optional[list[str]] = UNSET
    """Show image results with the specified model IDs"""

    orientation: Optional[OrientationOrStr] = UNSET
    """Show image results with horizontal or vertical orientation"""

    page: Optional[int] = UNSET
    """Page number"""

    per_page: Optional[int] = UNSET
    """Number of results per page"""

    people_model_released: Optional[bool] = UNSET
    """Show images of people with a signed model release"""

    people_age: Optional[PeopleAgeOrStr] = UNSET
    """Show images that feature people of the specified age category"""

    people_ethnicity: Optional[list[PeopleEthnicityOrStr]] = UNSET
    """Show images with people of the specified ethnicities, or start with NOT to show images without those
    ethnicities"""

    people_gender: Optional[PeopleGenderOrStr] = UNSET
    """Show images with people of the specified gender"""

    people_number: Optional[int] = UNSET
    """Show images with the specified number of people"""

    query: Optional[str] = UNSET
    """One or more search terms separated by spaces; you can use NOT to filter out images that match a term"""

    region: Optional[Region] = UNSET
    """Raise or lower search result rankings based on the result's relevance to a specified region; you can provide a
    country code or an IP address from which the API infers a country"""

    safe: Optional[bool] = UNSET
    """Enable or disable safe search"""

    sort: Optional[SortOrStr] = UNSET
    """Sort by"""

    spellcheck_query: Optional[bool] = UNSET
    """Spellcheck the search query and return results on suggested spellings"""

    view: Optional[ViewOrStr] = UNSET
    """Amount of detail to render in the response"""

    width: Optional[int] = UNSET
    """(Deprecated; use width_from and width_to instead) Show images with the specified width"""

    width_from: Optional[int] = UNSET
    """Show images with the specified width or larger, in pixels"""

    width_to: Optional[int] = UNSET
    """Show images with the specified width or smaller, in pixels"""


class SearchImageDict(TypedDict):
    added_date: NotRequired[Date]
    added_date_start: NotRequired[Date]
    aspect_ratio_min: NotRequired[float]
    aspect_ratio_max: NotRequired[float]
    aspect_ratio: NotRequired[float]
    added_date_end: NotRequired[Date]
    authentic: NotRequired[bool]
    category: NotRequired[str]
    color: NotRequired[str]
    contributor: NotRequired[list[str]]
    contributor_country: NotRequired[ContributorCountry | ContributorCountryDict]
    fields: NotRequired[str]
    height: NotRequired[int]
    height_from: NotRequired[int]
    height_to: NotRequired[int]
    image_type: NotRequired[list[ImageTypeOrStr]]
    keyword_safe_search: NotRequired[bool]
    language: NotRequired[Language2OrStr]
    license: NotRequired[list[LicenseOrStr]]
    model: NotRequired[list[str]]
    orientation: NotRequired[OrientationOrStr]
    page: NotRequired[int]
    per_page: NotRequired[int]
    people_model_released: NotRequired[bool]
    people_age: NotRequired[PeopleAgeOrStr]
    people_ethnicity: NotRequired[list[PeopleEthnicityOrStr]]
    people_gender: NotRequired[PeopleGenderOrStr]
    people_number: NotRequired[int]
    query: NotRequired[str]
    region: NotRequired[Region | RegionDict]
    safe: NotRequired[bool]
    sort: NotRequired[SortOrStr]
    spellcheck_query: NotRequired[bool]
    view: NotRequired[ViewOrStr]
    width: NotRequired[int]
    width_from: NotRequired[int]
    width_to: NotRequired[int]
