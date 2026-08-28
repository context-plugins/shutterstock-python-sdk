from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

LicenseVideosErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _LicenseVideosError:
    def map(self, response: HttpResponse) -> LicenseVideosErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


license_videos_error_mapper: Final[ErrorMapper[LicenseVideosErrorBody]] = _LicenseVideosError()
