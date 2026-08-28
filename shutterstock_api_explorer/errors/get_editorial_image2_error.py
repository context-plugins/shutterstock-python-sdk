from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetEditorialImage2ErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetEditorialImage2Error:
    def map(self, response: HttpResponse) -> GetEditorialImage2ErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404:
                return RawError(response)
            case _:
                return RawError(response)


get_editorial_image2_error_mapper: Final[ErrorMapper[GetEditorialImage2ErrorBody]] = _GetEditorialImage2Error()
