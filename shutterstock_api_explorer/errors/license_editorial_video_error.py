from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

LicenseEditorialVideoErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _LicenseEditorialVideoError:
    def map(self, response: HttpResponse) -> LicenseEditorialVideoErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


license_editorial_video_error_mapper: Final[ErrorMapper[LicenseEditorialVideoErrorBody]] = _LicenseEditorialVideoError()
