from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetEditorialImageLivefeedListErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetEditorialImageLivefeedListError:
    def map(self, response: HttpResponse) -> GetEditorialImageLivefeedListErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404:
                return RawError(response)
            case _:
                return RawError(response)


get_editorial_image_livefeed_list_error_mapper: Final[
    ErrorMapper[GetEditorialImageLivefeedListErrorBody]
] = _GetEditorialImageLivefeedListError()
