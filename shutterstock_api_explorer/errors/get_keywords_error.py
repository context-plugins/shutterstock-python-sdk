from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetKeywordsErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetKeywordsError:
    def map(self, response: HttpResponse) -> GetKeywordsErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 415:
                return RawError(response)
            case _:
                return RawError(response)


get_keywords_error_mapper: Final[ErrorMapper[GetKeywordsErrorBody]] = _GetKeywordsError()
