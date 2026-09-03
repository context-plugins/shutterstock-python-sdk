from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

ValidateErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ValidateError:
    def map(self, response: HttpResponse) -> ValidateErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


validate_error_mapper: Final[ErrorMapper[ValidateErrorBody]] = _ValidateError()
