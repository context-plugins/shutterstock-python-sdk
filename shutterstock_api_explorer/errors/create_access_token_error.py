from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

CreateAccessTokenErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _CreateAccessTokenError:
    def map(self, response: HttpResponse) -> CreateAccessTokenErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


create_access_token_error_mapper: Final[ErrorMapper[CreateAccessTokenErrorBody]] = _CreateAccessTokenError()
