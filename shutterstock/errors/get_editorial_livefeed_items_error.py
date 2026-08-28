from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetEditorialLivefeedItemsErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetEditorialLivefeedItemsError:
    def map(self, response: HttpResponse) -> GetEditorialLivefeedItemsErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 406:
                return RawError(response)
            case _:
                return RawError(response)


get_editorial_livefeed_items_error_mapper: Final[
    ErrorMapper[GetEditorialLivefeedItemsErrorBody]
] = _GetEditorialLivefeedItemsError()
