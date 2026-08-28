from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetImageErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetImageError:
    def map(self, response: HttpResponse) -> GetImageErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


get_image_error_mapper: Final[ErrorMapper[GetImageErrorBody]] = _GetImageError()
