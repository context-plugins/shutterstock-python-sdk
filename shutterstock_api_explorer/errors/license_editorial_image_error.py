from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

LicenseEditorialImageErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _LicenseEditorialImageError:
    def map(self, response: HttpResponse) -> LicenseEditorialImageErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 406:
                return RawError(response)
            case _:
                return RawError(response)


license_editorial_image_error_mapper: Final[ErrorMapper[LicenseEditorialImageErrorBody]] = _LicenseEditorialImageError()
