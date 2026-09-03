from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class License9(str, Enum):
    COMMERCIAL = "commercial"
    EDITORIAL = "editorial"

    __str__ = str.__str__


License9OrStr: TypeAlias = Annotated[License9 | str, open_enum_validator(License9)]
