from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetEditorialImageErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetEditorialImageError:
    def map(self, response: HttpResponse) -> GetEditorialImageErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404:
                return RawError(response)
            case _:
                return RawError(response)


get_editorial_image_error_mapper: Final[ErrorMapper[GetEditorialImageErrorBody]] = _GetEditorialImageError()
