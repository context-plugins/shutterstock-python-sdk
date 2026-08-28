from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Expires(str, Enum):
    """Whether or not the token expires, expiring tokens come with a refresh_token to renew the access_token"""

    TRUE = "true"
    FALSE = "false"

    __str__ = str.__str__


ExpiresOrStr: TypeAlias = Annotated[Expires | str, open_enum_validator(Expires)]
