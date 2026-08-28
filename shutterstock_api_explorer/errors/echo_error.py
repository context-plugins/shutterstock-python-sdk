from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

EchoErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _EchoError:
    def map(self, response: HttpResponse) -> EchoErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


echo_error_mapper: Final[ErrorMapper[EchoErrorBody]] = _EchoError()
