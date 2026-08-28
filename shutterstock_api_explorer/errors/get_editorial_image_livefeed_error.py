from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetEditorialImageLivefeedErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetEditorialImageLivefeedError:
    def map(self, response: HttpResponse) -> GetEditorialImageLivefeedErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404:
                return RawError(response)
            case _:
                return RawError(response)


get_editorial_image_livefeed_error_mapper: Final[
    ErrorMapper[GetEditorialImageLivefeedErrorBody]
] = _GetEditorialImageLivefeedError()
