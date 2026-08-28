from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetAccessTokenErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetAccessTokenError:
    def map(self, response: HttpResponse) -> GetAccessTokenErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


get_access_token_error_mapper: Final[ErrorMapper[GetAccessTokenErrorBody]] = _GetAccessTokenError()
