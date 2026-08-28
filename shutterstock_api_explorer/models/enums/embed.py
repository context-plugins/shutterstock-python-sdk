from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Embed(str, Enum):
    SHARE_CODE = "share_code"
    SHARE_URL = "share_url"

    __str__ = str.__str__


EmbedOrStr: TypeAlias = Annotated[Embed | str, open_enum_validator(Embed)]
