from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class GrantType(str, Enum):
    """Grant type: authorization_code generates user tokens, client_credentials generates short-lived client grants"""

    AUTHORIZATION_CODE = "authorization_code"
    CLIENT_CREDENTIALS = "client_credentials"
    REFRESH_TOKEN = "refresh_token"

    __str__ = str.__str__


GrantTypeOrStr: TypeAlias = Annotated[GrantType | str, open_enum_validator(GrantType)]
