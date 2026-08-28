from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

LicenseTrackErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _LicenseTrackError:
    def map(self, response: HttpResponse) -> LicenseTrackErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


license_track_error_mapper: Final[ErrorMapper[LicenseTrackErrorBody]] = _LicenseTrackError()
