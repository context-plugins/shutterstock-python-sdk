from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetEditorialImageLivefeedItemsErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetEditorialImageLivefeedItemsError:
    def map(self, response: HttpResponse) -> GetEditorialImageLivefeedItemsErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404:
                return RawError(response)
            case _:
                return RawError(response)


get_editorial_image_livefeed_items_error_mapper: Final[
    ErrorMapper[GetEditorialImageLivefeedItemsErrorBody]
] = _GetEditorialImageLivefeedItemsError()
