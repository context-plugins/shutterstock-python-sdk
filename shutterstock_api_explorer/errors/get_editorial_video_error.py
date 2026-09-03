from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetEditorialVideoErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetEditorialVideoError:
    def map(self, response: HttpResponse) -> GetEditorialVideoErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 406:
                return RawError(response)
            case _:
                return RawError(response)


get_editorial_video_error_mapper: Final[ErrorMapper[GetEditorialVideoErrorBody]] = _GetEditorialVideoError()
