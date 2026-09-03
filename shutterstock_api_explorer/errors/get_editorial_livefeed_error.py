from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetEditorialLivefeedErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetEditorialLivefeedError:
    def map(self, response: HttpResponse) -> GetEditorialLivefeedErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 406:
                return RawError(response)
            case _:
                return RawError(response)


get_editorial_livefeed_error_mapper: Final[ErrorMapper[GetEditorialLivefeedErrorBody]] = _GetEditorialLivefeedError()
