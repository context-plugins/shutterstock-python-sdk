from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DownloadAvailability(str, Enum):
    ALL = "all"
    DOWNLOADABLE = "downloadable"
    NON_DOWNLOADABLE = "non_downloadable"

    __str__ = str.__str__


DownloadAvailabilityOrStr: TypeAlias = Annotated[DownloadAvailability | str, open_enum_validator(DownloadAvailability)]
