from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetUpdatedEditorialImageErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetUpdatedEditorialImageError:
    def map(self, response: HttpResponse) -> GetUpdatedEditorialImageErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 406:
                return RawError(response)
            case _:
                return RawError(response)


get_updated_editorial_image_error_mapper: Final[
    ErrorMapper[GetUpdatedEditorialImageErrorBody]
] = _GetUpdatedEditorialImageError()
