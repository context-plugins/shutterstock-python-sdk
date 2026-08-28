from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

AuthorizeErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _AuthorizeError:
    def map(self, response: HttpResponse) -> AuthorizeErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


authorize_error_mapper: Final[ErrorMapper[AuthorizeErrorBody]] = _AuthorizeError()
