from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class License(str, Enum):
    COMMERCIAL = "commercial"
    EDITORIAL = "editorial"
    ENHANCED = "enhanced"

    __str__ = str.__str__


LicenseOrStr: TypeAlias = Annotated[License | str, open_enum_validator(License)]
