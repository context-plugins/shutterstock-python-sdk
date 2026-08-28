from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetEditorialLivefeedListErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetEditorialLivefeedListError:
    def map(self, response: HttpResponse) -> GetEditorialLivefeedListErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 406:
                return RawError(response)
            case _:
                return RawError(response)


get_editorial_livefeed_list_error_mapper: Final[
    ErrorMapper[GetEditorialLivefeedListErrorBody]
] = _GetEditorialLivefeedListError()
